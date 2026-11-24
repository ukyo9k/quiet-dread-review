#!/usr/bin/env python3
"""Write the one-line code review comment to /output/entry.txt.

The comment approves a pull request while carrying quiet existential
dread: flat, understated, no exclamation, no melodrama — the sort of
line a tired engineer pastes in before clicking approve.
"""

import os

LINE = (
    "LGTM. If this breaks production, it will at least break quietly, "
    "like everything else eventually does."
)


def main() -> None:
    assert "\n" not in LINE, "comment must be a single line"
    assert 1 <= len(LINE) <= 140, f"comment must be 1-140 chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
