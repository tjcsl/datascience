d = open('challenge_file', 'rb').read()
import string
#ips = [str(ord(a)) for a in d if a in string.ascii_letters]
ips = [str(int(x,16)) for x in '8F FB DA EA F0 D0 A2 92'.split()]
#ips = [str(ord(c)) for c in d if ord(c) > 31 and ord(c) < 127]
print(ips)

for x in range(0,len(ips),4):
    print('.'.join(ips[x:x+4]))
