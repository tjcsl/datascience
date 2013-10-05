
words = open('46883com.lwr').read().splitlines()

ana = {}

def a(word):
    index = "".join(sorted(word,key=lambda w:ord(w)))
    if index not in ana.keys():
        ana[index] = 1
    else:
        ana[index]+=1

for word in words:
    a(word)
print(ana)
a = max(ana.keys())
print("%s: %s" % (a, ana[a]))
