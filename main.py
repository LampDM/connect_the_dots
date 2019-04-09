import sys
import time
import matplotlib.pyplot as plt
import math
start = time. time()

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
ah=set()
b = []
bh=set()
ac = 0
min_score=float("inf")
min_ind = 0
minas = []
for ln in gen:
    flx = float(ln[1])
    if flx < 0:
        yval = float(ln[2].replace("\n",""))
        if yval<min_score:
            min_score=yval
            min_ind=ac

        a.append(Point(int(ln[0]), flx, yval))
        ac+=1
    else:
        b.append(Point(int(ln[0]), flx, float(ln[2].replace("\n",""))))


minp = min(a,key=lambda e: e.y)



def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def degrees_between(a, b):
    return math.degrees(math.atan((b.y-a.y)/(b.x-a.x)))

def check_rez(rezults):
    intersect_num = 0
    #Check if it's correct:
    for i in range(len(rezults)-1):
        for k in range(i+1,len(rezults)-1):
            if intersect(rezults[i][0],rezults[i][1],rezults[k][0],rezults[k][1]):
                intersect_num+=1
    print("Conflicts: {}".format(intersect_num))

def simple_min_to_min(a,b):
    rezults = []
    for i in range(len(a)):
        rs="{} - {}".format(a[i].ind,b[i].ind)
        plt.plot([a[i].x,b[i].x], [a[i].y, b[i].y])
        print(degrees_between(a[i],b[i]))
        print(rs)
        rezults.append((a[i],b[i]))
    return rezults

def mina_angle(a,b):
    rezults = []
    visited = set()
    for p in a:
        low_score=float("inf")
        low_choice=None
        nd = 0
        for q in b:
            if q in visited:
                continue
            nd=degrees_between(p,q)
            if nd<low_score:
                low_score=nd
                low_choice=q
        visited.add(low_choice)
        rezults.append((p,low_choice))

    return rezults

def plot_rez(rezults):
    print(rezults)
    for a,b in rezults:
        plt.plot([a.x, b.x], [a.y, b.y])

plot_rez(mina_angle(a,b))
end = time. time()
print("Total time: {}".format(end-start))




plt.show()