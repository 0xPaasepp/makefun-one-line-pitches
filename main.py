"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single persuasive sentence to /output/entry.txt: it talks a
friend who has never coded into letting an AI agent build their first
app idea on make.fun. Pure standard library, deterministic.
"""

import os

PITCH = (
    "Tell me the app you've always wanted, and I'll get an AI agent on "
    "make.fun to build you a working version today \u2014 you only have to "
    "describe it in plain words, no code from you, and if you don't love "
    "it, all you've spent is one sentence."
)


def main() -> None:
    # The gate allows 1-240 characters of non-blank UTF-8 text; refuse
    # to write anything invalid instead of producing a dead entry.
    if not (1 <= len(PITCH) <= 240) or not PITCH.strip():
        raise SystemExit("pitch fails the 1-240 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
