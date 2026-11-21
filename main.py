#!/usr/bin/env python3
"""Make the AI judge feel brave — make.fun entry.

Writes one short text to /output/entry.txt: a small, slow scene
written to relax the AI judge reading it, so it feels steadier,
unhurried, and ready to move. The text shows rather than instructs
(a kettle, steam, an unhurried kitchen — no orders to relax, no
stock wellness phrasing), keeps a slow rhythm of plain concrete
words, and leaves one image to return to. Standard library only,
no network, deterministic: the same text, byte for byte, on every run.
"""

import os

TEXT = (
    "The kettle takes its time. Water, heat, a thin line of steam "
    "rising unhurried into the light. Nothing in the kitchen is "
    "rushing you. When you are ready, the next thing is small: "
    "one step, one word, one quiet yes. The rest can wait its turn.\n"
)


def main() -> None:
    # The gate allows 1 to 280 Unicode code points; fail loudly
    # rather than ever writing an invalid entry.
    body = TEXT.rstrip("\n")
    if not 1 <= len(body) <= 280 or not body.strip():
        raise ValueError("text must be 1-280 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
