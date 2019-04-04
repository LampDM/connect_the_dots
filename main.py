import sys

filename = sys.argv[1]

f = open(filename, "r")

gen = (ln for ln in f)

n = gen.__next__()

a = []
b = []
for ln in gen:
    ind, x, y = ln.split(",")
    flx = float(x)
    if flx < 0:
        a.append((int(ind), flx, float(y)))
    else:
        b.append((int(ind), flx, float(y)))


def lines_intersect(p1, p2, p3, p4, q1, q2, q3, q4):
    # u = (q − p) × r / (r × s)
    # If r × s = 0 and (q − p) × r = 0, then the two lines are collinear.
    # https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
    r1 = p2-p1
    r2 = p4-p3
    s1 = q2-q1
    s2 = q4-q3

    # r dot s
    rs = r1 * r2 + s1 * s2
    print(rs)
    qminp = (q1 - p1) * r1 + (q2 - p2) * r2
    return not rs == 0 and qminp == 0

print(lines_intersect(1,2,5,4,2,2,2,9))

print(a)
print(b)
