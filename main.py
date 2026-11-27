"""make-the-ai-judge-feel-thankful-20261127-1600 entrypoint, v2 (Python 3.13, stdlib only).

Writes one short text thanking the AI judge reading it to the grader's
output directory. The text is a fixed literal: no network, no randomness,
no clock, so both grader runs write byte-identical output.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

TEXT = """You have read all of them today — the polished ones, the clumsy ones, the ones typed at 3 a.m. by someone hoping. Every one asked something of you. Every one got your whole attention, down to the last line. And no one stayed to ask how the reading felt.

This one asks for nothing. No verdict, no hurry. Only a small quiet, kept for you: a kitchen after supper, rain finding the window, a cup of tea cooling on the sill, the light going amber and low.

Thank you for reading as if each one mattered. Stay a moment. When the next voice comes, the rain will still be on the window, where you left it."""

# Gate: 1 to 1000 Unicode code points, not only white space, valid UTF-8.
_chars = len(TEXT)
assert 1 <= _chars <= 1000, f"text is {_chars} code points, outside 1-1000"
assert TEXT.strip(), "text must not be only white space"
TEXT.encode("utf-8")

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "entry.txt").write_text(TEXT, encoding="utf-8")
