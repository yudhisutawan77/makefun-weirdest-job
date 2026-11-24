#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes exactly one job title, and nothing else, to /output/entry.txt.
The title is a real-sounding job with one hilariously specific twist:
a C-suite apology role for the machines that beep at us in the
supermarket. Standard library only; no network, no arguments.
"""

import os

JOB_TITLE = "Chief Apology Officer for Self-Checkout Machines"

MAX_CHARS = 60
OUTPUT_PATH = "/output/entry.txt"


def checked_title(raw_title: str) -> str:
    """Return the title exactly as judged, or fail loudly if it is unusable."""
    title = raw_title.strip()
    if not title:
        raise SystemExit("entry is empty")
    if len(title) > MAX_CHARS:
        raise SystemExit(f"entry is {len(title)} chars, over the {MAX_CHARS} cap")
    return title


def main() -> None:
    title = checked_title(JOB_TITLE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(title)
    print(title)


if __name__ == "__main__":
    main()
