import winsound, time, random

#numberofcombos = 25     #total number of combos to perform
skill = 0             #time between strikes (.5 beginner, .01 advanced, 0 max)
mintime = 1            #minimum time between combos(rcmnd 1)
maxtime = 2  #maximum ause between combos (rcmnd 1-3)
mincmbolngth = 2       #minimum combo length (rcmnd 1-2)
cmbolngth = 4  #maximum number of techniques in a combo (rcmd 1-4)
rndlngth = 1  #length of each round in minutes

techniques = ["jab.wav", "jab.wav", "jab.wav",  "jab.wav", "cross.wav",
"cross.wav", "cross.wav","leadhook.wav", "leaduppercut.wav", "leadelbow.wav",
"rearelbow.wav"]
allhits = len(techniques)-1

def round():
    winsound.PlaySound("startbell.wav", winsound.SND_FILENAME)
    time_end = time.time() + 60 * rndlngth
    while time.time() < time_end:
        combolength = random.randint(mincmbolngth, cmbolngth)
        for bam in range(combolength):
            num = random.randint(0, allhits)
            print(techniques[num])
            winsound.PlaySound(techniques[num], winsound.SND_FILENAME)
            time.sleep(skill)
        print("    ")
        tbtc= random.randint(mintime, maxtime)  #time btween combos
        time.sleep(tbtc)
    winsound.PlaySound("startbell.wav", winsound.SND_FILENAME)
    start()

def start():
    print("enter q to quit, press enter to start a round")
    inp = input()
    if inp == "q":
        quit()
    else:
        round()

start()
