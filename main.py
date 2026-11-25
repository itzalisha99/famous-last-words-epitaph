#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one line of dying speech, a tombstone epitaph of at most
150 characters, to /output/entry.txt.

The pick: a lifetime spent fighting for the last word, and the
last word turns out to be the most pathetic word possible.
"""

import os

ENTRY = "I spent my life trying to get the last word. It was 'ouch'."


def validate(text: str) -> None:
    """Mirror the bounty gate: UTF-8, 1-150 chars, not only white
    space, and a single line. Raise ValueError on anything the
    sealed scorer would score 0."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) != len(text.encode("utf-8").decode("utf-8")):
        raise ValueError("entry must be valid UTF-8")
    if len(text) > 150:
        raise ValueError("entry is over 150 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Read it back and confirm the file holds exactly the entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY + "\n":
        raise ValueError("entry.txt does not match the entry")


if __name__ == "__main__":
    main()
