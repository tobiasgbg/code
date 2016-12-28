def is_trap(position, previous_row):
    if (position == 0):
        left_is_trap = False
    else:
        left_is_trap = (previous_row[position-1] == '^')

    if (position == (len(previous_row) - 1)):
        right_is_trap = False
    else:
        right_is_trap = (previous_row[position+1] == '^')

    center_is_trap = (previous_row[position] == '^')
    
    if (left_is_trap and center_is_trap and not right_is_trap):
        return True
    elif (center_is_trap and right_is_trap and not left_is_trap):
        return True
    elif (left_is_trap and not center_is_trap and not right_is_trap):
        return True
    elif (right_is_trap and not center_is_trap and not left_is_trap):
        return True    
    else:
        return False

file = open('Day18Input.txt', 'r')
file = file.read()
no_rows = 400000

array = []
array.append(file)

no_safe_tiles = 0
for index in range(0, no_rows - 1):
    next_row = ''
    for position in range(0, len(file)):
        if (is_trap(position, array[index])):
            next_row += '^'
        else:
            next_row += '.'
            no_safe_tiles += 1
    array.append(next_row)

for character in file:
    if (character == '.'):
        no_safe_tiles += 1

print ('number of safe tiles: ' + str(no_safe_tiles))