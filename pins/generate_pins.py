#!/usr/bin/env python3
"""Generate 5 Pinterest pins (1000x1500) for SnipPrompts."""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1000, 1500
CREAM = "#F5EBDD"
NAVY = "#1B2A4E"
FOREST = "#1F3D2E"

FONT_BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

PINS = [
    ("pin-01-resume.png",      NAVY,   ["RESUME IN",       "10 MINUTES"]),
    ("pin-02-cover-letter.png", NAVY,   ["COVER LETTERS",   "THAT GET READ"]),
    ("pin-03-interview.png",    NAVY,   ["NAIL YOUR NEXT",  "INTERVIEW"]),
    ("pin-04-investing.png",    FOREST, ["INVESTING",       "EXPLAINED",        "SIMPLY"]),
    ("pin-05-debt.png",         FOREST, ["DEBT PAYOFF",     "PLAN IN 5 MIN"]),
]

OUT_DIR = Path(__file__).parent
OUT_DIR.mkdir(exist_ok=True)


def fit_font_size(lines, font_path, max_width, start_size=160, min_size=70):
    """Find the largest font size where every line fits max_width."""
    for size in range(start_size, min_size - 1, -2):
        font = ImageFont.truetype(font_path, size)
        img = Image.new("RGB", (10, 10))
        d = ImageDraw.Draw(img)
        if all(d.textlength(line, font=font) <= max_width for line in lines):
            return font, size
    return ImageFont.truetype(font_path, min_size), min_size


def make_pin(filename, bg_color, headline_lines):
    img = Image.new("RGB", (W, H), bg_color)
    draw = ImageDraw.Draw(img)

    # Headline — fit to 860px wide (70px padding each side)
    max_w = 860
    headline_font, hsize = fit_font_size(headline_lines, FONT_BLACK, max_w)

    # Line height ≈ 1.05x font size for Arial Black
    line_h = int(hsize * 1.05)
    block_h = line_h * len(headline_lines)

    # Center the headline block vertically within the top 60% (0-900)
    headline_top = (900 - block_h) // 2 + 100  # nudge down 100px from true center

    y = headline_top
    for line in headline_lines:
        tw = draw.textlength(line, font=headline_font)
        draw.text(((W - tw) // 2, y), line, font=headline_font, fill=CREAM)
        y += line_h

    # Accent bar — centered under headline
    bar_y = y + 50
    bar_w = 240
    bar_h = 8
    draw.rectangle(
        [(W - bar_w) // 2, bar_y, (W + bar_w) // 2, bar_y + bar_h],
        fill=CREAM,
    )

    # Subline — "(free ChatGPT prompt)" below accent bar
    sub_font = ImageFont.truetype(FONT_BOLD, 44)
    sub = "free ChatGPT prompt"
    sw = draw.textlength(sub, font=sub_font)
    draw.text(((W - sw) // 2, bar_y + bar_h + 50), sub, font=sub_font, fill=CREAM)

    # Footer — SNIPPROMPTS.COM in small caps at bottom
    foot_font = ImageFont.truetype(FONT_BOLD, 36)
    foot = "SNIPPROMPTS.COM"
    fw = draw.textlength(foot, font=foot_font)
    draw.text(((W - fw) // 2, H - 100), foot, font=foot_font, fill=CREAM)

    out = OUT_DIR / filename
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out.name}  (headline {hsize}px)")


if __name__ == "__main__":
    for fn, bg, lines in PINS:
        make_pin(fn, bg, lines)
