Sample = '847 648 0 603 129 404 510 97 751 267 767 535 381 301 870 710 664 607 450 363 716 137 266 613 648 864 777 733 353 154 244 977 914 701 830 200 364 848 154 604 240 337 1057 466 57 1017 97 511 251 1001 567 438 250 977 967 510 676 750 507 547 97 137 113 501 960 398 347 904 604 1017 888 579 413 103 960 874 284 1017 226 785 450 761 664 329 863 813 1114 147 1011 985 210 466'
SampleList = Sample.split(' ')
SampleLen = len(SampleList)
for i in xrange(SampleLen):
    SampleList[i] = int(SampleList[i])
SampleList.sort()
substract = {}
output = ''

for i in xrange(SampleLen):
    for j in xrange(i+1,SampleLen):
        temp = SampleList[j] - SampleList[i]
        if temp != 0:
            if temp in substract.keys():
                substract[temp] = substract[temp] + 1
            else:
                substract[temp] = 1
result = sorted(substract.items(),cmp=lambda x,y: cmp(x[1],y[1]),reverse=True)
        
for i in xrange(len(result)):
    for j in xrange(result[i][1]):
        output = output + str(result[i][0]) + ' '
