import shutil
import os

FileLocation = "C:/Users/ReD-OrC/Documents/Paradox Interactive/Stellaris/save games/unitedempireofsol/gamestate"
cFileLocation = "C:/Users/ReD-OrC/Documents/Paradox Interactive/Stellaris/save games/unitedempireofsol/gamestatex"
repfileLocation = "C:/Users/ReD-OrC/Documents/Paradox Interactive/Stellaris/save games/unitedempireofsol/x"

primaryTarget = "\t\tportrait=\"human\"\n"
employmentCheck = "\t\tclass="
levelCheck = "\t\tlevel="
check1000 = "\t\tlevel=1000\n"
make1000 = "\t\tlevel=1000\n"

humans = 0
employed = 0
already1000 = 0
became1000 = 0
wiff = 0

shutil.copyfile(FileLocation, cFileLocation)

if os.path.exists(repfileLocation):
    os.remove(repfileLocation)
    print("Cleaned up")
else:
    print("Fresh Start")

with open(cFileLocation, "r+") as sf, open(repfileLocation, "a+") as ef:
    line = sf.readlines(-1)
    i = 0
    copyline = line[i]
    while i < len(line):
        if line[i] == primaryTarget:
            humans += 1
            if line[i+4][:8] == employmentCheck:
                employed += 1
                if line[i+5][:8] == levelCheck and line[i+5] == check1000:
                    ef.write(line[i])
                    already1000 += 1
                    i += 1
                elif line[i+5][:8] == levelCheck and line[i+5] != check1000:
                    ef.writelines(line[i])
                    ef.writelines(line[i+1])
                    ef.writelines(line[i+2])
                    ef.writelines(line[i+3])
                    ef.writelines(line[i+4])
                    ef.writelines(make1000)
                    became1000 += 1
                    i += 6
                elif line[i+6][:8] == levelCheck and line[i+6] == check1000:
                    ef.write(line[i])
                    already1000 += 1
                    i += 1
                elif line[i+6][:8] == levelCheck and line[i+6] != check1000:
                    ef.writelines(line[i])
                    ef.writelines(line[i+1])
                    ef.writelines(line[i+2])
                    ef.writelines(line[i+3])
                    ef.writelines(line[i+4])
                    ef.writelines(line[i+5])
                    ef.writelines(make1000)
                    became1000 += 1
                    i += 7
                else:
                    ef.writelines(line[i])
                    wiff += 1
                    i += 1
            else:
                ef.writelines(line[i])
                i += 1
        else:
            ef.writelines(line[i])
            i += 1

os.remove(FileLocation)
os.remove(cFileLocation)
os.rename(repfileLocation, FileLocation)

print("The number of human mentions: " + str(humans) + " but the number of \"real\" humans: " + str(employed))
print("There are " + str(already1000) + " old members of the upperhouses, and " + str(became1000) + " new members")
print("Let this be less than 20: " + str(wiff))
