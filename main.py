#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse -- make.fun entry.

Writes a single line (under 200 characters) in which a dog explains
why the homework got eaten, to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only.
"""

import os

EXCUSE = "The homework looked at me first. In dog law, that's consent."

# The gate allows 1-200 characters; keep the excuse inside it.
assert 1 <= len(EXCUSE) <= 200


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
