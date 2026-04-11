#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
cases = json.loads((ROOT / "artifacts/spec/shadow_reuse_cases.json").read_text())
fmt = sys.argv[1] if len(sys.argv) > 1 else "md"

def render_md(data):
    lines = ["# Shadow Reuse Cases", "", "## Canonical cases", ""]
    for row in data:
        lines.append(f"### {row['module']}")
        lines.append(f"- status: {row['status']}")
        lines.append(f"- native_object: {row['native_object']}")
        if row["ceiling_symbol"]:
            lines.append(f"- ceiling_symbol: {row['ceiling_symbol']}")
        if row["quantity_symbol"]:
            lines.append(f"- quantity_symbol: {row['quantity_symbol']}")
        if row["dual_object"]:
            lines.append(f"- dual_object: {row['dual_object']}")
        lines.append(f"- first_use_definition_required: {str(row['first_use_definition_required']).lower()}")
        lines.append("")
    return "\n".join(lines)

def render_txt(data):
    lines = ["Shadow Reuse Cases", ""]
    for row in data:
        lines.append(f"{row['module']} | {row['status']} | {row['native_object']}")
        if row["dual_object"]:
            lines.append(f"dual_object={row['dual_object']}")
        if row["ceiling_symbol"]:
            lines.append(f"ceiling_symbol={row['ceiling_symbol']}")
        if row["quantity_symbol"]:
            lines.append(f"quantity_symbol={row['quantity_symbol']}")
        lines.append("")
    return "\n".join(lines)

def esc(s: str) -> str:
    return s.replace("_", r"\_")

def render_tex(data):
    lines = [
        r"\section*{Shadow Reuse Cases}",
        r"\begin{itemize}"
    ]
    for row in data:
        pieces = [
            esc(row["module"]),
            esc(row["status"]),
            esc(row["native_object"])
        ]
        if row["dual_object"]:
            pieces.append("dual=" + esc(row["dual_object"]))
        if row["ceiling_symbol"]:
            pieces.append("L=" + esc(row["ceiling_symbol"]))
        if row["quantity_symbol"]:
            pieces.append("q=" + esc(row["quantity_symbol"]))
        lines.append(r"\item " + " ; ".join(pieces))
    lines.append(r"\end{itemize}")
    return "\n".join(lines)

renderers = {
    "md": render_md,
    "txt": render_txt,
    "tex": render_tex,
}

if fmt not in renderers:
    raise SystemExit(f"unsupported format: {fmt}")

out_dir = ROOT / "artifacts/generated"
out_dir.mkdir(parents=True, exist_ok=True)
suffix = {"md": ".md", "txt": ".txt", "tex": ".tex"}[fmt]
out_path = out_dir / f"shadow_reuse_cases{suffix}"
out_path.write_text(renderers[fmt](cases) + "\n")
print(out_path)
