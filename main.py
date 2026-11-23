"""One-line entry for make.fun's "Real-Life Patch Notes: The Comedy Changelog" bounty.

A software patch note for a bug in human hearing, in the terse register
of a real release note: the left ear buffers speech and replays it late,
but only during arguments. The comedy is the specificity — a version tag,
a concrete 3-second delay, and a bug that only triggers when it matters
most, filed like a routine audio driver fix.
"""

import os
import sys

# The entry: one line, at most 160 characters.
# Angle: hearing/audio — a buffering bug in the left ear. One clause, one
# bug, one number: no padding, every word works for the punchline.
TEXT = (
    "v2.4.1: fixed a bug where the left ear buffered speech and "
    "replayed it 3 seconds late during arguments."
)


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if not (1 <= len(TEXT) <= 160):
        print(f"gate failed: entry is {len(TEXT)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(TEXT)} characters -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
