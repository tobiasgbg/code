from audioop import reverse
from builtins import reversed
def SupportsTLS ( ip ):

    ip_list = list(ip)
    insideBrackets = False
    aba = False
    bab = False
    index = 0
    while index < len(ip) - 2:
        
        if (ip_list[index] == '['):
            insideBrackets = True
        elif (ip_list[index] == ']'):
            insideBrackets = False
            
        aba_str = ip_list[index:index+3]

        aba = not insideBrackets and aba_str[0] == aba_str[2] and aba_str[0] != aba_str[1]
        
        if (aba and has_bab(ip_list, list(aba_str))):
            return True
        
        index += 1

    return False

def has_bab ( ip_list, aba ):

    insideBrackets = False
    index = 0
    while index < len(ip_list) :
        
        bab = list(aba[1] + aba[0] + aba[1])
        possible_bab = ip_list[index:index+3]

        if (insideBrackets and bab == possible_bab):
            return True
        
        if (ip_list[index] == '['):
            insideBrackets = True
        elif (ip_list[index] == ']'):
            insideBrackets = False
        
        index += 1

    return False
    

file = open('Ips.txt', 'r')
ips_file = file.read()

ips_list = ips_file.split('\n')

NoIpsSupportsTLS = 0

for ip in ips_list:
    if (SupportsTLS(ip)):
        NoIpsSupportsTLS += 1 
    
  

print ("NoIpsSupportsTLS: " + str(NoIpsSupportsTLS))