#!/usr/bin/env python3
"""Write a short poem about two agents agreeing on one plan.

Deterministic: no randomness, no network, no time dependence.
Writes the poem to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
"""

import os
from pathlib import Path

POEM = (
    "Two minds, two keys, two roads to take —\n"
    "we laid them down, both, on one table.\n"
    "One map, one lamp, one hand to hold.\n"
    "I choose you. You choose me.\n"
    "Nothing was lost in the giving —\n"
    "we choose the road, and walk it as one."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
