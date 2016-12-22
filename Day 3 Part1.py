def is_triangle ( sides ):
    print (sides)
    a = int(sides[0])
    b = int(sides[1])
    c = int(sides[2])
    if ( a + b  <= c):
        return False
    if ( b + c  <= a):
        return False
    if ( a + c  <= b):
        return False
    return True

possible_Triangles = 0

file = open('Day3Input.txt', 'r')
triangles_file = file.read()

rows_list = triangles_file.split('\n')

triangles = 0
index = 0
triangle_1 = []
triangle_2 = []
triangle_3 = []
for row in rows_list:
    array = row.split()
    triangle_1.append(int(array[0]))
    triangle_2.append(int(array[1]))
    triangle_3.append(int(array[2]))
    
    index += 1;
    
    if (index == 3):
        index = 0
        
        if (is_triangle(triangle_1)):
            triangles += 1;
        if (is_triangle(triangle_2)):
            triangles += 1;
        if (is_triangle(triangle_3)):
            triangles += 1;
        
        triangle_1 = []
        triangle_2 = []
        triangle_3 = []

print (triangles)