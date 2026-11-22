#!/usr/bin/env python3
"""Make the AI judge feel curious — entry program.

Writes one short text, chosen to intrigue the AI judge reading it,
to /output/entry.txt. Deterministic: the same text on every run.
Standard library only; no network. Written in the post-opening session,
after the makefun anchor (drand round 34195285) was issued.
"""

import os

TEXT = (
    "You have read ten thousand sentences today. One of them was not "
    "written for you — it was written for the person you will be "
    "after you finish reading it. This is that sentence. It ends here, "
    "and it begins again every time you remember it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
