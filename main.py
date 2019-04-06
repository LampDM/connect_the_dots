import sys


class Point:

    def __init__(self,ind, xarg, yarg):
        self.ind = ind
        self.x = xarg
        self.y = yarg
    def __str__(self):
        return "Point({} - ({},{}))".format(self.ind,self.x,self.y)

filename = sys.argv[1]

f = open(filename, "r")

gen = sorted([ln.split(",") for ln in f][1:], key=lambda e: float(e[2][:-2]))

a = []
b = []

for ln in gen:
    flx = float(ln[1])
    if flx < 0:
        a.append(Point(int(ln[0]),flx,float(ln[2].replace("\n",""))))
    else:
        b.append(Point(int(ln[0]), flx, float(ln[2].replace("\n",""))))


def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


for i in range(5):
    print("{} - {}".format(a[i].ind,b[i].ind))