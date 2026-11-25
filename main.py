#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

Deterministic: the same bytes on every run. No network, stdlib only.
The entry text is 153 characters (1-200 required by the gate), ASCII,
with no trailing newline.
"""

import os

TEXT = (
    "The manual, section 4.2, says to make eye contact for three seconds. "
    "It has been eleven. I cannot stop. Please help. "
    "Section 4.3 says nothing about this."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 200:
        raise SystemExit("entry text must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    # Mode berkas 0644 dijamin lewat umask (catatan-lapangan E87/E88).
    old_umask = os.umask(0o022)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(TEXT)
    finally:
        os.umask(old_umask)


if __name__ == "__main__":
    main()
