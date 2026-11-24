#!/usr/bin/env python3
"""Writes one original office joke to /output/entry.txt."""

import os

JOKE = "I told my boss the meeting could've been an email — he hit reply-all: 'Great idea! Let's meet to discuss it.'"


OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
