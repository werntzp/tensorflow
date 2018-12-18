# ==========================
#
# Purpose: randomly delete frames to cut down on the total number
#
# ==========================
import os
import random

for f in os.listdir(os.getcwd()):
    r = random.randint(1, 11)
    if r > 2:
        os.remove(f)
print("completed")


