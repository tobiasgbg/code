from audioop import reverse
from builtins import reversed
def SupportsTLS ( ip ):

    ip_list = list(ip)
    insideBrackets = False
    supportsTLS = False
    index = 0
    while index < len(ip):
        
        if (ip_list[index] == '['):
            insideBrackets = True
        elif (ip_list[index] == ']'):
            insideBrackets = False

        checkOk = ip_list[index:index+2] == list(reversed(ip_list[index+2:index+4])) and ip_list[index:index+1] != ip_list[index+1:index+2]
        
        if (insideBrackets and checkOk):
            return False
        elif (not insideBrackets and checkOk):
            print (ip)
            print (ip_list[index:index+2])
            print (list(reversed(ip_list[index+2:index+4])))
            print ('--')
            supportsTLS = True
        
        index += 1

    return supportsTLS

file = open('Ips.txt', 'r')
ips_file = file.read()

ips_list = ips_file.split('\n')

NoIpsSupportsTLS = 0

for ip in ips_list:
    if (SupportsTLS(ip)):
        NoIpsSupportsTLS += 1 
  

print ("NoIpsSupportsTLS: " + str(NoIpsSupportsTLS))