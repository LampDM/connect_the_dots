import random

f = open("testx.txt", "w")

f.write("10000\n")
uz = 5000
ov = 5000
ind = 0
while uz != 0 and ov != 0:
    r = random.uniform(-100.0, 100.0)
    ind += 1
    if r < 0:
        uz -= 1
        f.write("{},{},{}\n".format(ind,r ,random.uniform(-100.0, 100.0)))
    else:
        ov -= 1
        f.write("{},{},{}\n".format(ind,r ,random.uniform(-100.0, 100.0)))
