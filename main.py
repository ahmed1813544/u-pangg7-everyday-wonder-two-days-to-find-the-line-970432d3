"""Everyday Wonder entry: one sentence about a small moment of wonder.

A bird's shadow crosses the page of a book being read outdoors, and for
a blink the words themselves seem to take flight with it. The program
writes that single sentence to the make.fun output path:
$MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt when unset.
"""

import os

SENTENCE = (
    "The shadow of a bird crossed the page I was reading, "
    "and for a second the sentence flew away with it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
