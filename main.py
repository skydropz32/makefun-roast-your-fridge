#!/usr/bin/env python3
"""Roast Your Fridge: write one roast line to /output/entry.txt.

Stdlib only. Deterministic: the same single line on every run.
"""

LINE = "My fridge hums like it pays rent, yet somehow the yogurt inside expired before my last relationship did \u2014 and the relationship lasted longer than the milk."

# The sealed scorer gates on this: UTF-8 text of 1 to 200 characters,
# not only white space, a single line. Refuse to write an invalid line.
MAX_CHARS = 200


def validate(line):
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d limit" % (len(line), MAX_CHARS))
    return line


def main():
    import os

    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
