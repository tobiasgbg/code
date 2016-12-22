import hashlib
import re
import logging

def stretch(hash, repeat):
    result = hash
    for i in range(0, repeat):
        result = get_hash(result)

    #print ('hash: ' + result)
    return result

def get_hash(hash):
    s = hash
    s = s.encode()
    md_5 = hashlib.md5(s)
    result = md_5.hexdigest()
    return result

def is_key(salt, index, steps, repeat, chars):
    for i in range(index, index + steps):
        hash = stretch(salt + str(i), 2017)

        regex = r"([" + chars + r"])\1{" + str(repeat - 1) + "}"

        m = re.search(regex, hash)

        #logging.debug('start index: ' + str(i) + ' steps: ' + str(steps))
        #logging.debug('index: ' + str(i))
        #logging.debug (hash)
        #logging.debug("--------------match : ")

        if m:
            if (steps > 1):
                return True

            return is_key(salt, i + 1, 1000, 5, m.group(0)[0])

    return False

salt = 'ahsbgdzn'
index = 0
keys = []
num_keys = 64
chars = '0-9a-zA-Z'
logging.basicConfig(filename='log.txt',level=logging.DEBUG)

while (len(keys) < num_keys):
    if (is_key(salt, index, 1, 3, chars)):
        keys.append(hash)
        print ('keys found: ' + str(len(keys)))
    index += 1
print ('answer: ' + str(index - 1))