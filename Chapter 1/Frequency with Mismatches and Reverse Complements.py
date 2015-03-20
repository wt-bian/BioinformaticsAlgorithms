DNA = 'GAATGATTCCACATGTGAGACACAGACACATTCGACATGTTTCCATGTTTCATTGTTTCCATGTCATTCGATGTGAGACATGTGAATTGTGATGTTGTATTGTCAATATTGTTTCATTTCGAGACATTCGATTCTGTTGTTTCGATGTTGTGATGTCATGTATCACATGTATGAGAGAATGATTCATTGTGATGTATTGTTGTTGTATGACAGACAATCAATGAGATGTGAGATTCGACA'
kmers = 8
hamming_distance = 3

# get the total mutations of a certain k-mer with one mismatch
def mutations(word, hamming_distance):
    mutation = list()
    mutation.append(word)
    for i in range(len(word)):
        for replacement in 'ATCG':
            temp = word[:i] + replacement + word[i+1:]
            mutation.append(temp)
    return set(mutation)

# get the total mutations of a certain k-mer with 2 mismatchs
def mutations2(word, hamming_distance):
    mutation = list()
    mutation.append(word)
    for i in range(len(word)):
        for replacement1 in 'ATCG':
            temp1 = word[:i] + replacement1 + word[i+1:]
            for j in range(len(word)):
                for replacement2 in 'ATCG':
                    temp2 = temp1[:j] + replacement2 + temp1[j+1:]
                    mutation.append(temp2)
    return set(mutation)

# get the total mutations of a certain k-mer with 3 mismatchs
def mutations3(word, hamming_distance):
    mutation = list()
    mutation.append(word)
    for i in range(len(word)):
        for replacement1 in 'ATCG':
            temp1 = word[:i] + replacement1 + word[i+1:]
            for j in range(len(word)):
                for replacement2 in 'ATCG':
                    temp2 = temp1[:j] + replacement2 + temp1[j+1:]
                    for k in range(len(word)):
                        for replacement3 in 'ATCG':
                            temp3 = temp2[:k] + replacement3 + temp2[k+1:]
                        mutation.append(temp3)
    return set(mutation)

# calculate the frequency of a certain k-mer and its mutations
def calK (mutation, DNA):
    temp = 0
    for i in range(len(mutation)):
        temp = temp + DNA.count(list(mutation)[i])
    return temp

# get the reverse complements
def revCom (word):
    a = word
    b=[]
    c=[]
    for x in range(len(a)):
        b.append(a[len(a)-x-1])
    for x in range(len(a)):
        if b[x]=='A':
            c.append('T')
        elif b[x]=='C':
            c.append('G')
        elif b[x]=='T':
            c.append('A')
        elif b[x]=='G':
            c.append('C') 
    d=''.join(c)
    return d

# calculate all the frequencies
frequency = list()
for i in range(len(DNA) - kmers + 1):
    word = DNA[ i : i + kmers ]
    if hamming_distance == 1:
        freqDNA = calK(mutations(word, hamming_distance),DNA)
        freqRevCom = calK(mutations(revCom(word), hamming_distance),DNA)
        frequency.append(freqDNA + freqRevCom)
    elif hamming_distance == 2:
        freqDNA = calK(mutations2(word, hamming_distance),DNA)
        freqRevCom = calK(mutations2(revCom(word), hamming_distance),DNA)
        frequency.append(freqDNA + freqRevCom)
    elif hamming_distance == 3:
        freqDNA = calK(mutations3(word, hamming_distance),DNA)
        freqRevCom = calK(mutations3(revCom(word), hamming_distance),DNA)
        frequency.append(freqDNA + freqRevCom) 

# get the output
maxium = max(frequency)
count = frequency.count(maxium)
resultList = list()
temp = -1
for i in range(count):
    begin = frequency[temp + 1:].index(maxium) + temp + 1
    end = begin + kmers
    resultList.append(DNA[begin:end])
    #resultList.append(revCom(DNA[begin:end]))
    temp = begin

resultSet = set(resultList)
resultStr = ' '.join(resultSet)
