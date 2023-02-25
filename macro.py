import pyautogui as p
import time

a = {
    "tl": (637, 293),
    "tm": (1074, 292),
    "tr": (1624, 266),
    "tml": (469, 512),
    "tmm": (880, 462),
    "tmr": (1526, 521),
    "bml": (661, 649),
    "bmm": (871, 649),
    "bmr": (1496, 681),
    "bl": (555, 871),
    "bm": (1013, 884),
    "br": (1623, 880)
}

b = ["tl", "tm", "tr", "tml", "tmm", "tmr", "bml", "bmm", "bmr", "bl", "bm", "br"]

def checkpx():
    v = 0
    d = len(b)
    print(d)
    for j in b:
        im = p.screenshot()
        px = im.getpixel(a[j])
        if px == (10, 9, 45):
            v += 1
            b.remove(j)
            print(v)
    if v == d:
        exit()
    else:
        return i - v

start = time.time()
i = 1
while i < len(b):
    x = 1
    while x < len(b):
        if b[x] == i:
            x += 1
            continue
        else:
            p.click(a[b[i]][0], a[b[i]][1])
            p.click(a[b[x]][0], a[b[x]][1])
            print("clicked")
        x += 1
    i = checkpx()
    i += 1
if not checkpx():
    for x in range(len(b)):
        if b[x] == b[i]:
            continue
        else:
            p.click(a[b[i]][0], a[b[i]][1])
            p.click(a[b[x]][0], a[b[x]][1])
            print("clicked")
print(time.time() - start)