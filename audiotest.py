import winsound, time, random

techniques = ["jab.wav", "cross.wav", "leadhook.wav", "leaduppercut.wav", "leadelbow.wav", "rearelbow.wav"]
allhits = len(techniques)-1
numberofcombos = 5
#winsound.PlaySound(startbell.wav, winsound.SND_FILENAME)
for hit in range(numberofcombos):
    combolength = random.randint(1, 4)
    for bam in range(combolength):
        num = random.randint(0, allhits)
        print(techniques[num])
        #winsound.PlaySound(techniques[allhits], winsound.SND_FILENAME)
    print("    pause")
    time.sleep(1)

#winsound.PlaySound(startbell.wav, winsound.SND_FILENAME)

#jab.wav
#cross.wav
#leadhook.wav
#leaduppercut.wav
#leadelbow.wav
#rearelbow.wav
#startbell.wav
