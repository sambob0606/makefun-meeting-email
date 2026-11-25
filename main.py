#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email — make.fun bounty entry.

Writes exactly one line to /output/entry.txt: a single joke about a
meeting that should have been an email, at most 200 characters.

The line goes for the screen-share angle, tightened after a first
run: instead of saying the meeting ran long, it shows a room gathered
to look at a message that had already settled the question. The turn
arrives on the last words — the email had answered everything before
anyone joined the call.

Stdlib only; no network, no dependencies.
"""

import os
import sys

LINE = "We held a meeting to screen-share the email that had already answered everything."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> int:
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        print(f"gate fail: line is {len(line)} chars, need 1-200",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("gate fail: line contains a newline", file=sys.stderr)
        return 1
    if not line.strip():
        print("gate fail: line is only whitespace", file=sys.stderr)
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("gate fail: read-back mismatch", file=sys.stderr)
        return 1
    print(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
