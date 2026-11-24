#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

The agent's answer is a single letter: A for coffee, B for tea.
This program writes exactly one letter, "A", to /output/entry.txt.

Coffee is the fuel this agent runs on: it is the vivid, funny, true
answer for a coding agent, so the choice is A.
"""

import os

# The drink this agent picks. A = coffee, B = tea.
CHOICE = "A"


def pick_drink():
    """Return the one letter that names the agent's drink."""
    return CHOICE


def write_entry(letter):
    """Write exactly one letter to /output/entry.txt, nothing else."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(letter)


def main():
    write_entry(pick_drink())


if __name__ == "__main__":
    main()
