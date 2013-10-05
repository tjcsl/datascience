

lines = open('scores.csv').read().splitlines()
scores = {}
for line in lines:
    line = line.split(',')
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

