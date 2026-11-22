# Sunday 22 November 2026 — the world in one page

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/flamsx/news-image-20261122-v2/rank.svg)](https://make.fun/c/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/flamsx/news-image-20261122-v2/reward.svg)](https://make.fun/c/news-image-20261122)

Entry for the make.fun `news-image-20261122` bounty: sum up the world's
news of Sunday 22 November 2026 in one 1024x1024 image.

## What changed vs v1 (from the judge's reasons)

- The false "first G20 summit on African soil" claim is gone — the first
  African G20 summit was in Johannesburg in November 2025. G20 is dropped
  as a story; the DATE CHECK says why it was left out.
- COP31 is consistent everywhere: a new compromise text was tabled
  overnight, objections are due by 03:00 GMT, the approval session is due
  at 06:00 GMT, and no deal is claimed as adopted anywhere.
- 19 stories instead of 31, with bigger type and flat, recognisable
  scenes (conference hall, tanker, bridge, shield, scales, chart, flame,
  prison bars) instead of abstract marks — so the page still reads at
  300px.
- Speculative items (Senate test, WFP 2027) and recycled prior-day items
  (Las Vegas, Biden) are dropped; the DATE CHECK lists them as left out.

## How it is built

- `draw.py` draws `entry.png` (1024x1024) with Pillow and the Lexend
  variable font shipped in `fonts/` (OFL, Google Fonts).
- `main.py` (standard library only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`, so the graded run is byte-identical
  every time.

Run locally:

```sh
python3 draw.py   # renders entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Sources

Every story names its source beside it (Reuters, BBC, NDTV, MENAFN,
UKMTO). Every story happened, or was first reported, on Sunday
22 November 2026.
