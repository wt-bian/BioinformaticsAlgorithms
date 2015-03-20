weight = (57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186)
sample = '0 101 103 115 129 131 137 156 163 163 163 204 230 246 260 266 278 293 300 319 326 333 361 367 375 409 429 434 456 456 463 464 476 496 530 538 565 566 571 579 619 619 627 639 659 667 694 702 722 734 742 742 782 790 795 796 823 831 865 885 897 898 905 905 927 932 952 986 994 1000 1028 1035 1042 1061 1068 1083 1095 1101 1115 1131 1157 1198 1198 1198 1205 1224 1230 1232 1246 1258 1260 1361'.split(' ')
for i in xrange(len(sample)):
    sample[i] = int(sample[i])

oriAA = list()
for i in weight:
    if i in sample:
        oriAA.append(i)

List = oriAA
def expand(x, AA):
    temp = list('0')*len(List)*len(oriAA)
    k = 0
    for i in x:
        for j in AA:
            temp[k] = str(i) + '-' + str(j)
            k = k + 1
    return temp

def mass(x):
    temp =  list()
    y = x.split('-')
    for i in xrange(len(y)):
        y[i] = int(y[i])
    for i in range(len(y)):
        for j in range(len(y)):
            if j+i+1>range(len(y)):
                break
            temp.append(sum(y[j:j+i+1]))
    return set(temp)

for maxium in xrange(max(sample)/57):
    List = expand(List,oriAA)
    temp = list()
    for i in List:
        if not(mass(i).issubset(sample)):
            temp.append(i)
    for j in xrange(len(temp)):
        List.remove(temp[j])
    if List == []:
        break
    result = List

output = ' '.join(result)    
