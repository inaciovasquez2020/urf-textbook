import json
import math
from pathlib import Path

OUT = Path("artifacts/grf/mass_function_transition_probe.json")

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
    "m_prime",
]


def local_mass(r, a):
    return 0.5 * r * (1.0 - math.exp(-2.0 * a * r))


def local_mass_prime(r, a):
    e = math.exp(-2.0 * a * r)
    return 0.5 * (1.0 - e) + a * r * e


def local_mass_second(r, a):
    e = math.exp(-2.0 * a * r)
    return 2.0 * a * e - 2.0 * a * a * r * e


def quintic_coefficients(y0, d0, dd0, y1, d1, dd1, width):
    c0 = y0
    c1 = d0 * width
    c2 = 0.5 * dd0 * width * width

    Y = y1 - (c0 + c1 + c2)
    V = d1 * width - (c1 + 2.0 * c2)
    A = dd1 * width * width - 2.0 * c2

    c3 = 10.0 * Y - 4.0 * V + 0.5 * A
    c4 = -15.0 * Y + 7.0 * V - A
    c5 = 6.0 * Y - 3.0 * V + 0.5 * A

    return c0, c1, c2, c3, c4, c5


def quintic_eval(coeffs, t, width):
    c0, c1, c2, c3, c4, c5 = coeffs

    q = c0 + c1*t + c2*t*t + c3*t**3 + c4*t**4 + c5*t**5
    qt = c1 + 2*c2*t + 3*c3*t*t + 4*c4*t**3 + 5*c5*t**4
    qtt = 2*c2 + 6*c3*t + 12*c4*t*t + 20*c5*t**3

    return q, qt / width, qtt / (width * width)


def mass_fields(r, params):
    a = params["a"]
    r1 = params["r1"]
    R_out = params["R_out"]
    M = params["M"]

    if r <= r1:
        return (
            local_mass(r, a),
            local_mass_prime(r, a),
            local_mass_second(r, a),
        )

    if r >= R_out:
        return M, 0.0, 0.0

    width = R_out - r1
    coeffs = quintic_coefficients(
        local_mass(r1, a),
        local_mass_prime(r1, a),
        local_mass_second(r1, a),
        M,
        0.0,
        0.0,
        width,
    )
    t = (r - r1) / width
    return quintic_eval(coeffs, t, width)


def margins_from_mass(r, m, mp, mpp):
    f = 1.0 - 2.0 * m / r
    if f <= 0.0:
        raise ValueError("horizon or invalid radial factor encountered")

    lam_p = (mp / r - m / (r * r)) / f

    numerator = m / (r * r) - mp / r
    numerator_p = 2.0 * mp / (r * r) - 2.0 * m / (r**3) - mpp / r
    f_p = -2.0 * mp / r + 2.0 * m / (r * r)

    phi_p = numerator / f
    phi_pp = (numerator_p * f - numerator * f_p) / (f * f)

    rho = mp / (4.0 * math.pi * r * r)
    pr = -rho

    pt = (
        f
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
        "m_prime": mp,
    }


def evaluate(params):
    minima = {name: {"value": float("inf"), "r": None} for name in MARGIN_NAMES}
    r0 = params["r0"]
    R_out = params["R_out"]
    samples = int(params["samples"])

    for i in range(samples):
        r = r0 + (R_out - r0) * i / (samples - 1)
        try:
            m, mp, mpp = mass_fields(r, params)
            margins = margins_from_mass(r, m, mp, mpp)
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

    energy_names = ["rho", "rho_plus_pr", "rho_plus_pt", "rho_minus_pr", "rho_minus_pt"]
    energy_min = min(minima[name]["value"] for name in energy_names)
    status = "PASS_NUMERICAL_SAMPLE" if energy_min >= 0.0 else "FRONTIER_FAIL"

    return {
        "status": status,
        "parameters": params,
        "min_margins": minima,
        "minimum_value": energy_min,
    }


def run_search():
    a = BASE["a"]
    r1 = BASE["r1"]
    m1 = local_mass(r1, a)

    candidates = []

    for mass_factor in [1.01, 1.05, 1.1, 1.25, 1.5, 2.0, 3.0, 5.0, 8.0, 13.0, 21.0, 34.0, 55.0, 89.0, 144.0, 233.0]:
        M = mass_factor * m1
        for R_out in [50.0, 80.0, 120.0, 200.0, 350.0, 600.0, 1000.0, 2000.0, 5000.0, 10000.0]:
            if R_out <= max(r1, 2.5 * M):
                continue

            params = dict(BASE)
            params.update(
                {
                    "M": M,
                    "mass_factor": mass_factor,
                    "R_out": R_out,
                    "local_mass_at_r1": m1,
                    "ansatz": "C2 quintic mass-function transition with radial NEC saturation",
                }
            )
            candidates.append(evaluate(params))

    valid = [c for c in candidates if c["status"] in {"PASS_NUMERICAL_SAMPLE", "FRONTIER_FAIL"}]
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
            "Mass-function transition search. This uses the Misner-Sharp variable as "
            "the transition coordinate and chooses Phi prime by radial NEC saturation. "
            "A sampled pass is not a theorem. A sampled failure is not an impossibility theorem."
        ),
        "base": BASE,
        "candidate_count": len(candidates),
        "best_candidate": best,
        "next_missing_object": "interval-certified mass-function transition ansatz",
    }


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = run_search()
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
