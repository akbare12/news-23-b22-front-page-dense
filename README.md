# THE WORLD TODAY — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b22-front-page-dense/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b22-front-page-dense/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One image summing up the world news of **Monday 23 November 2026** — 31 stories
across 6 regions, drawn as a front page.

## The day in one line

- **AI rout hits Asia** — Kospi -3.3% to 4,708.54, sheds 161 pts; intraday -5.8%.
  Samsung -3.1%, SK Hynix -2.5%.
- **Guterres: regulate AI before it's too late** — Bridgetown summit, Barbados;
  150 delegates back a risk framework (a blueprint, not a treaty).
- **US lead over China at record low** — Asia Power Index 2026: US 78.9, China 73.6,
  gap 5.3, narrowest since 2018. India third at 40.5.

## What's inside

- Number strip: -3.3% Kospi · 5.3 power gap · 11,762 Ebola cases (DRC) ·
  10T-won Seoul fund · 2% billionaire tax · $450M Skubal deal · 165 missiles/week ·
  12,000 cleared in Manchester · 264 kg seized in Lebanon · $107.3B Anthropic IPO.
- 3 hero scenes (drawn illustrations, not photographs), 10 story cards,
  a world map with numbered pins, an ALSO list, and a DATE CHECK box that
  keeps stories from other days out of the picture.

## How it is built

`draw.py` (Pillow) renders `entry.png` (1024x1024, under 1 MiB).
`main.py` is stdlib-only: it checks the PNG header by hand and copies the
image to `$MAKEFUN_OUTPUT_DIR/entry.png`.

```sh
python3 draw.py
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Sources

Reuters · AP · Bloomberg · AFP · Yonhap · BBC · WSJ · NYT · ESPN ·
Lowy Institute (Asia Power Index 2026).

CHIPS: REPORTED = confirmed by wires · CLAIM = one side's claim, not
independently confirmed · ONGOING = still developing.
