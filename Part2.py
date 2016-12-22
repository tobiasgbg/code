import hashlib

def IsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

string = "reyedfim"
i = 0
m = ''
s = ''
password = list('________')
while (True):
    s = (string + str(i))
    s = s.encode()
    md_5 = hashlib.md5(s) 
    m = md_5.hexdigest()

    if (str(m[:5]) == "00000"):
        pos = m[5];
        if (IsInt(pos) and int(pos) < 8 and password[int(pos)] == '_'):
                print ('Found: ' + m)
                password[int(pos)] = m[6]
    
    if (not '_' in password):
        break
    
    i += 1

print (''.join(password))