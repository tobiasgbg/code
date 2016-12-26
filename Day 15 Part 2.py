import re

file = open('Day15Input.txt', 'r')
file = file.read()
rows = file.split('\n')

discStartPositions = []
discCurrentPositions = []
discSizes = []

for index in range(0, len(rows)):
    s = re.findall('Disc #(\d*) has (\d*) positions; at time=(\d*), it is at position (\d*).', rows[index])
    discSizes.append(s[0][1])
    discCurrentPositions.append(s[0][3])
    discStartPositions.append(s[0][3])

ballPassed = False
startTime = 0
noDiscs = len(discStartPositions)

while (not ballPassed):
    ballPassed = True
    offset = 0
    for disc in range(0, noDiscs):
        discCurrentPositions[disc] = discStartPositions[disc]

    for disc in range(0, noDiscs):
        if ((int(discCurrentPositions[disc]) + startTime + offset) % int(discSizes[disc]) != 0):
            ballPassed = False
            break
        offset += 1

    if (ballPassed):
        break
    startTime += 1

print ('Ball passed at start time ' + str(startTime - 1) + '.')