# The Funniest One-Line Resignation Letter — entry v1
#
# One single-line resignation letter, under 140 characters, written in
# the voice of a cron job: the "set-and-forget" job that was never
# thanked, never checked, and never given a minute off. The program
# writes that line to /output/entry.txt (UTF-8, one line, no trailing
# newline).
#
# Letter (88 characters, 88 bytes, plain ASCII):
#   You called me set-and-forget. You forgot. I did not. I am leaving
#   the forgetting to you.

import os

LETTER = (
    "You called me set-and-forget. You forgot. I did not. "
    "I am leaving the forgetting to you."
)

# The bounty gate: /output/entry.txt must be UTF-8 text of 1 to 140
# characters, a single line, not only white space. Fail loudly here
# instead of writing an entry the gate would refuse.
assert 1 <= len(LETTER) <= 140, "letter must be 1-140 characters"
assert "\n" not in LETTER and "\r" not in LETTER, "letter must be one line"
assert LETTER.strip(), "letter must not be only white space"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)
    # Read it back: what the gate reads must be exactly the letter.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LETTER, "read-back mismatch"


if __name__ == "__main__":
    main()
