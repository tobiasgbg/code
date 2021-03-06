curr_pos = 5

file = open('Day2Input.txt', 'r')
coordinates = file.read()

coordinates_list = coordinates.split('\n')

for coordinate in coordinates_list:
    position = 0
    while (position < len(coordinate)):
        direction = coordinate[position]
        position += 1
        
        if (curr_pos == 1 and direction == 'L'):
            curr_pos = 1
        elif (curr_pos == 1 and direction == 'U'):
            curr_pos = 1
        elif (curr_pos == 1 and direction == 'R'):
            curr_pos = 1
        elif (curr_pos == 1 and direction == 'D'):
            curr_pos = 3                               
        elif (curr_pos == 2 and direction == 'L'):
            curr_pos = 2
        elif (curr_pos == 2 and direction == 'U'):
            curr_pos = 2
        elif (curr_pos == 2 and direction == 'R'):
            curr_pos = 3
        elif (curr_pos == 2 and direction == 'D'):
            curr_pos = 6
        elif (curr_pos == 3 and direction == 'L'):
            curr_pos = 2
        elif (curr_pos == 3 and direction == 'U'):
            curr_pos = 1
        elif (curr_pos == 3 and direction == 'R'):
            curr_pos = 4
        elif (curr_pos == 3 and direction == 'D'):
            curr_pos = 7
        elif (curr_pos == 4 and direction == 'L'):
            curr_pos = 3
        elif (curr_pos == 4 and direction == 'U'):
            curr_pos = 4
        elif (curr_pos == 4 and direction == 'R'):
            curr_pos = 4
        elif (curr_pos == 4 and direction == 'D'):
            curr_pos = 8   
        elif (curr_pos == 5 and direction == 'L'):
            curr_pos = 5
        elif (curr_pos == 5 and direction == 'U'):
            curr_pos = 5
        elif (curr_pos == 5 and direction == 'R'):
            curr_pos = 6
        elif (curr_pos == 5 and direction == 'D'):
            curr_pos = 5         
        elif (curr_pos == 6 and direction == 'L'):
            curr_pos = 5
        elif (curr_pos == 6 and direction == 'U'):
            curr_pos = 2
        elif (curr_pos == 6 and direction == 'R'):
            curr_pos = 7
        elif (curr_pos == 6 and direction == 'D'):
            curr_pos = 'A'      
        elif (curr_pos == 7 and direction == 'L'):
            curr_pos = 6
        elif (curr_pos == 7 and direction == 'U'):
            curr_pos = 3
        elif (curr_pos == 7 and direction == 'R'):
            curr_pos = 8
        elif (curr_pos == 7 and direction == 'D'):
            curr_pos = 'B'   
        elif (curr_pos == 8 and direction == 'L'):
            curr_pos = 7
        elif (curr_pos == 8 and direction == 'U'):
            curr_pos = 4
        elif (curr_pos == 8 and direction == 'R'):
            curr_pos = 9
        elif (curr_pos == 8 and direction == 'D'):
            curr_pos = 'C'  
        elif (curr_pos == 9 and direction == 'L'):
            curr_pos = 8
        elif (curr_pos == 9 and direction == 'U'):
            curr_pos = 9
        elif (curr_pos == 9 and direction == 'R'):
            curr_pos = 9
        elif (curr_pos == 9 and direction == 'D'):
            curr_pos = 9
        elif (curr_pos == 'A' and direction == 'L'):
            curr_pos = 'A'
        elif (curr_pos == 'A' and direction == 'U'):
            curr_pos = 6
        elif (curr_pos == 'A' and direction == 'R'):
            curr_pos = 'B'
        elif (curr_pos == 'A' and direction == 'D'):
            curr_pos = 'A'    
        elif (curr_pos == 'B' and direction == 'L'):
            curr_pos = 'A'
        elif (curr_pos == 'B' and direction == 'U'):
            curr_pos = 7
        elif (curr_pos == 'B' and direction == 'R'):
            curr_pos = 'C'
        elif (curr_pos == 'B' and direction == 'D'):
            curr_pos = 'D'   
        elif (curr_pos == 'C' and direction == 'L'):
            curr_pos = 'B'
        elif (curr_pos == 'C' and direction == 'U'):
            curr_pos = 8
        elif (curr_pos == 'C' and direction == 'R'):
            curr_pos = 'C'
        elif (curr_pos == 'C' and direction == 'D'):
            curr_pos = 'C'      
        elif (curr_pos == 'D' and direction == 'L'):
            curr_pos = 'D'
        elif (curr_pos == 'D' and direction == 'U'):
            curr_pos = 'B'
        elif (curr_pos == 'D' and direction == 'R'):
            curr_pos = 'D'
        elif (curr_pos == 'D' and direction == 'D'):
            curr_pos = 'D'                                                                        
    print ("Final position = " + str(curr_pos))