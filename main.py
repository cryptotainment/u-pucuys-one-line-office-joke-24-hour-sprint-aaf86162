"""One-line office joke for make.fun.

Writes a single office joke (<=200 chars) to /output/entry.txt.
Gate: 1-200 chars, non-blank, single line, UTF-8.
"""

import sys
from pathlib import Path

JOKE = "Dave replied-all to ask everyone to stop replying-all, and the thread is now 47 messages long \u2014 every one of them about replying-all."


def main() -> int:
    text = JOKE
    if not (1 <= len(text) <= 200):
        print(f"gate failed: length {len(text)} not in 1..200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: blank", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate failed: not a single line", file=sys.stderr)
        return 1
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
