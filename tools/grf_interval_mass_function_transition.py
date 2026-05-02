#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


OUT = Path("artifacts/grf/interval_mass_function_transition_probe.json")


@dataclass(frozen=True)
class I:
    lo: float
    hi: float

    def __post_init__(self):
        if not (math.isfinite(self.lo) and math.isfinite(self.hi)):
            raise ValueError((self.lo, self.hi))
        if self.lo > self.hi:
            raise ValueError((self.lo, self.hi))

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other):
        other = as_i(other)
        return I(self.lo - other.hi, self.hi - other.lo)

    def __mul__(self, other):
        other = as_i(other)
        xs = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return I(min(xs), max(xs))

    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError(other)
        xs = (
            self.lo / other.lo,
            self.lo / other.hi,
            self.hi / other.lo,
            self.hi / other.hi,
        )
        return I(min(xs), max(xs))

    def neg(self):
        return I(-self.hi, -self.lo)

    def sq(self):
        if self.lo <= 0 <= self.hi:
            return I(0.0, max(self.lo * self.lo, self.hi * self.hi))
        xs = (self.lo * self.lo, self.hi * self.hi)
        return I(min(xs), max(xs))

    def exp(self):
        return I(math.exp(self.lo), math.exp(self.hi))

    def lower(self):
        return self.lo

    def upper(self):
        return self.hi


def as_i(x):
    return x if isinstance(x, I) else I(float(x), float(x))


def hull(*xs: float) -> I:
    return I(min(xs), max(xs))


def quintic(s: I) -> I:
    return I(10, 10) * s * s * s - I(15, 15) * s * s * s * s + I(6, 6) * s * s * s * s * s


def d_quintic(s: I) -> I:
    return I(30, 30) * s * s * (I(1, 1) - s) * (I(1, 1) - s)


def dd_quintic(s: I) -> I:
    return I(60, 60) * s * (I(1, 1) - s) * (I(1, 1) - I(2, 2) * s)


def local_mass(a: float, r: float) -> float:
    beta = math.exp(2 * a * r)
    return 0.5 * r * (1.0 - 1.0 / beta)


def margin_intervals(
    *,
    a: float,
    r1: float,
    rout: float,
    mass_factor: float,
    cells: int,
):
    m1 = local_mass(a, r1)
    m2 = m1 * mass_factor
    width = rout - r1

    margins = {
        "m_prime": [],
        "rho": [],
        "rho_minus_pr": [],
        "rho_minus_pt": [],
        "rho_plus_pr": [],
        "rho_plus_pt": [],
    }

    for j in range(cells):
        r = I(r1 + width * j / cells, r1 + width * (j + 1) / cells)
        s = (r - r1) / width

        q = quintic(s)
        qp = d_quintic(s) / width
        qpp = dd_quintic(s) / (width * width)

        m = I(m1, m1) + I(m2 - m1, m2 - m1) * q
        mp = I(m2 - m1, m2 - m1) * qp
        mpp = I(m2 - m1, m2 - m1) * qpp

        one = I(1, 1)
        two = I(2, 2)
        four = I(4, 4)

        beta = one / (one - two * m / r)
        x = two * m / r
        if x.hi >= 1:
            raise ValueError("horizon-crossing interval")

        rho = mp / (r * r)

        phi_p = beta * mp / (r * r)
        beta_p_over_beta = (two * mp / r - two * m / (r * r)) / (one - two * m / r)

        pr = rho.neg()
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

        for k, v in vals.items():
            margins[k].append({"cell": j, "r": [r.lo, r.hi], "lo": v.lo, "hi": v.hi})

    return margins


def summarize(margins):
    out = {}
    for name, cells in margins.items():
        worst = min(cells, key=lambda c: c["lo"])
        out[name] = worst
    return out


def certified_pass(summary):
    return all(v["lo"] >= 0 for v in summary.values())


def main():
    base = {
        "a": 0.001,
        "r1": 20.0,
        "cells": 400,
    }

    candidates = []
    for rout in (200.0, 400.0, 600.0, 800.0, 1000.0):
        for mass_factor in (1.25, 1.5, 2.0, 3.0, 5.0, 8.0, 13.0, 21.0, 34.0, 55.0, 89.0, 144.0, 233.0):
            try:
                margins = margin_intervals(
                    a=base["a"],
                    r1=base["r1"],
                    rout=rout,
                    mass_factor=mass_factor,
                    cells=base["cells"],
                )
                summary = summarize(margins)
                status = "CERTIFIED_PASS" if certified_pass(summary) else "FRONTIER_OPEN"
                score = min(v["lo"] for v in summary.values())
                candidates.append(
                    {
                        "parameters": {
                            "a": base["a"],
                            "r1": base["r1"],
                            "R_out": rout,
                            "mass_factor": mass_factor,
                            "cells": base["cells"],
                            "ansatz": "interval C2 quintic positive-mass Misner-Sharp transition with radial NEC saturation",
                        },
                        "status": status,
                        "minimum_certified_lower_bound": score,
                        "certified_margin_lower_bounds": summary,
                    }
                )
            except Exception as e:
                candidates.append(
                    {
                        "parameters": {
                            "a": base["a"],
                            "r1": base["r1"],
                            "R_out": rout,
                            "mass_factor": mass_factor,
                            "cells": base["cells"],
                        },
                        "status": "INVALID_INTERVAL",
                        "error": str(e),
                        "minimum_certified_lower_bound": float("-inf"),
                    }
                )

    best = max(candidates, key=lambda c: c["minimum_certified_lower_bound"])

    payload = {
        "status": best["status"],
        "candidate_count": len(candidates),
        "best_candidate": best,
        "interpretation": "Interval mass-function transition search using outward-rounded conservative interval enclosures. CERTIFIED_PASS would certify nonnegative sampled-cell lower bounds for the encoded ansatz only. FRONTIER_OPEN is not an impossibility theorem.",
        "next_missing_object": "certified positive lower bound or replacement ansatz with interval certificate",
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
