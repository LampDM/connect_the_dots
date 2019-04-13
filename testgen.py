import random

f = open("testx.txt", "w")
num=2000
f.write("{}\n".format(num))

ind = 0
for i in range(round(num/2)):
    rn = random.uniform(-1000.0, -1)
    rp = random.uniform(1, 1000.0)
    ind += 1
    f.write("{},{},{}\n".format(ind, rn, random.uniform(-1000.0, 1000.0)))
    ind += 1
    if ind == num:
        f.write("{},{},{}".format(ind, rp, random.uniform(-1000.0, 1000.0)))
    else:
        f.write("{},{},{}\n".format(ind, rp, random.uniform(-1000.0, 1000.0)))



