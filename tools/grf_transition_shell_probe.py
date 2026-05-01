#!/usr/bin/env python3
import json
import math
from pathlib import Path

OUT = Path("artifacts/grf/transition_shell_probe.json")

PARAMS = {
    "a": 0.001,
    "r0": 10.0,
    "r1": 20.0,
    "R_out": 200.0,
    "samples": 5001,
    "exterior": "flat",
}

MARGIN_NAMES = [
    "rho",
    "rho_plus_pr",
    "rho_plus_pt",
    "rho_minus_pr",
    "rho_minus_pt",
]


def smoothstep(t: float) -> float:
    return 6.0 * t**5 - 15.0 * t**4 + 10.0 * t**3


def smoothstep_prime(t: float) -> float:
    return 30.0 * t**4 - 60.0 * t**3 + 30.0 * t**2


def smoothstep_second(t: float) -> float:
    return 120.0 * t**3 - 180.0 * t**2 + 60.0 * t


def local_fields(r: float, a: float):
    phi = -a * r
    phi_p = -a
    phi_pp = 0.0
    lam = a * r
    lam_p = a
    lam_pp = 0.0
    return phi, phi_p, phi_pp, lam, lam_p, lam_pp


def flat_fields(_r: float):
    return 0.0, 0.0, 0.0, 0.0, 0.0, 0.0


def blended_fields(r: float, params):
    a = params["a"]
    r1 = params["r1"]
    R_out = params["R_out"]

    if r <= r1:
        return local_fields(r, a)

    if r >= R_out:
        return flat_fields(r)

    width = R_out - r1
    t = (r - r1) / width
    h = smoothstep(t)
    hp = smoothstep_prime(t) / width
    hpp = smoothstep_second(t) / (width * width)

    phi0, phi0_p, phi0_pp, lam0, lam0_p, lam0_pp = local_fields(r, a)

    # Exterior is flat, so field_ext = field_ext' = field_ext'' = 0.
    phi = (1.0 - h) * phi0
    phi_p = (1.0 - h) * phi0_p - hp * phi0
    phi_pp = (1.0 - h) * phi0_pp - 2.0 * hp * phi0_p - hpp * phi0

    lam = (1.0 - h) * lam0
    lam_p = (1.0 - h) * lam0_p - hp * lam0
    lam_pp = (1.0 - h) * lam0_pp - 2.0 * hp * lam0_p - hpp * lam0

    return phi, phi_p, phi_pp, lam, lam_p, lam_pp


def energy_margins(r: float, fields):
    phi, phi_p, phi_pp, lam, lam_p, _lam_pp = fields
    e = math.exp(-2.0 * lam)

    rho = ((1.0 - e) / (r * r) + 2.0 * lam_p * e / r) / (8.0 * math.pi)
    pr = (-(1.0 - e) / (r * r) + 2.0 * phi_p * e / r) / (8.0 * math.pi)
    pt = (
        e
        * (
            phi_pp
            + phi_p * phi_p
            - phi_p * lam_p
            + (phi_p - lam_p) / r
        )
        / (8.0 * math.pi)
    )

    return {
        "rho": rho,
        "rho_plus_pr": rho + pr,
        "rho_plus_pt": rho + pt,
        "rho_minus_pr": rho - pr,
        "rho_minus_pt": rho - pt,
    }


def run_probe(params):
    r0 = params["r0"]
    R_out = params["R_out"]
    samples = int(params["samples"])

    minima = {
        name: {"value": float("inf"), "r": None}
        for name in MARGIN_NAMES
    }

    for i in range(samples):
        r = r0 + (R_out - r0) * i / (samples - 1)
        margins = energy_margins(r, blended_fields(r, params))
        for name, value in margins.items():
            if value < minima[name]["value"]:
                minima[name] = {"value": value, "r": r}

    min_value = min(item["value"] for item in minima.values())
    status = "PASS_NUMERICAL_SAMPLE" if min_value >= 0.0 else "FRONTIER_FAIL"

    return {
        "status": status,
        "candidate": "C2 smoothstep from local alpha-beta certificate to flat exterior",
        "parameters": params,
        "min_margins": minima,
        "minimum_value": min_value,
        "interpretation": (
            "Default smoothstep matching fails at least one sampled WEC/DEC margin; "
            "global matching remains open and requires a different transition ansatz "
            "or interval-certified construction."
        ),
    }


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = run_probe(PARAMS)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
