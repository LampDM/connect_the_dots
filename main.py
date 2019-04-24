import sys

import math
from collections import deque

# Determinant
def det(p1, p2, p3):
    return (p2.x - p1.x) * (p3.y - p1.y) \
           - (p2.y - p1.y) * (p3.x - p1.x)

# Checking if lines intersect
def ccw(A, B, C):
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)


def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


# Get the degrees between two points
def degrees_between(a, b):
    subrez = b.x - a.x
    if subrez == 0:
        subrez = 0.00000001
    rez = math.degrees(math.atan((b.y - a.y) / subrez))
    if rez < 0:
        rez = rez + 180
    return rez


# Check for any conflicts
def check_rez(rezults):
    intersect_num = 0
    # Check if it's correct:
    for i in range(len(rezults) - 1):
        for k in range(i + 1, len(rezults) - 1):
            if intersect(rezults[i][0], rezults[i][1], rezults[k][0], rezults[k][1]):
                intersect_num += 1
    print("Conflicts: {}".format(intersect_num))
    return intersect_num > 0


class Point:

    def __init__(self, ind, xarg, yarg):
        self.ind = ind
        self.x = xarg
        self.y = yarg
        self.ac = xarg - yarg
        self.bd = xarg + yarg

    def __str__(self):
        return "Point({} - ({},{}))".format(self.ind, self.x, self.y)


filename = sys.argv[1]

f = open(filename, "r")

gen = ([ln.split(",") for ln in f][1:])

c = deque(sorted([Point(int(ln[0]), float(ln[1]), float(ln[2].replace("\n", ""))) for ln in gen],
                 key=lambda e: (e.y, e.x),
                 reverse=True))

second = 0
x1prev = None
x2prev = None
y1prev = None
y2prev = None

def full_graham(cc):
    ia = cc

    length = len(ia)

    if length == 2:
        print("{} - {}".format(ia[0].ind, ia[1].ind))
        return ia.copy()

    if length > 200:

        global second
        global x1prev
        global x2prev
        global y1prev
        global y2prev

        if not second:
            # Do pruning
            maxA = float("-inf")
            maxB = float("-inf")
            minC = float("inf")
            minD = float("inf")

            for p in ia:
                if p.ac > maxA:
                    A = p
                    maxA = p.ac
                if p.bd > maxB:
                    B = p
                    maxB = p.bd
                if p.ac < minC:
                    C = p
                    minC = p.ac
                if p.bd < minD:
                    D = p
                    minD = p.bd

            x1 = max(C.x, D.x)
            x2 = min(A.x, B.x)
            y1 = max(A.y, D.y)
            y2 = min(B.y, C.y)

            x1prev=x1
            x2prev=x2
            y1prev=y1
            y2prev=y2

            second = True

        else:

            x1 = x1prev*0.97
            x2 = x2prev*0.97
            y1 = y1prev*0.97
            y2 = y2prev*0.97
            second = False

        ia = [p for p in ia if not (x1 < p.x < x2 and y1 < p.y < y2)]
    else:
        ia = cc.copy()
    # Pop the minimum
    minp = ia.pop()

    ia = sorted(ia, key=lambda e: degrees_between(minp, e))
    hull = deque([minp, ia[0]])
    links = deque([])

    # Main Graham Loop
    for s in ia[1:]:
        while det(hull[-2], hull[-1], s) <= 0:
            hull.pop()
        hull.append(s)

    seenlinks = set()
    # Collect the links
    for i in range(len(hull) - 1):
        if (hull[i].x * hull[i + 1].x) < 0:
            if hull[i] in seenlinks:
                continue
            if hull[i + 1] in seenlinks:
                continue
            links.append(hull[i])
            seenlinks.add(hull[i])
            links.append(hull[i + 1])
            seenlinks.add(hull[i + 1])
            print("{} - {}".format(hull[i].ind, hull[i + 1].ind))
    if hull[0].x * hull[-1].x < 0:
        if hull[0] in seenlinks:
            pass
        elif hull[-1] in seenlinks:
            pass
        else:
            links.append(hull[0])
            links.append(hull[-1])
            print("{} - {}".format(hull[0].ind, hull[-1].ind))

    return list(links)


rzs = deque([])

# Main loop
while c:
    ls = full_graham(c)

    if len(ls) == 4:
        rzs.append(ls[2:])
        rzs.append(ls[:2])

    elif len(ls) == 2:
        rzs.append(ls)
    # Remove links from c
    [c.remove(lnk) for lnk in ls]

