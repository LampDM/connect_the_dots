import sys
import time
from dot_visualisation import *
import math

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

    def __str__(self):
        return "Point({} - ({},{}))".format(self.ind, self.x, self.y)


filename = sys.argv[1]

f = open(filename, "r")

gen = sorted([ln.split(",") for ln in f][1:], key=lambda e: float(e[2][:-2]))

a = []
b = []
ac = 0

for ln in gen:
    flx = float(ln[1])
    if flx < 0:
        yval = float(ln[2].replace("\n", ""))
        a.append(Point(int(ln[0]), flx, yval))
        ac += 1
    else:
        b.append(Point(int(ln[0]), flx, float(ln[2].replace("\n", ""))))


# Returns a single list of points
# or touple of lists

def full_graham(cc):
    ia = cc[:]
    if len(ia) == 2:
        return ia
    minp = min(ia, key=lambda e: e.y)
    ia.remove(minp)

    ia = sorted(ia, key=lambda e: degrees_between(minp, e))
    hull = [minp, ia[0]]
    links = []
    for s in ia[1:]:
        while det(hull[-2], hull[-1], s) <= 0:
            hull.pop()
        hull.append(s)

    # Collect the intersections
    for i in range(len(hull) - 1):
        if (hull[i].x * hull[i + 1].x) < 0 and (hull[i] not in links) and (hull[i + 1] not in links):
            links.append(hull[i])
            links.append(hull[i + 1])
    if (hull[0].x * hull[-1].x < 0):
        links.append(hull[0])
        links.append(hull[-1])
    return links


rzs = []

c = a + b
while c:
    ls = full_graham(c)

    if len(ls) == 4:
        rzs.append(ls[2:])
        rzs.append(ls[:2])

    elif len(ls) == 2:
        rzs.append(ls)
    c = [el for el in c if el not in ls]

end = time.time()
print("Total time: {}".format(end - start))

# Rendering
plot_rezF(rzs)
# check_rez(rzs)
render_plots()
