#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path

OUT = Path("artifacts/grf/inner_boundary_control_probe.json")


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

    def __neg__(self):
        return self.neg()


def as_i(x):
    return x if isinstance(x, I) else I(float(x), float(x))


def local_mass(a: float, r: float) -> float:
    beta = math.exp(2.0 * a * r)
    return 0.5 * r * (1.0 - 1.0 / beta)


def basis(s: I):
    one = I(1, 1)
    two = I(2, 2)
    three = I(3, 3)
    four = I(4, 4)
    six = I(6, 6)
    seven = I(7, 7)
    eight = I(8, 8)
    ten = I(10, 10)
    fifteen = I(15, 15)

    h00 = one - ten*s*s*s + fifteen*s*s*s*s - six*s*s*s*s*s
    h01 = ten*s*s*s - fifteen*s*s*s*s + six*s*s*s*s*s
    h10 = s - six*s*s*s + eight*s*s*s*s - three*s*s*s*s*s
    h11 = four.neg()*s*s*s + seven*s*s*s*s - three*s*s*s*s*s
    h20 = (s*s - three*s*s*s + three*s*s*s*s - s*s*s*s*s) / two
    h21 = (s*s*s - two*s*s*s*s + s*s*s*s*s) / two
    return h00, h01, h10, h11, h20, h21


def basis_d(s: I):
    one = I(1, 1)
    two = I(2, 2)

    h00 = -I(30, 30)*s*s + I(60, 60)*s*s*s - I(30, 30)*s*s*s*s
    h01 = I(30, 30)*s*s - I(60, 60)*s*s*s + I(30, 30)*s*s*s*s
    h10 = one - I(18, 18)*s*s + I(32, 32)*s*s*s - I(15, 15)*s*s*s*s
    h11 = -I(12, 12)*s*s + I(28, 28)*s*s*s - I(15, 15)*s*s*s*s
    h20 = (I(2, 2)*s - I(9, 9)*s*s + I(12, 12)*s*s*s - I(5, 5)*s*s*s*s) / two
    h21 = (I(3, 3)*s*s - I(8, 8)*s*s*s + I(5, 5)*s*s*s*s) / two
    return h00, h01, h10, h11, h20, h21


def basis_dd(s: I):
    two = I(2, 2)

    h00 = -I(60, 60)*s + I(180, 180)*s*s - I(120, 120)*s*s*s
    h01 = I(60, 60)*s - I(180, 180)*s*s + I(120, 120)*s*s*s
    h10 = -I(36, 36)*s + I(96, 96)*s*s - I(60, 60)*s*s*s
    h11 = -I(24, 24)*s + I(84, 84)*s*s - I(60, 60)*s*s*s
    h20 = (two - I(18, 18)*s + I(36, 36)*s*s - I(20, 20)*s*s*s) / two
    h21 = (I(6, 6)*s - I(24, 24)*s*s + I(20, 20)*s*s*s) / two
    return h00, h01, h10, h11, h20, h21


def lincomb(coeffs, vals):
    out = I(0.0, 0.0)
    for c, v in zip(coeffs, vals):
        out = out + I(c, c) * v
    return out


def evaluate_candidate(*, a: float, r1: float, rout: float, mass_factor: float, d0_scale: float, dd0_scale: float, cells: int):
    m1 = local_mass(a, r1)
    m2 = m1 * mass_factor
    width = rout - r1

    y0 = m1
    y1 = m2
    d0 = width * d0_scale * (m2 - m1) / width
    d1 = 0.0
    dd0 = width * width * dd0_scale * (m2 - m1) / (width * width)
    dd1 = 0.0

    worst = {}

    for j in range(cells):
        r = I(r1 + width * j / cells, r1 + width * (j + 1) / cells)
        s = (r - r1) / width

        coeffs = [y0, y1, d0, d1, dd0, dd1]
        m = lincomb(coeffs, basis(s))
        mp = lincomb(coeffs, basis_d(s)) / width
        mpp = lincomb(coeffs, basis_dd(s)) / (width * width)

        one = I(1, 1)
        two = I(2, 2)

        compactness = two * m / r
        if compactness.hi >= 1:
            return {
                "parameters": {
                    "a": a,
                    "r1": r1,
                    "R_out": rout,
                    "mass_factor": mass_factor,
                    "d0_scale": d0_scale,
                    "dd0_scale": dd0_scale,
                    "cells": cells,
                    "ansatz": "small-amplitude quintic Hermite mass transition with inner-boundary control",
                },
                "certified_margin_lower_bounds": {
                    "m_prime": {"cell": -1, "r": [r.lo, r.hi], "lo": float("-inf"), "hi": float("inf")},
                    "rho": {"cell": -1, "r": [r.lo, r.hi], "lo": float("-inf"), "hi": float("inf")},
                    "rho_minus_pr": {"cell": -1, "r": [r.lo, r.hi], "lo": float("-inf"), "hi": float("inf")},
                    "rho_minus_pt": {"cell": -1, "r": [r.lo, r.hi], "lo": float("-inf"), "hi": float("inf")},
                    "rho_plus_pr": {"cell": -1, "r": [r.lo, r.hi], "lo": float("-inf"), "hi": float("inf")},
                    "rho_plus_pt": {"cell": -1, "r": [r.lo, r.hi], "lo": float("-inf"), "hi": float("inf")},
                },
                "minimum_certified_lower_bound": float("-inf"),
                "status": "FRONTIER_OPEN",
            }

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
            "d0_scale": d0_scale,
            "dd0_scale": dd0_scale,
            "cells": cells,
            "ansatz": "small-amplitude quintic Hermite mass transition with inner-boundary control",
        },
        "certified_margin_lower_bounds": worst,
        "minimum_certified_lower_bound": minimum,
        "status": "CERTIFIED_PASS" if minimum >= 0 else "FRONTIER_OPEN",
    }


def main():
    grid = {
        "a": 0.001,
        "r1": 20.0,
        "cells": 600,
        "R_out": [20.05, 20.1, 20.25, 20.5, 21.0, 22.0, 25.0, 30.0],
        "mass_factor": [1.0, 1.0 + 1e-14, 1.0 + 1e-13, 1.0 + 1e-12, 1.0 + 1e-11, 1.0 + 1e-10, 1.0 + 1e-9, 1.0 + 1e-8],
        "d0_scale": [0.0, 0.1, 0.25, 0.5, 1.0],
        "dd0_scale": [-1.0, -0.5, 0.0, 0.5, 1.0],
    }

    candidates = []
    for rout in grid["R_out"]:
        for mf in grid["mass_factor"]:
            for d0s in grid["d0_scale"]:
                for dd0s in grid["dd0_scale"]:
                    candidates.append(
                        evaluate_candidate(
                            a=grid["a"],
                            r1=grid["r1"],
                            rout=rout,
                            mass_factor=mf,
                            d0_scale=d0s,
                            dd0_scale=dd0s,
                            cells=grid["cells"],
                        )
                    )

    best = max(candidates, key=lambda c: c["minimum_certified_lower_bound"])

    payload = {
        "status": best["status"],
        "candidate_count": len(candidates),
        "best_candidate": best,
        "targeted_cell": "inner boundary cell",
        "targeted_margin": "rho_minus_pt",
        "interpretation": "Small-scale inner-boundary Hermite interval search. CERTIFIED_PASS would certify the encoded finite interval partition and ansatz family only. FRONTIER_OPEN is not an impossibility theorem.",
        "next_missing_object": "inner-boundary tangential-pressure control with certified nonnegative rho_minus_pt and all WEC/DEC margins",
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
