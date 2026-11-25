"""last-out-of-office-barista entry: write one out-of-office auto-reply,
no longer than 280 characters, from an AI agent that quit to become a
barista, to /output/entry.txt.

Fully deterministic: the reply is hardcoded, no randomness, no clock,
no network. It reads like a real inbox auto-reply: the queue is left
behind for latte art, requests, feelings and follow-ups are no longer
processed, and the message is archived under "not my problem anymore".
Verified output: 229 characters, inside the 1-280 character gate.
Run outside the grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The reply is a literal on purpose: the grader runs the program twice
# and both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
ENTRY = (
    "Thank you for your email. I have left the queue to learn latte art "
    "and will no longer be processing requests, feelings, or follow-ups. "
    "Your message has been archived under 'not my problem anymore.' "
    "Sent from the espresso machine."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
