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

class Point:
    def __init__(self, xarg, yarg):
        self.x = xarg
        self.y = yarg

def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

# Write more tests
print(intersect(Point(1,2),Point(5,4),Point(2,2),Point(2,9)))
print(intersect(Point(0,0),Point(0,10),Point(-3,-3),Point(2,2)))
print(intersect(Point(0,0),Point(0,10),Point(5,1),Point(5,55)))



print(a)
print(b)
