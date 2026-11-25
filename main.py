"""One Line, Big Laugh — write a single funny line to /output/entry.txt.

The joke is a short misdirection: the setup promises a helpful AI, the
punchline hands the AI a better love life than its owner.
"""

import os


JOKE = "My AI wrote my wedding vows, then proposed to my fiancee."


def main() -> None:
    # Gate mirror: the entry must be 1-200 characters, not only whitespace.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("joke fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: every byte counts toward the size tie-break.
    data = JOKE.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
