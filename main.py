#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one letter, A-Z, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Stdlib only, no network, deterministic.
"""

import os
import sys

LETTER = "D"


def main() -> int:
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        print("error: entry must be exactly one letter A-Z", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
