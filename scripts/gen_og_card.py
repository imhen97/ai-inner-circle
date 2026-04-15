#!/usr/bin/env python3
"""Generate 1200x630 Open Graph preview image (Kakao, etc.)."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
GOLD = (212, 175, 55)
GOLD_DIM = (160, 140, 90)
FG = (245, 243, 238)
MUTED = (160, 155, 145)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "og-card.png"


def load_font(size: int, bold: bool = False):
    paths = [
        "/System/Library/Fonts/AppleSDGothicNeo.ttc",
        "/System/Library/Fonts/Supplemental/AppleGothic.ttf",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size, index=1 if bold and p.endswith(".ttc") else 0)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    img = Image.new("RGB", (W, H), (10, 10, 15))
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        r = int(10 + (22 - 10) * t)
        g = int(10 + (18 - 10) * t)
        b = int(15 + (28 - 15) * t)
        for x in range(W):
            px[x, y] = (r, g, b)

    d = ImageDraw.Draw(img)
    margin = 48
    d.rectangle(
        [margin, margin, W - margin, H - margin],
        outline=GOLD_DIM,
        width=2,
    )
    inset = margin + 24
    d.line([(inset, inset + 80), (inset + 120, inset + 80)], fill=GOLD, width=3)
    d.line([(W - inset - 120, H - inset - 80), (W - inset, H - inset - 80)], fill=GOLD, width=3)

    font_en = load_font(26)
    font_title = load_font(56, bold=True)
    font_sub = load_font(30)
    font_line = load_font(28)
    font_small = load_font(22)

    cx = W // 2
    y0 = 120

    en = "THE AI INNER CIRCLE"
    tw = d.textlength(en, font=font_en)
    d.text((cx - tw / 2, y0), en, font=font_en, fill=GOLD)

    title = "1\uae30 \uc120\ubc1c \ucd08\ub300\uc7a5"
    tw = d.textlength(title, font=font_title)
    d.text((cx - tw / 2, y0 + 52), title, font=font_title, fill=FG)

    sub = (
        "2029 \uc804\uc7c1 \uc804, \uc548\uc804 \uc790\uc0b0\uc744 "
        "\ub9cc\ub4dc\ub294 \uc18c\uc218\uc758 \ubc29"
    )
    tw = d.textlength(sub, font=font_sub)
    d.text((cx - tw / 2, y0 + 140), sub, font=font_sub, fill=MUTED)

    line = (
        "\ucf54\ub529 \uc5c6\uc774 \u00b7 4\uc8fc \u00b7 10\uc778 "
        "\ud55c\uc815 \u00b7 \ube44\uacf5\uac1c \ud569\ub958"
    )
    tw = d.textlength(line, font=font_line)
    d.text((cx - tw / 2, y0 + 210), line, font=font_line, fill=FG)

    foot = "imhen97.github.io/ai-inner-circle"
    tw = d.textlength(foot, font=font_small)
    d.text((cx - tw / 2, H - 100), foot, font=font_small, fill=GOLD_DIM)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
