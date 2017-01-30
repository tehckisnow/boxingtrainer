import random
import time
attacks=["jab", "jab", "jab", "jab", "cross", "cross", "cross", "lead hook", "rear hook", "lead uppercut", "rear uppercut"]
wait = [0, 0, 0, 1, 2]
numberofhits = 10
ln1 = len(attacks) - 1
ln2 = len(wait) - 1
for hit in range(numberofhits):
    num = random.randint (0, ln1)
    print(attacks[num])
    num2 = random.randint(0, ln2)
    time.sleep(wait[num2])
    
