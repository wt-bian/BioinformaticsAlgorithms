def score_motif(motifs):
    for i in range(len(motifs[0])):
        temp = {}
        for j in range(len(motifs)):
            if motifs[j][i] in temp.keys():
                temp[motifs[j][i]] += 1
            else:
                temp[motifs[j][i]] = 1
        max_temp = sorted(temp, key=temp.get)[-1]
        score = 0
        for i in temp.keys():
            if i != max_temp:
                score += temp[i]
    return i


import math

print math.log(4,2)

a = [[0.2,0.1,0,0.7],[0.2,0.6,0,0.2],[0,0,1,0],[0,0,1,0],[0,0,0.9,0.1],
     [0,0,0.9,0.1],[0.9,0,0.1,0],[0.1,0.4,0,0.5],[0.1,0.1,0,0.8],
     [0.1,0.2,0,0.7],[0.3,0.4,0,0.3],[0,0.6,0,0.4]]
score = []
for i in a:
    temp = 0
    for j in i:
        if j == 0:
            continue
        else:
            temp += j*math.log(j,2)
    score.append(-temp)

for i in score:
    print i
