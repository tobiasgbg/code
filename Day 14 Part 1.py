import hashlib
import re
def is_key(salt, index, steps, repeat, chars):
    for i in range(index, index + steps):
        s = salt + str(i)
        s = s.encode()
        md_5 = hashlib.md5(s)
        hash = md_5.hexdigest()

        regex = r"([" + chars + r"])\1{" + str(repeat - 1) + "}"

        m = re.search(regex, hash)

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

while (len(keys) < num_keys):
    if (is_key(salt, index, 1, 3, chars)):
        keys.append(hash)
    index += 1
print ('answer: ' + str(index - 1))