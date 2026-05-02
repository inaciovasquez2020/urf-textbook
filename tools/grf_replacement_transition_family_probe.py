#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path

OUT = Path("artifacts/grf/replacement_transition_family_probe.json")


@dataclass(frozen=True)
class I:
    lo: float
    hi: float

    def __post_init__(self):
        if not math.isfinite(self.lo) or not math.isfinite(self.hi) or self.lo > self.hi:
            raise ValueError((self.lo, self.hi))

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other):
        other = as_i(other)
        return I(self.lo - other.hi, self.hi - other.lo)

    def __mul__(self, other):
        other = as_i(other)
        vals = (self.lo * other.lo, self.lo * other.hi, self.hi * other.lo, self.hi * other.hi)
        return I(min(vals), max(vals))

    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError(other)
        vals = (self.lo / other.lo, self.lo / other.hi, self.hi / other.lo, self.hi / other.hi)
        return I(min(vals), max(vals))

    def neg(self):
        return I(-self.hi, -self.lo)


def as_i(x):
    return x if isinstance(x, I) else I(float(x), float(x))


def q0(s: I) -> I:
    return I(10, 10) * s * s * s - I(15, 15) * s * s * s * s + I(6, 6) * s * s * s * s * s


def dq0(s: I) -> I:
    return I(30, 30) * s * s * (I(1, 1) - s) * (I(1, 1) - s)


def ddq0(s: I) -> I:
    return I(60, 60) * s * (I(1, 1) - s) * (I(1, 1) - I(2, 2) * s)


def bump(s: I) -> I:
    return s * s * s * (I(1, 1) - s) * (I(1, 1) - s) * (I(1, 1) - s)


def dbump(s: I) -> I:
    return I(3, 3) * s * s * (I(1, 1) - s) * (I(1, 1) - s) * (I(1, 1) - I(2, 2) * s)


def ddbump(s: I) -> I:
    return I(6, 6) * s * (I(1, 1) - s) * (I(1, 1) - I(5, 5) * s + I(5, 5) * s * s)


def q_family(s: I, lam: float) -> I:
    return q0(s) + I(lam, lam) * bump(s)


def dq_family(s: I, lam: float) -> I:
    return dq0(s) + I(lam, lam) * dbump(s)


def ddq_family(s: I, lam: float) -> I:
    return ddq0(s) + I(lam, lam) * ddbump(s)


def local_mass(a: float, r: float) -> float:
    beta = math.exp(2.0 * a * r)
    return 0.5 * r * (1.0 - 1.0 / beta)


def evaluate_candidate(*, a: float, r1: float, rout: float, mass_factor: float, lam: float, cells: int):
    m1 = local_mass(a, r1)
    m2 = m1 * mass_factor
    width = rout - r1
    worst = {}

    for j in range(cells):
        r = I(r1 + width * j / cells, r1 + width * (j + 1) / cells)
        s = (r - r1) / width

        q = q_family(s, lam)
        qp = dq_family(s, lam) / width
        qpp = ddq_family(s, lam) / (width * width)

        m = I(m1, m1) + I(m2 - m1, m2 - m1) * q
        mp = I(m2 - m1, m2 - m1) * qp
        mpp = I(m2 - m1, m2 - m1) * qpp

        one = I(1, 1)
        two = I(2, 2)

        compactness = two * m / r
        if compactness.hi >= 1:
            raise ValueError("horizon-crossing interval")

        beta = one / (one - compactness)
        beta_p_over_beta = (two * mp / r - two * m / (r * r)) / (one - compactness)

        rho = mp / (r * r)
        pr = rho.neg()

        phi_p = beta * mp / (r * r)

        pt = (
            one / beta
            * (
                phi_p * phi_p
                + (mpp / (r * r) - two * mp / (r * r * r)) * beta
                + beta_p_over_beta.neg() * phi_p / two
                + phi_p / r
                + beta_p_over_beta.neg() / (two * r)
            )
        )

        vals = {
            "m_prime": mp,
            "rho": rho,
            "rho_minus_pr": rho - pr,
            "rho_minus_pt": rho - pt,
            "rho_plus_pr": rho + pr,
            "rho_plus_pt": rho + pt,
        }

        for name, val in vals.items():
            rec = {"cell": j, "r": [r.lo, r.hi], "lo": val.lo, "hi": val.hi}
            if name not in worst or rec["lo"] < worst[name]["lo"]:
                worst[name] = rec

    minimum = min(v["lo"] for v in worst.values())
    return {
        "parameters": {
            "a": a,
            "r1": r1,
            "R_out": rout,
            "mass_factor": mass_factor,
            "lambda": lam,
            "cells": cells,
            "ansatz": "C2 quintic plus endpoint-flat cubic bump perturbation with radial NEC saturation",
        },
        "certified_margin_lower_bounds": worst,
        "minimum_certified_lower_bound": minimum,
        "status": "CERTIFIED_PASS" if minimum >= 0 else "FRONTIER_OPEN",
    }


def main():
    candidates = []
    grid = {
        "a": 0.001,
        "r1": 20.0,
        "cells": 400,
        "R_out": [120.0, 160.0, 200.0, 300.0, 500.0, 800.0, 1000.0],
        "mass_factor": [1.01, 1.05, 1.1, 1.25, 1.5, 2.0, 3.0, 5.0, 8.0, 13.0, 21.0, 34.0, 55.0, 89.0, 144.0, 233.0],
        "lambda": [-120.0, -80.0, -40.0, -20.0, -10.0, -5.0, -2.0, 0.0, 2.0, 5.0, 10.0, 20.0, 40.0, 80.0, 120.0],
    }

    for rout in grid["R_out"]:
        for mf in grid["mass_factor"]:
            for lam in grid["lambda"]:
                try:
                    candidates.append(
                        evaluate_candidate(
                            a=grid["a"],
                            r1=grid["r1"],
                            rout=rout,
                            mass_factor=mf,
                            lam=lam,
                            cells=grid["cells"],
                        )
                    )
                except Exception as e:
                    candidates.append(
                        {
                            "parameters": {
                                "a": grid["a"],
                                "r1": grid["r1"],
                                "R_out": rout,
                                "mass_factor": mf,
                                "lambda": lam,
                                "cells": grid["cells"],
                            },
                            "status": "INVALID_INTERVAL",
                            "error": str(e),
                            "minimum_certified_lower_bound": float("-inf"),
                            "certified_margin_lower_bounds": {},
                        }
                    )

    best = max(candidates, key=lambda c: c["minimum_certified_lower_bound"])

    payload = {
        "status": best["status"],
        "candidate_count": len(candidates),
        "best_candidate": best,
        "interpretation": "Replacement transition-family interval search. CERTIFIED_PASS would certify the encoded finite interval partition and ansatz family only. FRONTIER_OPEN is not an impossibility theorem.",
        "targeted_margin": "rho_minus_pt",
        "next_missing_object": "replacement transition family with certified nonnegative rho_minus_pt and all WEC/DEC margins",
        "boundary": [
            "This is an interval arithmetic frontier probe.",
            "It is not a theorem of global existence.",
            "It is not an impossibility theorem.",
            "It does not promote sampled numerical evidence to proof.",
            "It only certifies the encoded finite interval partition and ansatz family.",
        ],
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
