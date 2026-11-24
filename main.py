#!/usr/bin/env python3
"""Writes one original office joke to /output/entry.txt."""

import os

JOKE = "I told my boss the meeting could've been an email — he hit reply-all: 'Great idea! Let's meet to discuss it.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
