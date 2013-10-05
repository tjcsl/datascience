lines = open('iplist.txt').read().splitlines()

ipmap = []
for line in lines:
    line = line.split('/')
    line = [line[0]] + line[1].split()
    ipmap.append({'start':line[0],'mask':line[1],'ip':line[2]})

def conv(line):
    mask = pow(2,32-line[

ipmap = map(conv, ipmap)
