import time

def is_sorted (list):
    #print ('Check sorted: ' + str(list))
    index = 0
    while index < len(list) - 1:
        if list[index] < list[index+1]:
            return False
        index += 1

    return True

def is_real_room ( letters, checksum ):

    letters_list = []
    occurences_list = []
    checksum_list = []
    max_list = []

    #print ("---------")
    #print (letters)

    for letter in letters:
        if (letter in letters_list):
            occurences_list[letters_list.index(letter)] += 1
        else:
            letters_list.append(letter)
            occurences_list.append(1)

    #print ("Letters list: " + str(letters_list))
    #print ("Occurence list: " + str(occurences_list))

    occurences_list_sorted = sorted(list(set(occurences_list)))

    #print (str(occurences_list_sorted))
    occurences_list_sorted.reverse()

    #print (str(occurences_list_sorted))
    for value_sort in occurences_list_sorted:
        index = 0
        max_list = []
        for value in occurences_list:
            if (value == value_sort):
                max_list.append(letters_list[index])
            index += 1
        #print ("Max list: " + str(max_list))
        max_list.sort()
        checksum_list.append(max_list)

    #print ("Checksum list: " + str(checksum_list))
    #print ("Real checksum: " + str(checksum))

    flat_list = [val for sublist in checksum_list for val in sublist]

    flat_list_string = ''.join(flat_list[:5])

    #print ("Flat list: " + flat_list_string)

    b = sorted(letters)

    #if (checksum == "erzkv"):
    if (not is_sorted(occurences_list_sorted)):
        print ('----------------NOT SORTED---------------------')
        print (letters)
        print ("Letters list: " + str(letters_list))
        print ("Occurence list: " + str(occurences_list))
        print ("Occurence list sorted: " + str(occurences_list_sorted))
        print ("Flat list: " + flat_list_string)
        print("Letters list sorted: " + str(b))
        print ("Real checksum: " + str(checksum))

    if (flat_list_string == checksum):
        return True
    else:
        return False

file = open('EncryptedRooms.txt', 'r')
rooms_file = file.read()

rooms_list = rooms_file.split('\n')

#print(len(rooms_list))

sector_id_sum = 0

for room in rooms_list:
    room_array = room.split('-')
    i = 0
    letter_str = ""
    while (i < len(room_array) - 1):
        letter_str += room_array[i]
        i += 1

    last_pos = len(room_array) - 1
    sector_array = room_array[last_pos].split('[')

    sector_id = int(sector_array[0])
    checksum = sector_array[1].replace(']', "")

    if (is_real_room(letter_str, checksum)):
        sector_id_sum += sector_id;

print (sector_id_sum)
    # letters id checksum
    #
