import re

def getDisc(disc, discs):
    result = None
    for object in discs:
        if (object.number == str(disc)):
            result = object

    return result

class Disc:
    def __init__(self, number, noPositions, time, startPosition):
        self.number = number
        self.noPositions = noPositions
        self.time = time
        self.startPosition = startPosition
        self.position = self.startPosition

    def rotate(self):
        self.position = int(int(self.position) + 1) % int(self.noPositions)

    def display(self):
        print ('------')
        print ('Number: ' + str(self.number))
        print ('NoPositions: ' + str(self.noPositions))
        print ('Time: ' + str(self.time))
        print ('Position: ' + str(self.position))
    
    def reset(self):
        self.position = self.startPosition

def create_disc(discs, row):
    # Disc #1 has 5 positions; at time=0, it is at position 4.
    s = re.findall('Disc #(\d*) has (\d*) positions; at time=(\d*), it is at position (\d*).', row)
    disc = s[0][0]
    noPositions = s[0][1]
    time = s[0][2]
    position = s[0][3]

    discs.append(Disc(disc, noPositions, time, position))

file = open('Day15Input.txt', 'r')
file = file.read()

rows = file.split('\n')

discs = []

for row in rows:
    create_disc(discs, row)
    print(row)

time = 0
ballPosition = 0
ballDropped = False
ballPassed = False
ballBounced = False
startTime = 121834

while (True):
    #print ('Check start time: ' + str(startTime))
    time = 0
    ballPosition = 0
    ballDropped = False
    ballBounced = False
    for disc in discs:
        disc.reset()
    while (ballPosition < len(discs)):

        if (not ballDropped and time == startTime):
            ballDropped = True

        if (ballDropped):
            ballPosition += 1

            disc = getDisc(ballPosition, discs)
            if (disc.position != 0):
                ballBounced = True
                #print ('ball bounced')
                break

        for disc in discs:
            disc.rotate()
        time += 1

    if (not ballBounced):
        print ('Ball passed all discs!')
        break

    startTime += 1

print ('Ball passed at start time ' + str(startTime - 1) + '.')