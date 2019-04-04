import sys
filename = sys.argv[1]

f = open(filename,"r")

for ln in f:
    print(ln)