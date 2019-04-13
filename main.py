import sys
import time
from dot_visualisation import *
import math
from collections import deque

start = time.time()


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
    rez = math.degrees(math.atan((b.y - a.y) / (b.x - a.x)))
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

c = deque(sorted([Point(int(ln[0]), float(ln[1]), float(ln[2].replace("\n", ""))) for ln in gen], key=lambda e: e.y,
                 reverse=True))


def full_graham(cc):
    ia = cc.copy()  # remove this
    if len(ia) == 2:
        return ia

    # Do pruning
    A = None  # (Ax, Ay) which maximizes x - y
    B = None  # (Bx, Xy) which maximizes x + y
    C = None  # (Cx, Cy) which minimizes x - y
    D = None  # (Dx, Dy) which minimizes x + y

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

    ia = [p for p in ia if not (x1 < p.x and p.x < x2 and p.y > y1 and p.y < y2)]

    #Pop the minimum
    minp = ia.pop()

    ia = sorted(ia, key=lambda e: degrees_between(minp, e))
    hull = deque([minp, ia[0]])
    links = deque([])

    # Main Graham Loop
    for s in ia[1:]:
        while det(hull[-2], hull[-1], s) <= 0:
            hull.pop()
        hull.append(s)

    # Collect the links
    for i in range(len(hull) - 1):
        if (hull[i].x * hull[i + 1].x) < 0:
            links.append(hull[i])
            links.append(hull[i + 1])
    if hull[0].x * hull[-1].x < 0:
        links.append(hull[0])
        links.append(hull[-1])
    return list(links)


rzs = []

#Main loop
while c:
    ls = full_graham(c)
    if len(ls) == 4:
        rzs.append(ls[2:])
        rzs.append(ls[:2])

    elif len(ls) == 2:
        rzs.append(ls)
    # Remove links from c
    for lnk in ls:
        c.remove(lnk)

end = time.time()
print("Total time: {}".format(end - start))
check_rez(rzs)

# Rendering
#plot_rezF(rzs)
#render_plots()
