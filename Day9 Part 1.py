file = open('Day9Input.txt', 'r')
input_file = file.read()

result = ''
index = 0
marker = ''
record_marker = False
original_no_tokens = len(input_file)
tokens_traversed = 0

while tokens_traversed < original_no_tokens:
    #print ('original no tokens:' + str(original_no_tokens))
    #print ('index: ' + str(index))
    #print ('tokens_traversed: ' + str(tokens_traversed))
    #print ('marker list: ' + marker)
    #print ('record marker: ' + str(record_marker))
    #print ('result: ' + result)
    
    token = input_file[index]
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
        #print ('marker list: ' + str(marker_list))
        #print ('number tokens: ' + str(number_tokens))
        #print ('number repeat: ' + str(number_repeat))
        #print ('list to repeat: ' + input_file[index+1:index+number_tokens+1])
        result += input_file[index+1:index+number_tokens+1] * number_repeat
        index += number_tokens + 1
        tokens_traversed += number_tokens + 1
        marker = ''
        continue
    
    if (record_marker):
        marker += token
    else:
        result += token
    
    index += 1
    tokens_traversed += 1

#print (result)
print (len(result))