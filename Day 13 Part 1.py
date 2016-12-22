def search(x, y, grid):
    if grid[x][y] == 2:
        print ('found at %d,%d' % (x, y))
        return True
    elif grid[x][y] == 1:
        print ('wall at %d,%d' % (x, y))
        return False
    elif grid[x][y] == 3:
        print ('visited at %d,%d' % (x, y))
        return False
    
    print ('visiting %d,%d' % (x, y))
    # mark as visited
    grid[x][y] = 3

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(grid)-1 and search(x+1, y, grid))
        or (y > 0 and search(x, y-1, grid))
        or (x > 0 and search(x-1, y, grid))
        or (y < len(grid)-1 and search(x, y+1, grid))):
        return True

    return False

display_width = 50
display_height = 50

maze = [[0 for x in range(display_width)] for y in range(display_height)]

favorite_number = 1352
#favorite_number = 0

def print_display(display_list):

    result = ''

    for row in display_list:
        for item in row:
            result += str(item)
        result += '\n' 
        
    return result

def isWall (x, y, fav_num):
    sum = x*x + 3*x + 2*x*y + y + y*y
    sum += fav_num
    
    sum_bin = bin(sum)
    #print ('x, y = %d,%d' % (x, y))
    #print (str(sum))
    #print (str(sum_bin))
    
    number_one = 0
    for bit in sum_bin:
        if (bit == '1'):
            number_one += 1
    
    #print (str(number_one))
    
    if (number_one % 2 == 0):
        return False
    else:
        return True
    
for x in range(0, display_width):
    for y in range (0, display_height):
        if (isWall(x, y, favorite_number)):
            maze[y][x] = 1
        else:
            maze[y][x] = 0

print (print_display(maze))

goal_x = 31
goal_y = 39

maze[goal_y][goal_x] = 2

search(1,1, maze)

visited = 0
for x in range(0, display_height):
    for y in range (0, display_width):
        if (maze[x][y] == 3):
            visited += 1
            
print ("Numbers visited:" + str(visited) )
