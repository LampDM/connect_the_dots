import sys
import os
import subprocess
try:
    for i in range(1000):
        os.system("python testgen.py")
        #os.system("python main.py testx.txt")
        f = subprocess.check_output("python main.py testx.txt", shell=True)
        if "Conflicts: 0" in f.decode("utf-8"):
            print(f.decode("utf-8"))
        else:
            print(f.decode("utf-8"))
            break

except Exception as ex:
    print(ex)