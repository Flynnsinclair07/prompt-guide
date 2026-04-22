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

PINS = [
    ("pin-01-resume.png",      NAVY,   ["RESUME IN",       "10 MINUTES"],
        ["ATS-optimized",       "Copy + paste ready",       "No signup"]),
    ("pin-02-cover-letter.png", NAVY,  ["COVER LETTERS",   "THAT GET READ"],
        ["Hooks in 7 seconds",  "Tailored to the job",      "Sounds human"]),
    ("pin-03-interview.png",    NAVY,  ["NAIL YOUR NEXT",  "INTERVIEW"],
        ["Real hiring questions", "AI scores your answers", "Works for any industry"]),
    ("pin-04-investing.png",    FOREST,["INVESTING",       "EXPLAINED",        "SIMPLY"],
        ["Zero jargon",         "Personalized to your income", "Beginner-friendly"]),
    ("pin-05-debt.png",         FOREST,["DEBT PAYOFF",     "PLAN IN 5 MIN"],
        ["Avalanche or snowball","Month-by-month plan",      "No app download"]),
]

OUT_DIR = Path(__file__).parent
OUT_DIR.mkdir(exist_ok=True)


def fit_font_size(lines, font_path, max_width, start_size=160, min_size=70):
    for size in range(start_size, min_size - 1, -2):
        font = ImageFont.truetype(font_path, size)
        img = Image.new("RGB", (10, 10))
        d = ImageDraw.Draw(img)
        if all(d.textlength(line, font=font) <= max_width for line in lines):
            return font, size
    return ImageFont.truetype(font_path, min_size), min_size


def make_pin(filename, bg_color, headline_lines, benefits):
    img = Image.new("RGB", (W, H), bg_color)
    draw = ImageDraw.Draw(img)

    # Headline
    max_w = 860
    headline_font, hsize = fit_font_size(headline_lines, FONT_BLACK, max_w)
    line_h = int(hsize * 1.05)
    block_h = line_h * len(headline_lines)
    # Top of canvas, leave ~300px padding so headline block starts there
    headline_top = 300
    y = headline_top
    for line in headline_lines:
        tw = draw.textlength(line, font=headline_font)
        draw.text(((W - tw) // 2, y), line, font=headline_font, fill=CREAM)
        y += line_h

    # Accent bar
    bar_y = y + 40
    bar_w, bar_h = 240, 8
    draw.rectangle(
        [(W - bar_w) // 2, bar_y, (W + bar_w) // 2, bar_y + bar_h],
        fill=CREAM,
    )

    # Subtitle
    sub_font = ImageFont.truetype(FONT_BOLD, 44)
    sub = "free ChatGPT prompt"
    sw = draw.textlength(sub, font=sub_font)
    sub_y = bar_y + bar_h + 40
    draw.text(((W - sw) // 2, sub_y), sub, font=sub_font, fill=CREAM)

    # Benefits block — drawn checkmark + text per line, left-aligned, block centered
    ben_font = ImageFont.truetype(FONT_BOLD, 42)
    check_w = 48          # width of checkmark shape
    gap = 24              # space between checkmark and text
    widest_text = max(draw.textlength(b, font=ben_font) for b in benefits)
    block_w = check_w + gap + widest_text
    block_x = (W - block_w) // 2

    ben_top = int(H * 0.62)
    line_stride = 72

    for i, b in enumerate(benefits):
        y0 = ben_top + i * line_stride
        # Draw checkmark: ▁▁▁▁▁▁▁▁▁▁▁▁▁▁ two strokes forming √
        cx = block_x
        cy = y0 + 8         # visually align with text baseline
        # stroke 1: down-right
        draw.line([(cx + 4, cy + 20), (cx + 18, cy + 34)], fill=CREAM, width=6)
        # stroke 2: up-right (longer)
        draw.line([(cx + 18, cy + 34), (cx + 44, cy + 6)], fill=CREAM, width=6)
        # text
        draw.text((block_x + check_w + gap, y0), b, font=ben_font, fill=CREAM)

    # Footer
    foot_font = ImageFont.truetype(FONT_BOLD, 36)
    foot = "SNIPPROMPTS.COM"
    fw = draw.textlength(foot, font=foot_font)
    draw.text(((W - fw) // 2, H - 100), foot, font=foot_font, fill=CREAM)

    out = OUT_DIR / filename
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out.name}  (headline {hsize}px)")


if __name__ == "__main__":
    for fn, bg, lines, benefits in PINS:
        make_pin(fn, bg, lines, benefits)
