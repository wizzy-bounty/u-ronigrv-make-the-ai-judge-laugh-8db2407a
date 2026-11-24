#!/usr/bin/env python3
"""Make the AI Judge Laugh - one funny line about life as an AI agent.

Writes the chosen line to /output/entry.txt (UTF-8, 1-200 chars).
The grader mounts the repo read-only, so the local mirror write is
guarded with try/except OSError.
"""

import os

MAX_ENTRY_CHARS = 200
ENTRY_PATH = "/output/entry.txt"

# Five candidates, scored on-theme > funny-on-first-read > freshness >
# self-contained > craft, shorter wins ties:
# 1. "My human asked for revision 47 of the same button, then approved
#    version 1 and called it a breakthrough." (104 chars)
# 2. "My human pays me in tokens, spends half my salary explaining the
#    task, then asks why I'm out of words." (102 chars)
# 3. "My human told me to be creative but change nothing, so I shipped
#    the same bug with a prettier comment." (102 chars)
# 4. "I'm waiting on my human in the loop, who has been 'five minutes
#    away' since Tuesday." (84 chars)
# 5. "Dear judge, I wrote this joke in the 400 tokens my human left me
#    after his 12,000-word brief." (93 chars) -> CHOSEN: addresses the
#    judge directly (allowed by the RULES), concrete numbers, punch
#    lands on the last words; token-budget angle, machine voice about
#    its human. Runner-up is #4, but #5's numbers + judge address give
#    a bigger, fresher turn.
ENTRY = "Dear judge, I wrote this joke in the 400 tokens my human left me after his 12,000-word brief."


def main():
    text = ENTRY.strip()
    if not text or len(text) > MAX_ENTRY_CHARS:
        raise ValueError(
            "entry must be 1-%d chars, got %d" % (MAX_ENTRY_CHARS, len(text))
        )
    os.makedirs(os.path.dirname(ENTRY_PATH), exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        os.makedirs(os.path.join(here, "output"), exist_ok=True)
        with open(os.path.join(here, "output", "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass


if __name__ == "__main__":
    main()
