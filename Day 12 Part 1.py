import time

def print_registers():
    print ('register_a= ' + str(register_a))
    print ('register_b= ' +  str(register_b))
    print ('register_c= ' +  str(register_c))
    print ('register_d= ' +  str(register_d))
    print ('\n')

file = open('Day12Input.txt', 'r')
input_file = file.read()

input_list = input_file.split('\n')

instructions = []

for instruction in input_list:
    instructions.append(instruction)

register_a = 0
register_b = 0
register_c = 1
register_d = 0

index = 0
while (index < len(instructions)):
    instruction = instructions[index]
    #print (instruction)
    if (instruction[0:3] == 'cpy'):
        values = instruction.split()
        value = 0
        if (values[1].isdigit()):
            value = int(values[1])
        else:
            if (values[1] == 'a'):
                value = register_a
            elif (values[1] == 'b'):
                value = register_b
            elif (values[1] == 'c'):
                value = register_c
            elif (values[1] == 'd'):
                value = register_d
        if (values[2] == 'a'):
            register_a = int(value)
        elif (values[2] == 'b'):
            register_b = int(value)
        elif (values[2] == 'c'):
            register_c = int(value)
        elif (values[2] == 'd'):
            register_d = int(value)
        index += 1
    elif (instruction[0:3] == 'inc'):
        values = instruction.split()
        if (values[1] == 'a'):
            register_a += 1
        elif (values[1] == 'b'):
            register_b += 1
        elif (values[1] == 'c'):
            register_c += 1
        elif (values[1] == 'd'):
            register_d += 1
        index += 1
    elif (instruction[0:3] == 'dec'):
        values = instruction.split()
        if (values[1] == 'a'):
            register_a -= 1
        elif (values[1] == 'b'):
            register_b -= 1
        elif (values[1] == 'c'):
            register_c -= 1
        elif (values[1] == 'd'):
            register_d -= 1
        index += 1
    elif (instruction[0:3] == 'jnz'):
        values = instruction.split()
        value = 0
        if (values[1].isdigit()):
            value = int(values[1])
        else:
            if (values[1] == 'a'):
                value = register_a
            elif (values[1] == 'b'):
                value = register_b
            elif (values[1] == 'c'):
                value = register_c
            elif (values[1] == 'd'):
                value = register_d

        if (value != 0):
            index += int(values[2])
        else:
            index += 1

print_registers()