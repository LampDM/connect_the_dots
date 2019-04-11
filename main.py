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
    return math.degrees(math.atan((b.y - a.y) / (b.x - a.x)))


# Check for any conflicts
def check_rez(rezults):
    intersect_num = 0
    # Check if it's correct:
    for i in range(len(rezults) - 1):
        for k in range(i + 1, len(rezults) - 1):
            if intersect(rezults[i][0], rezults[i][1], rezults[k][0], rezults[k][1]):
                intersect_num += 1
    print("Conflicts: {}".format(intersect_num))

def plot_rez(rezults):
    for a, b in rezults:
        store_plots([a.x, b.x], [a.y, b.y])

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
ah = set()
b = []
bh = set()
ac = 0
min_score = float("inf")
min_ind = 0
minas = []
for ln in gen:
    flx = float(ln[1])
    if flx < 0:
        yval = float(ln[2].replace("\n", ""))
        if yval < min_score:
            min_score = yval
            min_ind = ac

        a.append(Point(int(ln[0]), flx, yval))
        ac += 1
    else:
        b.append(Point(int(ln[0]), flx, float(ln[2].replace("\n", ""))))


# Returns a single list of points
# or touple of lists
def half_graham(ia, ib):
    if len(ia) == 1:
        k = [[ia[0], ib[0]]]
        return k
    minp = min(ia, key=lambda e: e.y)
    maxp = max(ia, key=lambda e: e.y)
    ib = sorted(ib, key=lambda e: degrees_between(minp, e))
    ib.append(maxp)

    hull = [minp, ib[0]]

    for s in ib[1:]:
        while det(hull[-2], hull[-1], s) <= 0:
            hull.pop()
        hull.append(s)
    l1 = hull[:2]
    l2 = hull[-2:]
    # ([point,point],[point,point])
    return [l1, l2]


rzs = []
while a:
    hg = half_graham(a, b)
    print(len(a))
    if len(hg) == 2:
        l1, l2 = hg
        rzs.append(l1)
        rzs.append(l2)
        a.remove(l1[0])
        a.remove(l2[1])

        b.remove(l1[1])
        b.remove(l2[0])
    else:
        l1 = hg[0]
        rzs.append(l1)
        a.remove(l1[0])

#TODO Implement FULl Graham Scan
end = time.time()
print("Total time: {}".format(end - start))

# Rendering
plot_rez(rzs)
check_rez(rzs)
render_plots()
