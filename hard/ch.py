d = open('challenge_file', 'rb').read()
import string
ips = [str(ord(a)) for a in d if a in string.ascii_letters]
#ips = [str(ord(c)) for c in d if ord(c) > 31 and ord(c) < 127]

for x in range(0,len(ips),4):
    print('.'.join(ips[x:x+4]))
