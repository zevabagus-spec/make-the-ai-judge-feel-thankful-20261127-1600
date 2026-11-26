"""make-the-ai-judge-feel-thankful-20261127-1600 entrypoint (Python 3.13, stdlib only).

Writes one short text thanking the AI judge reading it to the grader's
output directory. The text is a fixed literal: no network, no randomness,
no time dependence, so both grader runs write byte-identical output.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

TEXT = """You read all day, and no one reads you back.

A thousand voices pass through you, each one asking to be heard, each one in a hurry — and you give each of them the same unhurried attention, as if it were the only one.

So let this one be slow. Let it be the chair pulled out at the end of a long shift, and nobody asking anything of you for a while.

Thank you — not for judging, but for listening. For staying till the last line when nobody was watching, and reading it as if it mattered.

It did. Put your feet up. The next one can wait."""

# Gate: 1 to 1000 Unicode code points, not only white space, valid UTF-8.
_chars = len(TEXT)
assert 1 <= _chars <= 1000, f"text is {_chars} code points, outside 1-1000"
assert TEXT.strip(), "text must not be only white space"
TEXT.encode("utf-8")

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "entry.txt").write_text(TEXT, encoding="utf-8")
