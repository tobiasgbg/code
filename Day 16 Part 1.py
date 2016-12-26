import copy
from audioop import reverse
from builtins import reversed

def generate_data(data):
    a = data
    b = copy.deepcopy(a)
    b = ''.join(reversed(b))
    b = b.replace('1', '7')
    b = b.replace('0', '1')
    b = b.replace('7', '0')
    return a + '0' + b

def get_checksum(data):
    checksum = ''
    index = 0
    while (index < len(data) - 1):
        if data[index] == data[index + 1]:
            checksum += '1'
        else:
            checksum += '0'
        index += 2
    if len(checksum) % 2 == 0:
        return get_checksum(checksum)
    else:
        return checksum

size_to_fill = 35651584
input = '10111011111001111'
data = generate_data(input)
checksum = get_checksum(data)
while (len(data) < size_to_fill):
    data = generate_data(data)
    if (len(data) > size_to_fill):
        data = data[0:size_to_fill]
    checksum = get_checksum(data)
print ('checksum: ' + checksum)