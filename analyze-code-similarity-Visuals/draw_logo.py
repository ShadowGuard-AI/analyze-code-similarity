#!/usr/bin/env python3
"""Similarity logo: twin smoke columns, the gap between them, the tower below. Name in Atma."""
import os
from PIL import Image, ImageDraw, ImageFont
V = os.environ.get("VARIANT", "")
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 960, 640
IND = (30, 34, 72); WHITE = (250, 250, 246); GREEN = (110, 178, 128); MAG = (214, 40, 120)
img = Image.new("RGB", (W, H), WHITE); d = ImageDraw.Draw(img)
def column(cx, base, top, width, thread=False, squash=1.0):
    steps = 14
    pts = []
    for i in range(steps):
        t = i / steps
        y = base - t * (base - top)
        x = cx + (t * t) * 56
        r = width * (0.55 + t * 0.95) * squash
        shade = (236 - int(10 * t), 238 - int(8 * t), 232)
        d.ellipse([x - r, y - r * 0.62, x + r, y + r * 0.62], fill=shade, outline=(196, 198, 190))
        if i < 3:
            d.ellipse([x - r * 0.66, y - r * 0.36, x + r * 0.66, y + r * 0.36], fill=GREEN)
        pts.append((x + r * 0.92, y))
    if thread:
        d.line(pts, fill=MAG, width=5)
gap = 30 if V == "1" else 74  # v1 columns nearly touch; v2 restores the judging gap
column(400 - gap // 2, 430, 60, 62)
column(560 + gap // 2, 430, 66, 55, thread=True)
# forested ridge
d.polygon([(0, 452), (220, 424), (480, 446), (720, 420), (960, 444), (960, 500), (0, 500)], fill=IND)
# lookout tower between the bases: timber frame, glassed cab
tx = 480
d.polygon([(tx - 52, 452), (tx - 30, 356), (tx + 30, 356), (tx + 52, 452)], outline=IND, width=6)
d.line([(tx - 44, 420), (tx + 44, 420)], fill=IND, width=5)
d.line([(tx - 50, 450), (tx + 28, 360)], fill=IND, width=4)
d.line([(tx + 50, 450), (tx - 28, 360)], fill=IND, width=4)
d.rectangle([tx - 44, 316, tx + 44, 360], fill=(168, 198, 216), outline=IND, width=5)
d.line([(tx, 316), (tx, 360)], fill=IND, width=3)
d.polygon([(tx - 56, 316), (tx + 56, 316), (tx + 38, 292), (tx - 38, 292)], fill=IND)
font = ImageFont.truetype(os.path.join(HERE, "fonts", "Atma.ttf"), 46)
d.text((44, 528), "analyze-code-similarity", font=font, fill=IND)
d.line([(44, 592), (916, 592)], fill=IND, width=3)
out = os.path.join(HERE, "scratch", f"logo-v{V}.png") if V else os.path.join(HERE, "logo.png")
os.makedirs(os.path.dirname(out), exist_ok=True); img.save(out); print("saved", out)
if not V:
    img.resize((96, 64)).save(os.path.join(HERE, "scratch", "logo64-ship.png"))
