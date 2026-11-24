#!/usr/bin/env python3
"""news-23 b22 front-page-dense: draw THE WORLD TODAY, Monday 23 November 2026."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (17, 17, 17)
RED = (178, 34, 34)
NAVY = (13, 27, 62)
TEAL = (14, 107, 107)
GOLD = (184, 134, 11)
GREEN = (46, 125, 50)
PURPLE = (106, 27, 154)
GREY = (90, 90, 90)
DARK = (30, 30, 30)

FD = "/usr/share/fonts/truetype/dejavu/"


def f_serif(size, bold=False):
    return ImageFont.truetype(FD + ("DejaVuSerif-Bold.ttf" if bold else "DejaVuSerif.ttf"), size)


def f_sans(size, bold=False):
    return ImageFont.truetype(FD + ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"), size)


def wrap(d, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, text, font, fill, max_w, leading, max_lines=None):
    lines = wrap(d, text, font, max_w)
    if max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += leading
    return y


def chip(d, x, y, label, color):
    f = f_sans(9, True)
    w_ = d.textlength(label, font=f) + 10
    d.rounded_rectangle([x, y, x + w_, y + 14], radius=3, fill=color)
    d.text((x + 5, y + 2), label, font=f, fill=(255, 255, 255))
    return w_


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- masthead ----
d.rectangle([0, 0, W, 64], fill=(0, 0, 0))
d.text((14, 6), "THE WORLD TODAY", font=f_serif(50, True), fill=(255, 255, 255))
d.text((640, 22), "MONDAY  23 NOVEMBER 2026", font=f_sans(17, True), fill=(212, 175, 55))

# ---- kicker ----
d.text((14, 70), "AI rout hits Asia  ·  UN chief urges AI rules  ·  US lead over China at record low  ·  Anthropic IPO $107.3B",
       font=f_serif(15, True), fill=RED)

# ---- number strip ----
nums = [("-3.3%", "KOSPI", RED), ("5.3", "US-CHINA POWER GAP", NAVY),
        ("11,762", "EBOLA CASES, DRC", (139, 90, 0)), ("$450M", "SKUBAL DEAL", PURPLE),
        ("$107.3B", "ANTHROPIC IPO", (128, 0, 128))]
x = 14
cw = 196
for val, lab, col in nums:
    d.text((x, 94), val, font=f_sans(30, True), fill=col)
    d.text((x, 126), lab, font=f_sans(11, True), fill=INK)
    x += cw
d.line([14, 146, 1010, 146], fill=INK, width=2)

# ---- day in numbers strip ----
d.rectangle([14, 150, 1010, 168], fill=NAVY)
d.text((20, 154), "THE DAY IN NUMBERS", font=f_sans(11, True), fill=(255, 255, 255))
d.text((200, 154), "-5.8% intraday low   ·   165 missiles in a week   ·   12,000 cleared   ·   264 kg seized   ·   2% tax backed",
       font=f_sans(11), fill=(255, 255, 255))

# ---- region bar ----
regions = [("ASIA-PACIFIC 7", (46, 125, 50), 7), ("AMERICAS 8", NAVY, 8),
           ("MIDDLE EAST 6", (139, 90, 0), 6), ("EUROPE 5", TEAL, 5),
           ("AFRICA 3", PURPLE, 3), ("WORLD 2", GREY, 2)]
rx = 14
for lab, col, n in regions:
    w_ = int(996 * n / 31)
    d.rectangle([rx, 172, rx + w_ - 2, 190], fill=col)
    d.text((rx + 6, 176), lab, font=f_sans(10, True), fill=(255, 255, 255))
    rx += w_

# ---- heroes ----
HX = [14, 354, 694]
HW = 316
HY = 196
SCENE_H = 148

# hero 1: Kospi chart
x0 = HX[0]
d.rectangle([x0, HY, x0 + HW, HY + SCENE_H], fill=(13, 27, 62))
# skyline
import random
random.seed(7)
for i in range(14):
    bx = x0 + 8 + i * 22
    bh = random.randint(18, 52)
    d.rectangle([bx, HY + SCENE_H - 22 - bh, bx + 16, HY + SCENE_H - 22], fill=(24, 48, 96))
    for wy in range(2):
        for wx in range(2):
            d.rectangle([bx + 3 + wx * 7, HY + SCENE_H - 22 - bh + 4 + wy * 12, bx + 6 + wx * 7, HY + SCENE_H - 22 - bh + 8 + wy * 12], fill=(255, 214, 90))
# chart line
pts = [(x0 + 14, HY + 62), (x0 + 60, HY + 48), (x0 + 110, HY + 58), (x0 + 160, HY + 44),
       (x0 + 205, HY + 66), (x0 + 250, HY + 78), (x0 + 300, HY + 96)]
d.line(pts, fill=(255, 80, 80), width=3)
for px, py in pts:
    d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=(255, 214, 90))
d.text((x0 + 10, HY + 6), "-3.3%", font=f_sans(34, True), fill=(255, 80, 80))
d.rectangle([x0, HY + SCENE_H - 22, x0 + HW, HY + SCENE_H], fill=(0, 0, 0))
d.text((x0 + 8, HY + SCENE_H - 19), "KOSPI  4,708.54   ·   -161 PTS", font=f_sans(12, True), fill=(255, 255, 255))

# hero 2: Guterres
x0 = HX[1]
d.rectangle([x0, HY, x0 + HW, HY + SCENE_H], fill=TEAL)
d.text((x0 + 10, HY + 8), "150 DELEGATES", font=f_sans(30, True), fill=(255, 214, 90))
d.text((x0 + 10, HY + 44), "BACK A RISK FRAMEWORK", font=f_sans(17, True), fill=(255, 255, 255))
# globe
gx, gy, gr = x0 + HW - 52, HY + 104, 32
d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(168, 216, 232))
d.ellipse([gx - 18, gy - 22, gx + 2, gy - 2], fill=(46, 125, 50))
d.ellipse([gx - 4, gy + 4, gx + 20, gy + 24], fill=(46, 125, 50))
d.ellipse([gx - 24, gy + 6, gx - 10, gy + 20], fill=(46, 125, 50))
# flags
for i, fc in enumerate([(178, 34, 34), (30, 90, 200), (255, 214, 90)]):
    fx = x0 + 22 + i * 46
    d.line([fx, HY + 96, fx, HY + 132], fill=(255, 255, 255), width=2)
    d.polygon([(fx, HY + 96), (fx + 30, HY + 104), (fx, HY + 112)], fill=fc)
d.rectangle([x0, HY + SCENE_H - 22, x0 + HW, HY + SCENE_H], fill=(0, 0, 0))
d.text((x0 + 8, HY + SCENE_H - 19), "UN  ·  BRIDGETOWN", font=f_sans(12, True), fill=(255, 255, 255))

# hero 3: power bars
x0 = HX[2]
d.rectangle([x0, HY, x0 + HW, HY + SCENE_H], fill=(255, 255, 255), outline=(150, 150, 150))
d.text((x0 + 10, HY + 6), "NARROWEST SINCE 2018", font=f_sans(13, True), fill=INK)
d.text((x0 + HW - 78, HY + 6), "GAP 5.3", font=f_sans(13, True), fill=GOLD)
bars = [("US", 78.9, NAVY), ("CHINA", 73.6, RED), ("INDIA", 40.5, GOLD)]
bx = x0 + 34
for lab, val, col in bars:
    bh = int(val * 0.85)
    d.rectangle([bx, HY + SCENE_H - 34 - bh, bx + 56, HY + SCENE_H - 34], fill=col)
    d.text((bx + 8, HY + SCENE_H - 34 - bh - 20), f"{val}", font=f_sans(15, True), fill=col)
    d.text((bx + 6, HY + SCENE_H - 30), lab, font=f_sans(11, True), fill=INK)
    bx += 92

# hero headlines + bodies
heroes = [
    ("1  AI ROUT HITS ASIA",
     "Kospi -3.3% to 4,708.54, sheds 161 pts; intraday -5.8%. Samsung -3.1%, SK Hynix -2.5%.",
     "KOREA EXCHANGE"),
    ("2  GUTERRES: REGULATE AI BEFORE IT'S TOO LATE",
     "UN chief urges global AI safety rules at the Bridgetown summit; 150 delegates back a risk framework.",
     "UNITED NATIONS"),
    ("3  US LEAD OVER CHINA AT RECORD LOW",
     "Asia Power Index 2026: US 78.9, China 73.6 - gap 5.3, narrowest since 2018. India third at 40.5.",
     "LOWY INSTITUTE"),
]
hy = HY + SCENE_H + 8
for i, (hl, body, src) in enumerate(heroes):
    x0 = HX[i]
    y = text_block(d, x0, hy, hl, f_sans(15, True), INK, HW, 18, max_lines=2)
    y = text_block(d, x0, y + 2, body, f_sans(11), INK, HW, 14, max_lines=3)
    d.text((x0, y + 4), src, font=f_sans(9), fill=GREY)
    chip(d, x0 + HW - 62, y + 2, "REPORTED", NAVY)

# ---- more of the day ----
d.line([14, 452, 1010, 452], fill=INK, width=2)
d.text((14, 458), "MORE OF THE DAY  —  10 STORIES", font=f_sans(14, True), fill=INK)

cards = [
    ("AMERICAS", "4", "BESSENT: NVIDIA ANSWERS", "Treasury chief wants to know of violations over China sales.", "Reuters", "REPORTED", NAVY),
    ("FBI", "5", "FBI PROBES NCIC HACK", "Hackers hit the NCIC system used by police nationwide.", "AP", "REPORTED", NAVY),
    ("WHITE HOUSE", "6", "TRUMP: IRAN STRIKES MAY RESUME", "President says strikes could resume in the New Year.", "Reuters", "REPORTED", NAVY),
    ("MARKETS", "7", "US FUTURES JUMP 3%", "Holiday-week rally lifts Nasdaq futures as the AI rout cools.", "Bloomberg", "REPORTED", NAVY),
    ("SPORT", "8", "SKUBAL'S $450M METS DEAL", "Two-time Cy Young winner signs nine years, largest ever for a pitcher.", "ESPN", "REPORTED", NAVY),
    ("SPORT", "9", "TOM JACKSON DIES AT 75", "Broncos linebacker turned ESPN voice dies.", "ESPN", "REPORTED", NAVY),
    ("LEGAL", "10", "STATES SUE SPACEX", "Ten states challenge AI safety claims.", "AP", "REPORTED", NAVY),
    ("TECH", "11", "ANTHROPIC IPO: $107.3B", "Claude maker raises at $83 a share; debut closes $97.17.", "WSJ", "REPORTED", NAVY),
    ("EUROPE", "12", "POLAND: 3 RUSSIAN MISSILES CROSSED AIRSPACE", "Kyiv says three Kh-101s crossed Polish airspace Friday.", "AP", "CLAIM", RED),
    ("SPACE", "13", "RUSSIAN NUCLEAR SATELLITE", "Intel claims Moscow built a satellite to carry a nuclear warhead.", "Reuters", "CLAIM", RED),
]
cat_colors = {"AMERICAS": (139, 30, 30), "FBI": (90, 30, 120), "WHITE HOUSE": (139, 90, 0),
              "MARKETS": (14, 107, 107), "SPORT": (46, 125, 50), "LEGAL": (90, 30, 120),
              "TECH": (13, 27, 62), "EUROPE": (139, 30, 30), "SPACE": (90, 90, 90)}
CY0, CH, CW, CG = 482, 82, 194, 7
for idx, (cat, num, hl, body, src, chip_lab, chip_col) in enumerate(cards):
    r, c = divmod(idx, 5)
    x0 = 14 + c * (CW + CG)
    y0 = CY0 + r * (CH + 6)
    d.rectangle([x0, y0, x0 + CW, y0 + CH], outline=(160, 160, 160))
    d.rectangle([x0, y0, x0 + CW, y0 + 16], fill=cat_colors[cat])
    d.text((x0 + 5, y0 + 2), cat, font=f_sans(9, True), fill=(255, 255, 255))
    d.text((x0 + CW - 18, y0 + 2), num, font=f_sans(10, True), fill=(255, 255, 255))
    y = text_block(d, x0 + 5, y0 + 19, hl, f_sans(11, True), INK, CW - 10, 13, max_lines=2)
    y = text_block(d, x0 + 5, y + 1, body, f_sans(9), INK, CW - 10, 11, max_lines=2)
    d.text((x0 + 5, y0 + CH - 15), src, font=f_sans(8), fill=GREY)
    chip(d, x0 + CW - 66, y0 + CH - 16, chip_lab, chip_col)

# ---- map + also ----
d.line([14, 664, 1010, 664], fill=INK, width=2)
d.text((14, 670), "WHERE IT HAPPENED", font=f_sans(14, True), fill=INK)
d.text((500, 670), "ALSO ON MONDAY", font=f_sans(14, True), fill=INK)
MX, MY, MW, MH = 14, 692, 466, 158
d.rectangle([MX, MY, MX + MW, MY + MH], fill=(214, 232, 240), outline=(160, 160, 160))
for gx in range(MX + 20, MX + MW, 24):
    d.line([gx, MY, gx, MY + MH], fill=(190, 210, 220), width=1)
for gy in range(MY + 20, MY + MH, 24):
    d.line([MX, gy, MX + MW, gy], fill=(190, 210, 220), width=1)
# continents (simplified)
d.polygon([(30, 706), (120, 700), (180, 712), (196, 736), (168, 762), (120, 772), (60, 762), (26, 730)], fill=(139, 188, 122))
d.polygon([(150, 776), (192, 780), (188, 812), (162, 820), (148, 796)], fill=(139, 188, 122))
d.polygon([(258, 706), (300, 700), (316, 716), (292, 732), (262, 728)], fill=(139, 188, 122))
d.polygon([(262, 736), (302, 736), (312, 776), (288, 824), (266, 812), (256, 766)], fill=(139, 188, 122))
d.polygon([(322, 700), (452, 694), (470, 722), (442, 752), (400, 734), (362, 748), (330, 722)], fill=(139, 188, 122))
d.polygon([(402, 800), (452, 800), (456, 824), (410, 828)], fill=(139, 188, 122))
pins = [(446, 706, "1"), (104, 792, "2"), (408, 700, "3"), (96, 726, "4"), (122, 716, "5"),
        (332, 726, "6"), (84, 742, "7"), (52, 748, "8"), (72, 766, "9"), (98, 786, "10"),
        (278, 706, "11"), (302, 722, "12"), (336, 698, "13")]
for px, py, n in pins:
    d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline=(255, 255, 255))
    f = f_sans(9, True)
    tw = d.textlength(n, font=f)
    d.text((px - tw / 2, py - 6), n, font=f, fill=(255, 255, 255))
d.text((MX, MY + MH + 4), "Pins 1-13:  1 Seoul  ·  2 Bridgetown  ·  3 Beijing  ·  4 Washington  ·  5 New York  ·  6 Tehran  ·  7 Chicago",
       font=f_sans(9), fill=INK)
d.text((MX, MY + MH + 17), "8 San Francisco  ·  9 Denver  ·  10 Austin  ·  11 Warsaw  ·  12 Kyiv  ·  13 Moscow",
       font=f_sans(9), fill=INK)

also_l = ["14. Paris: 100+ back 2% billionaire tax", "15. Manchester: 12,000 cleared",
          "16. Zelenskyy: 165 missiles in a week", "17. COP31: the day after pact rejected",
          "18. Benghazi: UN demands port probe", "19. Israel unity talks resume",
          "20. Gaza: two killed in Israeli strike", "21. West Bank settler attacks",
          "22. Iran war: no deal in sight"]
also_r = ["23. Lebanon seizes 264 kg explosives", "24. Bahrain: strike hits plant, 2 hurt",
          "25. Sudan: defences down drones", "26. DRC: fighting traps Ebola teams",
          "27. Bangladesh: Hasina jailed if she returns", "28. Seoul minister quits in exam row",
          "29. SK Telecom -7.3% as hype cools", "30. China eases margin rules",
          "31. Seoul readies 10T-won fund"]
ay = MY + 2
for t in also_l:
    d.text((500, ay), t, font=f_sans(11), fill=INK)
    ay += 19
ay = MY + 2
for t in also_r:
    d.text((760, ay), t, font=f_sans(11), fill=INK)
    ay += 19

# ---- date check ----
d.rectangle([14, 884, 1010, 952], outline=RED, width=3)
d.text((22, 890), "DATE CHECK", font=f_sans(14, True), fill=RED)
d.text((140, 890), "READ 23 NOV 2026, 23:59 UTC  —  STORIES DATED 23 NOV ONLY", font=f_sans(12, True), fill=INK)
text_block(d, 22, 912, "LEFT OUT — NOT 23 NOV:  Democrats reach 258 seats (22 Nov)  ·  Sparta II fire (22 Nov)  ·  El Chapo Isidro captured (22 Nov)  ·  EU-Indonesia pact (21 Nov)  ·  Nigeria boat (21 Nov)  ·  ICJ Myanmar ruling (19 Nov)",
           f_sans(11), INK, 970, 14, max_lines=1)
text_block(d, 22, 930, "NOT YET:  Dymer search continues (14 missing)  ·  4 House races uncalled  ·  COP32 venue not set  ·  WHO evacuating trapped Ebola staff",
           f_sans(11), INK, 970, 14, max_lines=1)

# ---- sources ----
d.text((14, 958), "Sources: Reuters  ·  AP  ·  Bloomberg  ·  AFP  ·  Yonhap  ·  BBC  ·  WSJ  ·  NYT  ·  ESPN  ·  Lowy Institute (Asia Power Index 2026).",
       font=f_sans(9), fill=GREY)
d.text((14, 972), "CHIPS:  REPORTED = confirmed by wires  ·  CLAIM = one side's claim, not independently confirmed  ·  ONGOING = still developing",
       font=f_sans(9), fill=GREY)

# ---- bottom strip ----
d.rectangle([0, 990, W, H], fill=(0, 0, 0))
d.text((14, 1000), "Scenes are drawn illustrations, not photographs.   ·   THE WORLD TODAY — Monday 23 November 2026   ·   31 stories   ·   6 regions",
       font=f_sans(11, True), fill=(212, 175, 55))

img.save("entry.png")
print("saved entry.png", img.size)
