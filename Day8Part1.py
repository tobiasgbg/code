import copy

def turn_on_rect(list_in, rect):
    rect_list = rect.split('x')
    row_size = int(rect_list[0])
    col_size = int(rect_list[1])
    
    list_out = copy.deepcopy(list_in)
    
    for row in range(0, row_size):
        for col in range(0, col_size):
            list_out[col][row] = 1
            
    return list_out

def print_display(display_list):

    result = ''

    for row in display_list:
        result += '\n' + str(row)
        
    return result

def move_row_right(list_in, row_number, steps_right, width, height):
    list_out = copy.deepcopy(list_in)
    
    print("list_out: " + print_display(list_out))
    
    for element in range(0, width-1):
        if element >= steps_right:
            list_out[row_number][element] = list_in[row_number][element-steps_right]
        else:
            list_out[row_number][element] = list_in[row_number][width-steps_right+element]

    return list_out

def move_col_down(list_in, col_number, steps_down, width, height):

    list_out = copy.deepcopy(list_in)

    #print ('Move col down')
    #print ('col: ' + str(col_number))
    #print ('steps_down: ' + str(steps_down))
    
    #print("before move: " + print_display(list_in))
    #print("0 1: " + str(list_in[0][1]))

    for element in range(0, height):
        #print('setting---- ' + str(element) + ' ' + str(col_number))
        if element >= steps_down:
            #print(' to ' + str(element-steps_down) + ' ' + str(col_number) + ' value: ' + str(list_in[element-steps_down][col_number]))
            list_out[element][col_number] = list_in[element-steps_down][col_number]
        else:
            #print(' to ' + str(height-steps_down) + ' ' + str(col_number) + ' value: ' + str(list_in[height-steps_down][col_number]))
            list_out[element][col_number] = list_in[height-steps_down+element][col_number]

    #print("after move: " + print_display(list_out))

    return list_out

file = open('Day8Input.txt', 'r')
input_file = file.read()

input_list = input_file.split('\n')
display_width = 50
display_height = 6

display_list = [[0 for x in range(display_width)] for y in range(display_height)]

for row in input_list:
    row_list = row.split()
    
    if (row_list[0] == "rect"):
        display_list = turn_on_rect(display_list, row_list[1])
    elif (row_list[1] == "row"):
        row_number = int(row_list[2].split('=')[1])
        steps_right = int(row_list[4])
        display_list = move_row_right(display_list, row_number, steps_right, display_width, display_height)
    elif (row_list[1] == "column"):
        col_number = int(row_list[2].split('=')[1])
        steps_down = int(row_list[4])
        display_list = move_col_down(display_list, col_number, steps_down, display_width, display_height)

number_one = 0

for row in range(0, display_width):
    for col in range(0, display_height):
        if (display_list[col][row] == 1):
            number_one += 1

print("after move: " + print_display(display_list))
print(str(number_one))