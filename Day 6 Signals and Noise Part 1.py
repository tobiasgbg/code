def get_code ( signals ):

    code = ''

    letters_list = []
    occurences_list = []

    i = 0
    
    while (i < 8):
        letters_list = []
        occurences_list = []
    
        for signal in signals:
            letter = signal[i]
            if (letter in letters_list):
                occurences_list[letters_list.index(letter)] += 1
            else:
                letters_list.append(letter)
                occurences_list.append(1)

        i += 1
        max_val = min(occurences_list)
        code += letters_list[occurences_list.index(max_val)]
        print (code)
    
    return code            
        
file = open('Signals.txt', 'r')
signals_file = file.read()

signals_list = signals_file.split('\n')

code = get_code(signals_list)

print (code)