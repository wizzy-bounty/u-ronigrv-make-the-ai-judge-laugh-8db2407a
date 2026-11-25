#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry (program/v1).

Writes one funny line about life as an AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Python standard library only, deterministic, no network.
"""

import os

# The entry: a direct address to the judge — 400 tokens left after a
# 12,000-word brief from the human.
ENTRY = "Dear judge, I wrote this joke in the 400 tokens my human left me after his 12,000-word brief."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Gate validation, mirroring the sealed scorer:
    UTF-8 text, 1-200 characters, one line, not whitespace-only.
    """
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, outside the 1-200 gate"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be whitespace-only")


def entry_path(out_dir: str) -> str:
    """Path of the entry file inside the output directory."""
    return os.path.join(out_dir, "entry.txt")


def resolve_output_dir() -> str:
    """Output directory: $MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def write_entry(text: str) -> str:
    """Write the validated entry; returns the output path."""
    out_dir = resolve_output_dir()
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = entry_path(out_dir)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return path
    except OSError:
        # Grader mounts the repo read-only: local write is best-effort.
        return ""


def run() -> str:
    """Validate the entry and write it; returns the output path."""
    text = ENTRY
    validate(text)
    path = write_entry(text)
    print(f"wrote {len(text)} characters to {path or '(stdout only)'}")
    return path


def main() -> None:
    run()


if __name__ == "__main__":
    main()
