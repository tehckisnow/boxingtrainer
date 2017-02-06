import winsound, time, random

numberofcombos = 5     #total number of combos to perform
skill = .5             #time between strikes (.5 beginner, .01 advanced, 0 max)
mintime = 1            #minimum time between combos(rcmnd 1)
maxtime = 3  #maximum ause between combos (rcmnd 1-3)
mincmbolngth = 2       #minimum combo length (rcmnd 1-2)
cmbolngth = 4  #maximum number of techniques in a combo (rcmd 1-4)

techniques = ["jab.wav", "jab.wav", "jab.wav", "cross.wav", "cross.wav",
"leadhook.wav", "leaduppercut.wav", "leadelbow.wav", "rearelbow.wav"]
allhits = len(techniques)-1
winsound.PlaySound("startbell.wav", winsound.SND_FILENAME)
for hit in range(numberofcombos):
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

#jab.wav
#cross.wav
#leadhook.wav
#leaduppercut.wav
#leadelbow.wav
#rearelbow.wav
#startbell.wav
