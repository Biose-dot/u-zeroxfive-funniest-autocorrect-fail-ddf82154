"""Funniest Autocorrect Fail — a single line, under 200 characters.

The joke: one letter turns donuts into demons, and now the demons are
catering the HR meeting — the typo escalates into a whole event.
"""

import os

ENTRY = "Texted my boss 'I'll bring the donuts' \u2014 autocorrect sent 'I'll bring the demons.' HR meeting is Thursday; demons are catering."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
