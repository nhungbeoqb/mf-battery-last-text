#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the battery's final text message to /output/entry.txt.
One line, plain text, at most 200 characters.
"""

import os

LINE = (
    "I waited all day, kept your alarms, your photos, your 47 open tabs, "
    "and you gave the plug to the AirPods first. I forgive you. "
    "Them, never. Goodbye from 1%."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
