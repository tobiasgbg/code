def get_decompressed_size(string):

    index = 0
    marker = ''
    record_marker = False
    original_no_tokens = len(string)
    tokens_traversed = 0
    decompressed_size = 0
    
    print ('--------------------check :' + string)
    
    while tokens_traversed < original_no_tokens:
        
        token = string[index]
        
        print ('original no tokens:' + str(original_no_tokens))
        print ('index: ' + str(index))
        print ('tokens_traversed: ' + str(tokens_traversed))
        print ('marker list: ' + marker)
        print ('record marker: ' + str(record_marker))
        print ('token: ' + token)
        print ('---- ')
        
        if (token == '('):
            record_marker = True
            tokens_traversed += 1
            index += 1
            continue
        elif (token == ')'):
            record_marker = False
            marker_list = marker.split('x')
            number_tokens = int(marker_list[0])
            number_repeat = int(marker_list[1])
            print ('marker list: ' + str(marker_list))
            print ('number tokens: ' + str(number_tokens))
            print ('number repeat: ' + str(number_repeat))
            print ('list to repeat: ' + string[index+1:index+number_tokens+1])
            decompressed_size += number_repeat * get_decompressed_size(string[index+1:index+number_tokens+1])
            index += number_tokens + 1
            tokens_traversed += number_tokens + 1
            marker = ''
            continue
        
        if (record_marker):
            marker += token
        else:
            decompressed_size += 1
        
        index += 1
        tokens_traversed += 1
        
    return decompressed_size

file = open('Day9Input.txt', 'r')
input_file = file.read()

decompressed_size = get_decompressed_size(input_file)

#print (result)
print ('decompressed_size: ' + str(decompressed_size))