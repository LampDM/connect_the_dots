import os
import subprocess
import time

n = 100
tt = 0
try:
    for i in range(n):
        os.system("python testgen.py")
        start = time.time()
        f = subprocess.check_output("python main.py testx.txt", shell=True)
        end = time.time()
        print(f.decode("utf-8"))
        print("Total time: {}".format(end - start))
        tt = tt + (end - start)
        # if "Conflicts: 0" in f.decode("utf-8"):
        # print(f.decode("utf-8"))
        # else:
        # print(f.decode("utf-8"))
        # break

except Exception as ex:
    print(ex)

print("Average time: {}".format(tt / n))
