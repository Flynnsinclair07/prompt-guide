#!/usr/bin/env python3
"""Generate a 500x500 SnipPrompts logo for Product Hunt / directories."""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

SIZE = 500
CREAM = "#F5EBDD"
NAVY = "#1B2A4E"
FONT_BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"


def fit_font(text, max_width, start=150, min_size=40):
    for size in range(start, min_size - 1, -2):
        font = ImageFont.truetype(FONT_BLACK, size)
        d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
        if d.textlength(text, font=font) <= max_width:
            return font, size
    return ImageFont.truetype(FONT_BLACK, min_size), min_size


def make_logo():
    img = Image.new("RGB", (SIZE, SIZE), NAVY)
    draw = ImageDraw.Draw(img)

    max_w = 400  # leave ~50px padding each side
    lines = ["Snip", "Prompts"]
    font, fsize = fit_font("Prompts", max_w)  # size to the wider word
    line_h = int(fsize * 1.02)
    block_h = line_h * len(lines)

    # Accent bar height + generous gap so it clears the 'p' descenders
    bar_h, bar_gap = 8, 70
    descender_pad = 24
    total_h = block_h + descender_pad + bar_gap + bar_h
    y = (SIZE - total_h) // 2

    for line in lines:
        tw = draw.textlength(line, font=font)
        draw.text(((SIZE - tw) // 2, y), line, font=font, fill=CREAM)
        y += line_h

    # Cream accent bar under the wordmark (brand element from the pins)
    y += descender_pad + bar_gap
    bar_w = 140
    draw.rectangle(
        [(SIZE - bar_w) // 2, y, (SIZE + bar_w) // 2, y + bar_h],
        fill=CREAM,
    )

    out = Path(__file__).parent / "snipprompts-logo.png"
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out}  (wordmark {fsize}px)")


if __name__ == "__main__":
    make_logo()
