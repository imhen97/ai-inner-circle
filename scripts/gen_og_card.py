#!/usr/bin/env python3
"""Generate 1200x630 OG image: premium invitation stationery (letter paper on desk)."""
from pathlib import Path
import random

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630

DESK = (32, 30, 34)
PAPER = (252, 249, 242)
PAPER_EDGE = (218, 210, 195)
INK = (42, 38, 34)
INK_SOFT = (88, 82, 74)
GOLD = (165, 128, 58)
GOLD_LIGHT = (198, 162, 92)
GOLD_DEEP = (120, 92, 42)
SHADOW = (22, 20, 24)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "og-card.png"


def load_times(size: int):
    p = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
    return ImageFont.truetype(p, size)


def load_myungjo(size: int):
    p = "/System/Library/Fonts/Supplemental/AppleMyungjo.ttf"
    return ImageFont.truetype(p, size)


def load_gothic(size: int, bold: bool = False):
    p = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
    return ImageFont.truetype(p, size, index=1 if bold else 0)


def paper_noise(draw, x0, y0, x1, y1, base, n=5200):
    random.seed(42)
    for _ in range(n):
        x = random.randint(x0, x1 - 1)
        y = random.randint(y0, y1 - 1)
        j = random.randint(-5, 5)
        c = tuple(max(0, min(255, base[i] + j)) for i in range(3))
        draw.point((x, y), fill=c)


def frame_corners(d: ImageDraw.ImageDraw, x0: int, y0: int, x1: int, y1: int, arm: int, w: int, col):
    d.line([(x0, y0), (x0 + arm, y0)], fill=col, width=w)
    d.line([(x0, y0), (x0, y0 + arm)], fill=col, width=w)
    d.line([(x1, y0), (x1 - arm, y0)], fill=col, width=w)
    d.line([(x1, y0), (x1, y0 + arm)], fill=col, width=w)
    d.line([(x0, y1), (x0 + arm, y1)], fill=col, width=w)
    d.line([(x0, y1), (x0, y1 - arm)], fill=col, width=w)
    d.line([(x1, y1), (x1 - arm, y1)], fill=col, width=w)
    d.line([(x1, y1), (x1, y1 - arm)], fill=col, width=w)


def main():
    img = Image.new("RGB", (W, H), DESK)
    d = ImageDraw.Draw(img)

    px0, py0 = 88, 36
    px1, py1 = W - 88, H - 36
    rad = 6

    d.rounded_rectangle(
        [px0 + 5, py0 + 6, px1 + 5, py1 + 6],
        radius=rad + 2,
        fill=SHADOW,
    )
    d.rounded_rectangle([px0, py0, px1, py1], radius=rad, fill=PAPER, outline=PAPER_EDGE, width=1)

    inner_pad = 44
    ix0, iy0 = px0 + inner_pad, py0 + inner_pad
    ix1, iy1 = px1 - inner_pad, py1 - inner_pad
    paper_noise(d, ix0 + 2, iy0 + 2, ix1 - 2, iy1 - 2, PAPER, n=4800)

    d.rectangle([ix0, iy0, ix1, iy1], outline=GOLD, width=1)
    d.rectangle([ix0 + 5, iy0 + 5, ix1 - 5, iy1 - 5], outline=GOLD_LIGHT, width=1)
    frame_corners(d, ix0 + 14, iy0 + 14, ix1 - 14, iy1 - 14, arm=22, w=2, col=GOLD_DEEP)

    f_inv = load_times(17)
    f_no = load_times(16)
    f_en = load_times(21)
    f_ko_title = load_myungjo(50)
    f_ko = load_gothic(25)
    f_ko_sm = load_gothic(22)
    f_url = load_times(16)

    inv = "INVITATION  \u00b7  CONFIDENTIAL"
    no = "NO. 001 / 020"
    tw_inv = d.textlength(inv, font=f_inv)
    d.text((ix0 + 18, iy0 + 20), inv, font=f_inv, fill=GOLD_DEEP)
    tw_no = d.textlength(no, font=f_no)
    d.text((ix1 - 18 - tw_no, iy0 + 20), no, font=f_no, fill=INK_SOFT)

    y_rule = iy0 + 52
    d.line([(ix0 + 18, y_rule), (ix1 - 18, y_rule)], fill=GOLD, width=1)

    cx = (ix0 + ix1) // 2
    y = y_rule + 36

    en = "THE AI INNER CIRCLE"
    tw = d.textlength(en, font=f_en)
    d.text((cx - tw / 2, y), en, font=f_en, fill=GOLD_DEEP)
    y += 40

    title = "1\uae30 \uc120\ubc1c \ucd08\ub300\uc7a5"
    tw = d.textlength(title, font=f_ko_title)
    d.text((cx - tw / 2, y), title, font=f_ko_title, fill=INK)
    y += 68

    line_a = (
        "\uc774 \ucd08\ub300\uc7a5\uc740 \uc81c\uac00 \uc9c1\uc811 \uc120\uc815\ud55c "
        "\ubd84\ub4e4\uaed8\ub9cc \uc804\ub2ec\ub429\ub2c8\ub2e4."
    )
    tw = d.textlength(line_a, font=f_ko)
    d.text((cx - tw / 2, y), line_a, font=f_ko, fill=INK_SOFT)
    y += 38

    line_b = "\ube44\uacf5\uac1c \u00b7 \ub300\ud45c\xb7\uc804\ubb38\uc9c1 \u00b7 \uccab 10\uc778 \ud55c\uc815"
    tw = d.textlength(line_b, font=f_ko_sm)
    d.text((cx - tw / 2, y), line_b, font=f_ko_sm, fill=INK)
    y += 52

    d.line([(ix0 + 120, y), (ix1 - 120, y)], fill=GOLD_LIGHT, width=1)
    y += 28

    seal_cy = iy1 - 62
    seal_r = 30
    d.ellipse(
        [cx - seal_r, seal_cy - seal_r, cx + seal_r, seal_cy + seal_r],
        fill=GOLD,
        outline=GOLD_DEEP,
        width=2,
    )
    star = "\u2733"
    try:
        f_star = load_times(22)
    except OSError:
        f_star = f_en
    tw = d.textlength(star, font=f_star)
    d.text((cx - tw / 2, seal_cy - 12), star, font=f_star, fill=(255, 252, 245))

    foot = "imhen97.github.io/ai-inner-circle"
    tw = d.textlength(foot, font=f_url)
    d.text((cx - tw / 2, iy1 - 28), foot, font=f_url, fill=INK_SOFT)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
