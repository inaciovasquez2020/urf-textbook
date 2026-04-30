#!/usr/bin/env python3
"""
VTD Anti-Gravity Certificate Verifier.

Certificate tested:
    |a_hat(t*) + g_cert| > eps_meas + eps_F + eps_g

If the supplied certificates are valid, this falsifies
    H0: z''(t*) = -g + F_non_gravity(t*)/m,
        |F_non_gravity(t*)|/m <= eps_F,

and certifies the lower bound
    |g_eff - g_true| >= |a_hat(t*) + g_cert| - eps_meas - eps_F - eps_g > 0.

Boundary:
    This verifier certifies a trajectory anomaly relative to ordinary force
    balance. It does not identify the physical mechanism as anti-gravity.
"""
from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass(frozen=True)
class EvalRow:
    idx: int
    t: float
    a_hat: float
    lhs: float
    margin: float
    certified: bool
    cond: float


def die(msg: str) -> None:
    raise SystemExit(f"ERROR: {msg}")


def require_finite_nonnegative(name: str, value: float) -> None:
    if not math.isfinite(value) or value < 0:
        die(f"{name} must be finite and nonnegative")


def require_finite_positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        die(f"{name} must be finite and positive")


def load_csv(path: str) -> tuple[np.ndarray, np.ndarray]:
    t: list[float] = []
    z: list[float] = []
    with open(path, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or row[0].strip().startswith("#"):
                continue
            if len(row) < 2:
                continue
            try:
                ti = float(row[0])
                zi = float(row[1])
            except ValueError:
                continue
            t.append(ti)
            z.append(zi)

    if len(t) == 0:
        die("CSV contains no numeric t,z rows")

    t_arr = np.asarray(t, dtype=float)
    z_arr = np.asarray(z, dtype=float)

    if not np.all(np.isfinite(t_arr)) or not np.all(np.isfinite(z_arr)):
        die("CSV contains non-finite numeric values")
    if np.any(np.diff(t_arr) <= 0):
        die("time column must be strictly increasing")

    return t_arr, z_arr


def second_derivative_weights(
    t: np.ndarray,
    idx: int,
    window: int,
    degree: int,
) -> tuple[np.ndarray, float]:
    half = window // 2
    lo = idx - half
    hi = idx + half + 1

    if lo < 0 or hi > len(t):
        die("evaluation index does not admit the chosen centered window")

    dt = t[lo:hi] - t[idx]
    scale = float(np.max(np.abs(dt)))

    if not math.isfinite(scale) or scale <= 0:
        die("invalid local time scale")

    x = dt / scale
    V = np.vander(x, degree + 1, increasing=True)
    pinv = np.linalg.pinv(V)

    functional = np.zeros(degree + 1)
    functional[2] = 2.0 / (scale * scale)

    weights = functional @ pinv
    cond = float(np.linalg.cond(V))

    return weights, cond


def local_second_derivative(
    t: np.ndarray,
    z: np.ndarray,
    idx: int,
    window: int,
    degree: int,
) -> tuple[float, float]:
    half = window // 2
    weights, cond = second_derivative_weights(t, idx, window, degree)
    local_z = z[idx - half : idx + half + 1]
    return float(weights @ local_z), cond


def evaluation_indices(
    t: np.ndarray,
    window: int,
    index: int | None,
    time: float | None,
) -> list[int]:
    half = window // 2
    valid = range(half, len(t) - half)

    if index is not None and time is not None:
        die("use only one of --index or --time")

    if index is not None:
        if index not in valid:
            die("--index is outside the interior range allowed by --window")
        return [index]

    if time is not None:
        if not math.isfinite(time):
            die("--time must be finite")
        idx = int(np.argmin(np.abs(t - time)))
        if idx not in valid:
            die("nearest --time index is outside the interior range allowed by --window")
        return [idx]

    return list(valid)


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", help="CSV with columns t,z in SI units")
    ap.add_argument("--m", type=float, required=True, help="mass in kg")
    ap.add_argument("--g", type=float, required=True, help="certified local gravitational acceleration in m/s^2")
    ap.add_argument("--eps-g", type=float, default=0.0, help="certified |g_cert-g_true| bound in m/s^2")
    ap.add_argument("--eps-meas", type=float, required=True, help="certified |a_hat-a_true| bound in m/s^2")
    ap.add_argument("--eps-F", type=float, required=True, help="certified |F_non_gravity|/m bound in m/s^2")
    ap.add_argument("--window", type=int, default=21, help="odd number of samples in each local fit")
    ap.add_argument("--degree", type=int, default=4, help="local polynomial degree, at least 2")
    ap.add_argument("--index", type=int, default=None, help="evaluate only this row index; zero-based")
    ap.add_argument("--time", type=float, default=None, help="evaluate only the row nearest this time")
    ap.add_argument("--quiet", action="store_true", help="print only the final certificate block")
    return ap.parse_args()


def main() -> int:
    args = parse_args()

    require_finite_positive("m", args.m)
    require_finite_positive("g", args.g)
    require_finite_nonnegative("eps_g", args.eps_g)
    require_finite_nonnegative("eps_meas", args.eps_meas)
    require_finite_nonnegative("eps_F", args.eps_F)

    if args.degree < 2:
        die("degree must be >= 2")
    if args.window < args.degree + 1:
        die("window must be >= degree+1")
    if args.window % 2 == 0:
        die("window must be odd")

    t, z = load_csv(args.csv)

    if len(t) < args.window:
        die("not enough samples for the chosen window")

    indices = evaluation_indices(t, args.window, args.index, args.time)
    threshold = args.eps_meas + args.eps_F + args.eps_g
    rows: list[EvalRow] = []

    for idx in indices:
        a_hat, cond = local_second_derivative(t, z, idx, args.window, args.degree)
        lhs = abs(a_hat + args.g)
        margin = lhs - threshold
        rows.append(EvalRow(idx, float(t[idx]), a_hat, lhs, margin, margin > 0.0, cond))

    best = max(rows, key=lambda r: r.margin)
    any_cert = any(r.certified for r in rows)

    if not args.quiet:
        print(f"# VTD verifier: {Path(args.csv).name}")
        print(f"# evaluated_points = {len(rows)}")
        print(f"# threshold = eps_meas + eps_F + eps_g = {threshold:.12g} m/s^2")
        if len(rows) > 1:
            print("# scan mode: eps_meas and eps_F must be valid uniformly over all evaluated points")
        print("idx,t*,a_hat,abs(a_hat+g),margin,certified,cond")
        for r in rows:
            print(
                f"{r.idx},{r.t:.12g},{r.a_hat:.12g},"
                f"{r.lhs:.12g},{r.margin:.12g},{r.certified},{r.cond:.6g}"
            )

    print("\n# === VTD certificate ===")
    print(f"evaluated_points = {len(rows)}")
    print(f"threshold_m_s2 = {threshold:.12g}")
    print(f"best_index = {best.idx}")
    print(f"best_t_s = {best.t:.12g}")
    print(f"best_a_hat_m_s2 = {best.a_hat:.12g}")
    print(f"best_abs_a_hat_plus_g_m_s2 = {best.lhs:.12g}")
    print(f"best_margin_m_s2 = {best.margin:.12g}")

    if any_cert:
        print("decision = H0_REJECTED")
        print(f"certified_lower_bound_abs_g_eff_minus_g_m_s2 = {best.margin:.12g}")
        print("claim_boundary = trajectory anomaly certified under supplied measurement, force, and gravity-reference bounds; physical anti-gravity mechanism not identified")
    else:
        print("decision = H0_NOT_REJECTED")
        print("certified_lower_bound_abs_g_eff_minus_g_m_s2 = 0")
        print("claim_boundary = failure to falsify ordinary force balance; not proof of H0")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
