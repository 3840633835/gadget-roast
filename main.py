#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — entry program for make.fun.

Writes the one-line entry (the roast of a gadget used every day, 105
characters, under the 200-character gate) to ``<output>/entry.txt``
and prints it. Standard library only, no network, no randomness, no
clock: the same bytes come out on every run.

The grader runs this as ``python3 -P -s /bot/main.py`` and reads
``/output/entry.txt``; ``MAKEFUN_OUTPUT_DIR`` (used by the local test)
overrides the output directory, default ``/output``.
"""

import os
import sys

# The entry, byte-identical to entry.txt in this repository.
# A smartwatch roast: the watch congratulates the wearer for standing
# up, as if sitting down was the one job he had and he failed it.
# Two laughs in one line — the praise itself is the insult, and the
# second clause turns sitting into a job failed.
ENTRY = "My smartwatch congratulates me for standing up, as if sitting down was the one job I had and I failed it."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = "entry.txt"


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # The grader collects outputs as another user: leave the file
    # readable by everyone (0644), never the 0600 a temp file gets.
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
