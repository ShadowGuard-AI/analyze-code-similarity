#!/usr/bin/env python3
"""Similarity banner: the whole horizon from the cab, two columns, the station sign on the door."""
import os, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(31)
V = os.environ.get("VARIANT", "")
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 520
IND = (30, 34, 72); WHITE = (250, 250, 246); GREEN = (110, 178, 128)
img = Image.new("RGB", (W, H), (198, 210, 228)); d = ImageDraw.Draw(img, "RGBA")
for y in range(0, 200):
    t = y / 200
    d.line([(0, y), (W, y)], fill=(int(208 - 20 * t), int(218 - 16 * t), int(234 - 6 * t)))
d.polygon([(0, 196), (300, 168), (640, 190), (940, 164), (1200, 188), (1200, 280), (0, 280)], fill=(128, 134, 172))
d.polygon([(0, 252), (260, 224), (600, 248), (920, 220), (1200, 244), (1200, 340), (0, 340)], fill=(82, 88, 132))
d.polygon([(0, 316), (320, 288), (680, 314), (980, 286), (1200, 308), (1200, 420), (0, 420)], fill=(46, 50, 98))
# dirt road switching down one slope, firebreak crossing another
pts = [(120, 330), (280, 344), (210, 366), (380, 380), (320, 402)]
d.line(pts, fill=(196, 188, 164), width=6)
d.line([(760, 300), (1120, 356)], fill=(172, 178, 150), width=10)
def column(cx, base, top, width, bend):
    steps = 15
    for i in range(steps):
        t = i / steps
        y = base - t * (base - top)
        x = cx + bend * (t * t) * 110
        r = width * (0.55 + t * 0.95)
        d.ellipse([x - r, y - r * 0.62, x + r, y + r * 0.62], fill=(240, 241, 236, 235), outline=(198, 200, 192))
        if i < 4:
            d.ellipse([x - r * 0.68, y - r * 0.38, x + r * 0.68, y + r * 0.38], fill=(*GREEN, 130))
column(215, 300, 44, 56, 1.0)    # left distance, bending in the upper wind
column(1052, 286, 58, 40, 0.55)  # right drainage, slimmer and straighter
# cab framing at the bottom edge: railing, ledge tools, door with the station sign
d.rectangle([0, 428, W, H], fill=(22, 25, 56))
d.rectangle([0, 414, W, 430], fill=(15, 17, 42))
for x in range(24, W, 86):
    d.rectangle([x, 430, x + 11, 478], fill=(15, 17, 42))
# binoculars, map board, open logbook on the ledge
d.rounded_rectangle([70, 386, 116, 412], 7, fill=(10, 12, 30)); d.rounded_rectangle([124, 386, 170, 412], 7, fill=(10, 12, 30))
d.rectangle([300, 380, 470, 414], fill=(226, 220, 198), outline=(120, 116, 100), width=2)
for cx, cy in [(308, 388), (462, 388), (308, 406), (462, 406)]:
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=IND)
d.rectangle([700, 382, 850, 414], fill=(240, 238, 228), outline=(120, 116, 100), width=2)
for yy in range(390, 412, 7):
    d.line([(712, yy), (838, yy)], fill=(170, 172, 180), width=1)
# station sign nailed to the cab door below the railing
font = ImageFont.truetype(os.path.join(HERE, "fonts", "Atma.ttf"), 30 if V == "1" else 27)
sign_w = 560 if V == "1" else 520
d.rectangle([600 - sign_w // 2, 452, 600 + sign_w // 2, 506], fill=(238, 236, 226), outline=(120, 116, 100), width=3)
d.text((600, 466), "analyze-code-similarity", font=font, fill=IND, anchor="ma")
img = img.filter(ImageFilter.GaussianBlur(0.5))
out = os.path.join(HERE, "scratch", f"banner-v{V}.png") if V else os.path.join(HERE, "banner.png")
os.makedirs(os.path.dirname(out), exist_ok=True); img.save(out); print("saved", out)
