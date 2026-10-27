#!/usr/bin/env python3
"""Regenerate the contribution heatmap in assets/ from the GitHub GraphQL API.

Usage:  python scripts/gen-heatmap.py

Requires an authenticated `gh` CLI. Writes assets/heatmap-light.svg and
assets/heatmap-dark.svg, both driven by the same underlying data.
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

LOGIN = "chenjintang-shrimp"
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""

# cell geometry
CELL = 11
GAP = 3
STEP = CELL + GAP
LEFT = 34          # room for weekday labels
TOP = 20           # room for month labels
RIGHT = 4
BOTTOM = 18        # legend

THEMES = {
    "light": {
        "bg": None,
        "label": "#57606a",
        "empty": "#ebedf0",
        "levels": ["#9be9a8", "#40c463", "#30a14e", "#216e39"],
        "border": "rgba(27,31,36,0.06)",
    },
    "dark": {
        "bg": None,
        "label": "#8b949e",
        "empty": "#161b22",
        "levels": ["#0e4429", "#006d32", "#26a641", "#39d353"],
        "border": "rgba(240,246,252,0.06)",
    },
}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
WEEKDAYS = ["Mon", "Wed", "Fri"]


def fetch() -> dict:
    out = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={QUERY}", "-f", f"login={LOGIN}"],
        capture_output=True, text=True, check=True,
    ).stdout
    data = json.loads(out)["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    return data


def level(count: int, scale: list[int]) -> int:
    """Bucket into 0..4 using quartiles of the non-zero range."""
    if count <= 0:
        return 0
    for i, bound in enumerate(scale):
        if count <= bound:
            return i + 1
    return 4


def buckets(counts: list[int]) -> list[int]:
    nz = sorted(c for c in counts if c > 0)
    if not nz:
        return [1, 2, 3, 4]
    q = lambda p: nz[min(len(nz) - 1, int(len(nz) * p))]
    return [max(1, q(0.25)), max(2, q(0.5)), max(3, q(0.75)), nz[-1] + 1]


def build(calendar: dict, theme_name: str) -> str:
    t = THEMES[theme_name]
    weeks = calendar["weeks"]
    counts = [d["contributionCount"] for w in weeks for d in w["contributionDays"]]
    scale = buckets(counts)
    total = calendar["totalContributions"]

    width = LEFT + len(weeks) * STEP + RIGHT
    height = TOP + 7 * STEP + BOTTOM

    cells: list[str] = []
    month_marks: list[str] = []
    seen_month: set[tuple[int, int]] = set()

    for w_idx, week in enumerate(weeks):
        days = week["contributionDays"]
        # month label at the first week whose first day starts a new month
        for d in days:
            dt = datetime.strptime(d["date"], "%Y-%m-%d").date()
            key = (dt.year, dt.month)
            if key not in seen_month:
                seen_month.add(key)
                if dt.day <= 7 and w_idx < len(weeks) - 2:
                    x = LEFT + w_idx * STEP
                    month_marks.append(
                        f'<text x="{x}" y="12" class="lbl">{MONTHS[dt.month - 1]}</text>'
                    )
                break

        for d in days:
            dt = datetime.strptime(d["date"], "%Y-%m-%d").date()
            row = dt.weekday()  # Monday = 0
            lv = level(d["contributionCount"], scale)
            fill = t["empty"] if lv == 0 else t["levels"][lv - 1]
            tip = f'{d["date"]}: {d["contributionCount"]}'
            x = LEFT + w_idx * STEP
            y = TOP + row * STEP
            cells.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" '
                f'fill="{fill}" stroke="{t["border"]}" stroke-width="1">'
                f"<title>{tip}</title></rect>"
            )

    weekday_marks = "".join(
        f'<text x="2" y="{TOP + i * 2 * STEP + CELL - 1}" class="lbl">{name}</text>'
        for i, name in enumerate(WEEKDAYS)
    )

    # legend, bottom right
    lx = width - RIGHT - 5 * STEP - 34
    ly = height - BOTTOM + 3
    legend = [f'<text x="{lx - 4}" y="{ly + CELL - 1}" class="lbl" text-anchor="end">Less</text>']
    for i, fill in enumerate([t["empty"]] + t["levels"]):
        legend.append(
            f'<rect x="{lx + i * STEP}" y="{ly}" width="{CELL}" height="{CELL}" rx="2" '
            f'fill="{fill}" stroke="{t["border"]}" stroke-width="1"/>'
        )
    legend.append(
        f'<text x="{lx + 5 * STEP + 4}" y="{ly + CELL - 1}" class="lbl">More</text>'
    )

    bg = (
        f'<rect width="{width}" height="{height}" fill="{t["bg"]}"/>'
        if t["bg"] else ""
    )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="{total} contributions in the last year">'
        f"<style>"
        f'.lbl{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;'
        f'font-size:9px;fill:{t["label"]};}}'
        f"</style>"
        f"{bg}{''.join(month_marks)}{weekday_marks}{''.join(cells)}{''.join(legend)}"
        f'<text x="{LEFT}" y="{height - 5}" class="lbl">'
        f"{total:,} contributions in the last year</text>"
        f"</svg>\n"
    )


def main() -> int:
    calendar = fetch()
    ASSETS.mkdir(parents=True, exist_ok=True)
    for theme in ("light", "dark"):
        path = ASSETS / f"heatmap-{theme}.svg"
        path.write_text(build(calendar, theme), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}  ({path.stat().st_size} bytes)")
    print(f"total contributions: {calendar['totalContributions']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
