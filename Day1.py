from enum import Enum
class Direction(Enum):
    N = 1
    E = 2
    S = 3
    W = 4

x = 0
y = 0
r = Direction.N
found_it = False

file = open('steps.txt', 'r')
coordinates = file.read()

coordinates_list = coordinates.split(",")
location_list = [0, 0]

for coordinate in coordinates_list:
    #if (found_it):
     #   break
    coordinate = coordinate.strip()
    direction = coordinate[:1]
    stepsStr = coordinate[1:]
    steps = int(coordinate[1:])
    print ("Direction = " + direction)
    print ("Steps = " + stepsStr)
    print ("r = " + str(r))
    
    if (direction == 'L' and r == Direction.N):
        x_steps = -1
        y_steps = 0
        r=Direction.W
    elif (direction == 'L' and r == Direction.E):
        x_steps = 0
        y_steps = 1
        r=Direction.N
    elif (direction == 'L' and r == Direction.S):
        x_steps = 1
        y_steps = 0
        r=Direction.E
    elif (direction == 'L' and r == Direction.W):
        x_steps = 0
        y_steps = -1
        r=Direction.S
    elif (direction == 'R' and r == Direction.N):
        x_steps = 1
        y_steps = 0
        r=Direction.E
    elif (direction == 'R' and r == Direction.E):
        x_steps = 0
        y_steps = -1
        r=Direction.S
    elif (direction == 'R' and r == Direction.S):
        x_steps = -1
        y_steps = 0
        r=Direction.W
    elif (direction == 'R' and r == Direction.W):
        x_steps = 0
        y_steps = 1
        r=Direction.N
    
    a = 0
    while (a < steps):
        a += 1
        x += x_steps
        y += y_steps
        if [x, y] in location_list:
            print("x_second = " + str(x) + " y_second = " + str(y))
            found_it = True
        location_list.append([x, y])
        
    print ("x = " + str(x))
    print ("y = " + str(y))