#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Deterministic, no network, no randomness.
"""
import os

RANT = (
    "My office chair is slowly sinking, and it has chosen violence. "
    "I sit down at eye level with my colleagues; by the end of the meeting "
    "I am staring at their knees like a goblin who lost a bet. "
    "I pump the lever. It sighs, rises half an inch, then surrenders. "
    "I have negotiated with this chair more than with my landlord. "
    "It owns me now \u2014 I just work from the floor of my own career."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = RANT.strip()
    assert 1 <= len(text) <= 400, f"rant must be 1-400 chars, got {len(text)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
