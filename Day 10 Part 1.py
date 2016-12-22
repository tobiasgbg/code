from enum import Enum
import re
import logging

def getBot(bot, bots):
    for object in bots:
        if (object.number == bot):
            return object

    #No bot found, create new one
    newBot = Bot(bot)
    bots.append(newBot)

    return newBot

def getOutput(output, outputs):
    for object in outputs:
        if (object.number == output):
            return object

    #No output found, create new one
    newOutput = Output(output)
    outputs.append(newOutput)

    return newOutput

def giveValue(str, bots, outputs):
    s = re.findall('bot (\d*) gives \D* to (\D*) (\d*) and \D* to (\D*) (\d*)', str)
    bot = s[0][0]
    target1Type = s[0][1]
    target1Name = s[0][2]
    target2Type = s[0][3]
    target2Name = s[0][4]
    botObj = getBot(bot, bots)
    botObj.addInstruction(Instruction(target1Type, target1Name, target2Type, target2Name))

def addValue(str, bots, outputs):
    s = re.findall('value (\d*) goes to bot (\d*)', str)
    value = s[0][0]
    bot = s[0][1]
    botObj = getBot(bot, bots)

    botObj.takeChip(value, bots, outputs)

class Position(Enum):
    Lower = 1
    Higher = 2

class TargetType(Enum):
    Output = 'output'
    Bot = 'bot'

class Instruction:

    def __init__(self, lowerTargetType, lowerTargetName, higherTargetType, higherTargetName):
        self.lowerTargetType = TargetType(lowerTargetType)
        self.lowerTargetName = lowerTargetName
        self.higherTargetType = TargetType(higherTargetType)
        self.higherTargetName = higherTargetName

    def getLowerTargetType(self):
        return self.lowerTargetType

    def getLowerTargetName(self):
        return self.lowerTargetName

    def getHigherTargetType(self):
        return self.higherTargetType

    def getHigherTargetName(self):
        return self.higherTargetName

    def display(self):
        print ('Give lower to ' + str(self.lowerTargetType) + ' ' + str(self.lowerTargetName) + ' and higher to ' + str(self.higherTargetType) + ' ' + str(self.higherTargetName))

class Output:
    def __init__(self, number):
        self.number = number
        self.chip = None

    def display(self):
        print ("Chip : " + str(self.chip) +  ", Value: " + str(self.number))

    def takeChip(self, chip):
        self.chip = chip

class Bot:
    def __init__(self, number):
        self.number = number
        self.lower_value_chip = None
        self.higher_value_chip = None
        self.instructions = []

    def display(self):
        print ("Number : " + str(self.number) +  ", Lower value chip: " + str(self.lower_value_chip) +  ", Higher value chip: " + str(self.higher_value_chip))
        print ('Instructions:')
        for instruction in self.instructions:
            instruction.display()

    def takeChip(self, chip, bots, outputs):
        if (self.lower_value_chip == None):
            self.lower_value_chip = chip
        else:
            if (int(chip) >= int(self.lower_value_chip)):
                self.higher_value_chip = chip
            else:
                self.higher_value_chip = self.lower_value_chip
                self.lower_value_chip = chip

        logging.debug("Number : " + str(self.number) +  ", Lower value chip: " + str(self.lower_value_chip) +  ", Higher value chip: " + str(self.higher_value_chip) + '\n')

        print ("Number : " + str(self.number) +  ", Lower value chip: " + str(self.lower_value_chip) +  ", Higher value chip: " + str(self.higher_value_chip))

        if (self.lower_value_chip == "17" and self.higher_value_chip == "61"):
            print ("Bot responsible is: " + str(self.number))

    def getChip(self, position):
        if (position == Position.Lower):
            return self.lower_value_chip
        elif (position == Position.Higher):
            return self.higher_value_chip

    def giveChipToOutput(self, position, name, outputs):
        chip = self.getChip(position)
        outputObj = getOutput(name, outputs)
        outputObj.takeChip(chip)

    def giveChipToBot(self, position, name, bots, outputs):
        chip = self.getChip(position)
        botObj = getBot(name, bots)
        botObj.takeChip(chip, bots, outputs)

    def addInstruction(self, instruction):
        self.instructions.append(instruction)

    def giveChip(self, position, targetType, targetName, bots, outputs):
        if (targetType == TargetType.Output):
            self.giveChipToOutput(position, targetName, outputs)
        elif (targetType == TargetType.Bot):
            self.giveChipToBot(position, targetName, bots, outputs)

    def executeInstruction(self, bots, outputs):

        if (len(self.instructions) == 0):
            return

        if (self.lower_value_chip == None or self.higher_value_chip == None):
            return

        instruction = self.instructions.pop()
        
        str(instruction.display())
        
        self.giveChip(Position.Lower, instruction.getLowerTargetType(), instruction.getLowerTargetName(), bots, outputs)
        self.lower_value_chip = None
        self.giveChip(Position.Higher, instruction.getHigherTargetType(), instruction.getHigherTargetName(), bots, outputs)
        self.higher_value_chip = None

def executeInstructions(bots, outputs):
    for bot in bots:
        bot.executeInstruction(bots, outputs)

logging.basicConfig(filename='log.txt',level=logging.DEBUG)

file = open('Day10Input.txt', 'r')
input_file = file.read()

input_list = input_file.split('\n')

outputs = []
bots = []

for line in input_list:
    #print ('line: ' + line)
    if (line.startswith('value')):
        addValue(line, bots, outputs)
    elif (line.startswith('bot')):
        giveValue(line, bots, outputs)
        
    executeInstructions(bots, outputs)

index = 0
while index < 1000:
    index += 1
    executeInstructions(bots, outputs)

sum = 1    
for output in outputs:
    if (output.number == '0' or output.number == '1' or output.number == '2'):
        sum = sum * int(output.chip)
    output.display()
    
print ("Sum is: " + str(sum))

