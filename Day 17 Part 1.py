import hashlib
import random
import copy

def is_door(direction, current_pos):
    if (current_pos[0] == 0 and direction == 'L'):
        return False
    elif (current_pos[1] == 0 and direction == 'U'):
        return False
    elif (current_pos[0] == 3 and direction == 'R'):
        return False
    elif (current_pos[1] == 3 and direction == 'D'):
        return False

    return True

def is_open(direction, directions, hash):
    return hash[directions.index(direction)] in 'bcdef'

def get_hash(string):
    s = string
    s = s.encode()
    md_5 = hashlib.md5(s)
    result = md_5.hexdigest()
    return result

input = 'ulqzkmiv'
path = ''
start_pos = [0,0]
goal_pos = [3,3]
current_pos = [0,0]
directions = ['U', 'D', 'L', 'R']
shortest_path = ''
is_stuck = False

for i in range(0, 100000):
    is_stuck = False
    current_pos = [0,0]
    path = ''
    while (current_pos != goal_pos):
        hash = get_hash(input + path)

        possible_moves = []

        for direction in directions:
            if (is_door(direction, current_pos) and is_open(direction, directions, hash)):
                possible_moves.append(direction)
    

        if (len(possible_moves) == 0):
            is_stuck = True
            break

        next = random.choice(possible_moves)
        path += next

        if (next == 'L'):
            current_pos[0] -= 1
        elif (next == 'R'):
            current_pos[0] += 1
        elif (next == 'D'):
            current_pos[1] += 1
        elif (next == 'U'):
            current_pos[1] -= 1

    if (not is_stuck and len(path) != 0 and current_pos == goal_pos):
        if (len(shortest_path) == 0 or len(path) < len(shortest_path)):
            shortest_path = copy.deepcopy(path)
            print ('shortest path: ' + shortest_path)

print ('done')
print ('shortest path: ' + shortest_path)