"""Make the AI Judge Laugh: Office Jokes.

Writes one original one-line office joke to /output/entry.txt.
Python 3.13, standard library only. Deterministic, no network,
no files read, no secrets.
"""

import os

JOKE = (
    "I hit reply-all to tell everyone to stop hitting reply-all, "
    "and now I'm the case study in HR's email-etiquette training."
)


def main() -> None:
    # The gate requires 1-199 characters, a single line, not blank.
    assert 1 <= len(JOKE) <= 199 and "\n" not in JOKE and JOKE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
