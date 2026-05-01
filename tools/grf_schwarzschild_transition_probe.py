#!/usr/bin/env python3
import json
import math
from pathlib import Path

OUT = Path("artifacts/grf/schwarzschild_transition_probe.json")

BASE = {
    "a": 0.001,
    "r0": 10.0,
    "r1": 20.0,
    "samples": 4001,
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


def local_mass(r: float, a: float) -> float:
    return 0.5 * r * (1.0 - math.exp(-2.0 * a * r))


def local_fields(r: float, a: float):
    return {
        "phi": -a * r,
        "phi_p": -a,
        "phi_pp": 0.0,
        "lam": a * r,
        "lam_p": a,
        "lam_pp": 0.0,
    }


def schwarzschild_fields(r: float, M: float):
    f = 1.0 - 2.0 * M / r
    if f <= 0.0:
        raise ValueError("Schwarzschild exterior evaluated at or inside horizon")

    denom = r * r * f
    phi = 0.5 * math.log(f)
    phi_p = M / denom
    phi_pp = -2.0 * M * (r - M) / (denom * denom)

    lam = -0.5 * math.log(f)
    lam_p = -M / denom
    lam_pp = 2.0 * M * (r - M) / (denom * denom)

    return {
        "phi": phi,
        "phi_p": phi_p,
        "phi_pp": phi_pp,
        "lam": lam,
        "lam_p": lam_p,
        "lam_pp": lam_pp,
    }


def blended_fields(r: float, params):
    a = params["a"]
    r1 = params["r1"]
    Rout = params["R_out"]
    M = params["M"]

    if r <= r1:
        return local_fields(r, a)

    if r >= Rout:
        return schwarzschild_fields(r, M)

    width = Rout - r1
    t = (r - r1) / width
    h = smoothstep(t)
    hp = smoothstep_prime(t) / width
    hpp = smoothstep_second(t) / (width * width)

    L = local_fields(r, a)
    E = schwarzschild_fields(r, M)

    out = {}
    for key, deriv1, deriv2 in [
        ("phi", "phi_p", "phi_pp"),
        ("lam", "lam_p", "lam_pp"),
    ]:
        f0 = L[key]
        f0p = L[deriv1]
        f0pp = L[deriv2]

        f1 = E[key]
        f1p = E[deriv1]
        f1pp = E[deriv2]

        diff = f1 - f0
        diffp = f1p - f0p
        diffpp = f1pp - f0pp

        out[key] = f0 + h * diff
        out[deriv1] = f0p + hp * diff + h * diffp
        out[deriv2] = f0pp + hpp * diff + 2.0 * hp * diffp + h * diffpp

    return out


def energy_margins(r: float, fields):
    phi_p = fields["phi_p"]
    phi_pp = fields["phi_pp"]
    lam = fields["lam"]
    lam_p = fields["lam_p"]

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


def evaluate(params):
    r0 = params["r0"]
    Rout = params["R_out"]
    samples = int(params["samples"])

    minima = {name: {"value": float("inf"), "r": None} for name in MARGIN_NAMES}

    for i in range(samples):
        r = r0 + (Rout - r0) * i / (samples - 1)
        try:
            fields = blended_fields(r, params)
            margins = energy_margins(r, fields)
        except (ValueError, OverflowError, ZeroDivisionError):
            return {
                "status": "INVALID",
                "parameters": params,
                "min_margins": minima,
                "minimum_value": None,
            }

        for name, value in margins.items():
            if value < minima[name]["value"]:
                minima[name] = {"value": value, "r": r}

    min_value = min(item["value"] for item in minima.values())
    status = "PASS_NUMERICAL_SAMPLE" if min_value >= 0.0 else "FRONTIER_FAIL"
    return {
        "status": status,
        "parameters": params,
        "min_margins": minima,
        "minimum_value": min_value,
    }


def run_search():
    a = BASE["a"]
    r1 = BASE["r1"]
    m1 = local_mass(r1, a)

    candidates = []
    for mass_factor in [1.0, 1.05, 1.1, 1.25, 1.5, 2.0, 3.0, 5.0, 8.0, 13.0]:
        M = mass_factor * m1
        for R_out in [50.0, 80.0, 120.0, 200.0, 350.0, 600.0, 1000.0]:
            if R_out <= max(r1, 2.5 * M):
                continue
            params = dict(BASE)
            params.update(
                {
                    "M": M,
                    "mass_factor": mass_factor,
                    "R_out": R_out,
                    "exterior": "positive-mass Schwarzschild",
                    "local_mass_at_r1": m1,
                }
            )
            candidates.append(evaluate(params))

    valid = [c for c in candidates if c["status"] != "INVALID"]
    passing = [c for c in valid if c["status"] == "PASS_NUMERICAL_SAMPLE"]

    if passing:
        best = max(passing, key=lambda c: c["minimum_value"])
        status = "PASS_NUMERICAL_SAMPLE"
    else:
        best = max(valid, key=lambda c: c["minimum_value"])
        status = "FRONTIER_FAIL"

    return {
        "status": status,
        "interpretation": (
            "Grid search over positive-mass Schwarzschild smoothstep transitions. "
            "A PASS_NUMERICAL_SAMPLE is only sampled numerical evidence, not interval proof. "
            "A FRONTIER_FAIL means this finite grid found no sampled nonnegative shell."
        ),
        "base": BASE,
        "candidate_count": len(candidates),
        "best_candidate": best,
        "next_missing_object": "interval-certified positive-mass Schwarzschild transition ansatz",
    }


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = run_search()
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
