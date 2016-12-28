no_elves = 3012210

elves = [0 for x in range(no_elves)]
for x in range(0, no_elves):
    elves[x] = x + 1

while (len(elves) > 1):

    elf = 1

    len_new_list = int(len(elves) / 2)
    new_list = [0 for x in range(len_new_list)]

    index = 0
    step = 2
    if ((len(elves) % 2) == 0):
        index = 0
        step = 0

    #print ('list: ' + str(elves))
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # [3, 5, 7, 9, 11]
    # [7, 11]
    while (index < len_new_list):
        #print ('index: ' + str(index))
        #print ('step: ' + str(index+step))
        new_list[index] = elves[index+step]
        elf += 1
        step += 1
        index += 1

    if (len_new_list <= 3 and (len_new_list % 2) != 0):
        new_list.reverse()
        new_list = [new_list[0]]
        elves = new_list
        break
    elif (len_new_list <= 3 and (len_new_list % 2) == 0):
        new_list = [new_list[0]]
        elves = new_list
        break
    
    elves = new_list
    
print(elves)