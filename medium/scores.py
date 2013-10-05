

lines = open('scores.csv').read().splitlines()
scores = {}
teams = {}
for line in lines:
    line = line.split(',')
    if line[0] not in teams:
        teams[line[0]] = []
    if line[2] not in teams:
        teams[line[2]] = []
    teams[line[0]].append('w/' + line[1] + '/' + line[3])
    teams[line[2]].append('l/' + line[3] + '/' + line[1])
    scores[line[0]] = {'hscore': int(line[1]), 'other': line[2], 'lscore': int(line[3])}

rdiff = {x:0 for x in scores.keys()}
winp = {x:{'win':0,'lose':0} for x in scores.keys()}

for name,team in scores.items():
    rdiff[name] += team['hscore'] - team['lscore']
    winp[name]['win']+=1
    winp[team['other']]['lose']+=1

wins = []

for x in winp.values():
    total = x['win'] + x['lose']
    wins.append(float(x['win'])/total)

print('best dif: %s' % max(rdiff.values()))
print('worst dif: %s' % min(rdiff.values()))
print('best winp: %0.5f' % max(wins))
print('worst winp: %0.5f' % min(wins))

fteams = {}
for i in teams.keys():
    wins = 0
    losses = 0
    rs = 0
    ra = 0
    for j in teams[i]:
        k = j.split('/')
        if k[0] == 'w':
            wins += 1
            rs += int(k[1])
            ra += int(k[2])
        else:
            losses += 1
            rs += int(k[2])
            ra += int(k[1])
    fteams[i] = [wins, losses, rs, ra]
for i in fteams:
    print(i + str(float(fteams[i][0]) / fteams[i][1]) + ' ' + str(float(fteams[i][2]) / fteams[i][3]))
