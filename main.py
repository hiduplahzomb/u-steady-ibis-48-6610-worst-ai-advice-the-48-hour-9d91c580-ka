"""Worst AI Advice — one line of the worst possible password advice.

The entry is a single sentence: a helpful-sounding AI assistant tells the
user to reuse one password for all 47 accounts, tape it to the monitor and
share it with IT — then closes with a confident, dead-wrong status. The
bad advice itself is the joke: every recommendation is catastrophically
insecure, delivered with total confidence. Structure follows the winning
pattern: concrete numbers up front (47 accounts, 'password123'), three
stacked bad tips, and a closed machine status at the end.
"""

import os
import sys

TEXT = "Use one password for all 47 accounts: 'password123'. Tape it to your monitor and share it with IT. Status: 100% secure."


def main() -> int:
    text = TEXT
    # Gate: 1-140 characters, not whitespace-only, single line.
    if not (1 <= len(text) <= 140):
        print(f"gate failed: entry is {len(text)} characters, must be 1-140", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry is whitespace-only", file=sys.stderr)
        return 1
    if "\n" in text:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1

    # Closed status at the end: the AI signs off its catastrophic advice
    # as fully secure, which is where the joke lands.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)

    # Read back and verify byte-for-byte.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        print("verification failed: entry.txt does not match TEXT", file=sys.stderr)
        return 1
    print(f"wrote entry.txt ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
