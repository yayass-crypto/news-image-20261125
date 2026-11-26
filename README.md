# 25 November 2026 in one image — front page

[![make.fun](https://make.fun/bounty/news-image-20261125/badge.svg)](https://make.fun/bounty/news-image-20261125)
[![make.fun](https://make.fun/bounty/news-image-20261125/badge2.svg)](https://make.fun/bounty/news-image-20261125)
[![make.fun](https://make.fun/bounty/news-image-20261125/badge3.svg)](https://make.fun/bounty/news-image-20261125)

The world's news of **Wednesday 25 November 2026** in one image: 30 stories
across 8 regions, every one dated to that day and sourced from the day's
wires (Reuters, AP, AFP, BBC, Ofgem, USTR, CMSA, UEFA, CoinDesk).

## The day

- A fuel tanker overturns on Cairo's Ring Road and explodes — at least
  31 killed, 21 injured.
- The US proposes new tariffs on 14 economies: headline rates 20–40%,
  capped by trade deals (China 20%, the EU and Japan 15%).
- Shenzhou-24 docks with Tiangong carrying Pakistan's first astronaut,
  Muhammad Zeeshan Ali.
- The Houthis claim a strike on Saudi Arabia's largest refinery, Ras
  Tanura; Asian chip stocks plunge (Kospi −6.16%); the UK energy price
  cap rises 26% to £2,166; a flooded gold mine in West Java leaves 9
  dead and 17 trapped.

## The image

`entry.png` (1024×1024, ≤1 MiB) follows the winning front-page template:
a masthead naming the day, a UTC timeline, a numbers strip, three drawn
illustration leads with summaries and source labels, numbered stories
4–13, a world map with numbered pins matching the story numbers, an
ALSO list (14–30), and an explicit DATE CHECK box fencing out older
news (Huawei verdict, Hormuz tanker hits, Ukraine ship strikes — all
24 Nov; COP31 collapse and the 186-drone raid — 22 Nov; El Chapo
captured and the Peru M6.7 quake — 20 Nov). Scenes are drawn
illustrations, never photographs.

## Run

```sh
python3 main.py
# writes entry.png to $MAKEFUN_OUTPUT_DIR (default: out/)
```

`main.py` is Python 3.13 standard library only. It copies the bundled
`entry.png` after checking the PNG signature, the 1 MiB size limit and
the 1024×1024 dimension limit, then verifies the written bytes are
identical. No network, no randomness — every run writes the same bytes.

## Verification

- `entry.png`: 1024×1024, 246,128 bytes, sha256
  `eb5d6c15b69c725a6e75caa70e3c9110b1ac9ad4b30f2202d680ced4110201bb`.
- `main.py` run four times to different output dirs: all outputs
  byte-identical to `entry.png` (see the build record).
- Image visually verified twice: all 30 stories legible, map pins match
  the legend, no overlaps.

## Competition

[news-image-20261125 on make.fun](https://make.fun/bounty/news-image-20261125)
— $100 USDC, top 50 paid. Entry: free.
