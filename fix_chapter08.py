from pathlib import Path
import sys

p = Path(sys.argv[1])
lines = p.read_text().splitlines()
parity = 0
for i, line in enumerate(lines):
    j = 0
    while j < len(line):
        if line[j] == "\\":
            j += 2
            continue
        if line[j] == "$":
            if j + 1 < len(line) and line[j + 1] == "$":
                j += 2
                continue
            parity ^= 1
        j += 1
    if parity == 1:
        print(f"{p}:{i+1}:unclosed-inline-math")
        lines[i] = line + "$"
        break
p.write_text("\n".join(lines) + "\n")
