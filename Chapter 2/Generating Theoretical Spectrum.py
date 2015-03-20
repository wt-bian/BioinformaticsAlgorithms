sample = 'VPWMTIIWEHKNEY'
weight = {'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,
          'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,
          'R':156,'Y':163,'W':186}
sub = list()
for i in range(len(sample)-1):
    for j in range(len(sample)):
        if j+i +1> len(sample):
            sub.append(sample[j:]+sample[:i+j+1-len(sample)])
        else:
            sub.append(sample[j:j+i+1])
sub.append(sample)


spectrumList = list()
for i in range(len(sub)):
    spectrum = 0
    for aa in sub[i]:
        spectrum = spectrum + weight[aa]
    spectrumList.append(spectrum)

spectrumList.sort()

result = ''
for i in range(len(spectrumList)):
    result = result + str(spectrumList[i]) +' '

