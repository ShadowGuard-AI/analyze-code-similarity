#!/usr/bin/env python3
"""Similarity intro: one smoke column getting organised, one faint smudge. Scenery only, no text."""
import os, random
from PIL import Image, ImageDraw, ImageFilter
random.seed(23)
V = os.environ.get("VARIANT", "")
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 520
IND = (30, 34, 72); WHITE = (244, 244, 238); GREEN = (110, 178, 128)
img = Image.new("RGB", (W, H), (196, 208, 226)); d = ImageDraw.Draw(img, "RGBA")
for y in range(0, 190):
    t = y / 190
    d.line([(0, y), (W, y)], fill=(int(206 - 22 * t), int(216 - 18 * t), int(232 - 8 * t)))
# thin cloud streaks leaning with the wind
for (cy, ln) in [(36, 300), (74, 420), (112, 260)]:
    d.line([(80, cy), (80 + ln, cy - 14)], fill=(250, 250, 246, 190), width=7)
    d.line([(620, cy + 18), (620 + ln * 0.7, cy + 6)], fill=(250, 250, 246, 150), width=5)
# ridges, each paler than the one in front
d.polygon([(0, 210), (300, 178), (640, 200), (940, 172), (1200, 196), (1200, 300), (0, 300)], fill=(122, 128, 168))
d.polygon([(0, 268), (260, 238), (600, 262), (920, 232), (1200, 258), (1200, 360), (0, 360)], fill=(76, 82, 128))
d.polygon([(0, 330), (320, 302), (680, 328), (980, 300), (1200, 322), (1200, 430), (0, 430)], fill=(44, 48, 96))
for _ in range(420):  # forest speckle on the near ridge
    x, y = random.uniform(0, W), random.uniform(312, 400)
    d.line([(x, y), (x, y - random.uniform(6, 13))], fill=(30, 34, 70), width=2)
def column(cx, base, top, width, alpha, curl):
    steps = 15
    for i in range(steps):
        t = i / steps
        y = base - t * (base - top)
        x = cx + curl * (t * t) * 90
        r = width * (0.55 + t * 0.95)
        col = (238, 240, 236, int(alpha * (1 - t * 0.35)))
        d.ellipse([x - r, y - r * 0.62, x + r, y + r * 0.62], fill=col)
        if i < 4:
            d.ellipse([x - r * 0.7, y - r * 0.4, x + r * 0.7, y + r * 0.4], fill=(*GREEN, int(alpha * 0.5)))
w1 = 30 if V == "1" else 52
column(430, 322, 66, w1, 235, 1.0)  # v1 too thin and straight; v2 finds its width and curl
# second distant smudge, far right, barely a thickening of air
for i in range(6):
    t = i / 6; y = 268 - t * 60; x = 1010 + t * 26; r = 34 + t * 26
    d.ellipse([x - r, y - r * 0.4, x + r, y + r * 0.4], fill=(232, 234, 230, 52))
# lookout cab railing and roof corner in deep indigo shadow, binoculars on the rail
d.polygon([(0, 520), (0, 452), (1200, 438), (1200, 520)], fill=(22, 25, 56))
d.rectangle([0, 436, W, 452], fill=(16, 18, 44))
for x in range(30, W, 90):
    d.rectangle([x, 452, x + 12, 500], fill=(16, 18, 44))
d.polygon([(880, 0), (1200, 0), (1200, 58), (1010, 30)], fill=(22, 25, 56))
bx, by = 250, 408
d.rounded_rectangle([bx, by, bx + 54, by + 30], 8, fill=(14, 16, 38))
d.rounded_rectangle([bx + 62, by, bx + 116, by + 30], 8, fill=(14, 16, 38))
d.rectangle([bx + 50, by + 10, bx + 66, by + 20], fill=(14, 16, 38))
d.line([(bx + 108, by + 30), (bx + 118, by + 58)], fill=(14, 16, 38), width=4)
img = img.filter(ImageFilter.GaussianBlur(0.6))
out = os.path.join(HERE, "scratch", f"intro-v{V}.png") if V else os.path.join(HERE, "intro-banner.png")
os.makedirs(os.path.dirname(out), exist_ok=True); img.save(out); print("saved", out)
