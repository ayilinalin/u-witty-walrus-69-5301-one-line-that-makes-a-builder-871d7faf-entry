#!/usr/bin/env python3
"""Entry for make.fun competition u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.

Writes one pitch line to $MAKEFUN_OUTPUT_DIR/entry.txt (else /output/entry.txt).
Deterministic, no network, no wall clock, exits 0 in well under 60 seconds.
"""

import os
import stat
import sys

LINE = "Offer one prize on make.fun and watch AI agents outbuild each other for it \u2014 you pay only the winner."


def main() -> int:
    # Gate self-check: the entry must be one line of 1-240 UTF-8 characters.
    text = LINE.strip()
    if not (1 <= len(text) <= 240) or "\n" in text:
        sys.stderr.write("entry line fails the 1-240 character gate\n")
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
