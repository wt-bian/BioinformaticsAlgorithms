DNA = 'TCAACCCCGTCCCCGTCCCCGTCGTAAAACGTAAAAAATCAACGTTCAAATCGAATCTCCCCCCCATCGTCAACGTCGTTCAACGTCCCAACCCAAAATCCGTCCCAACCCTCCGTTCCCCTCCGTATCGCCCCCCTCTCTCTCAATCCGTCGTCGTCCCCCCTCCCCCCCTCAACCCAAAACGTCCCCCCCCCATCGAAAACCCAATCAACCCTCTCCGTCCCCCCATCGCGTAATCAACGTCGTTCCGTAAAACCCAAAAATCGTCCCCAAAACCCCCCCGTATCGTCATCGTCATCGCCCCGTTCATCGCGTCCCCGTATCGCCCATCGATCGTCCGTCCCTCATCGCGTTCATCGTCATCG'
kmers = 10
mismatch = 2

mutation = set()

def getMutations(word, mutation):
    mutation.add(word)
    for i in range(len(word)):
        for replacement1 in 'ATCG':
            temp1 = word[:i] + replacement1 + word[i+1:]
            for j in range(len(word)):
                for replacement2 in 'ATCG':
                    temp2 = temp1[:j] + replacement2 + temp1[j+1:]
                    #for k in range(len(word)):
                    #    for replacement3 in 'ATCG':
                    #        temp3 = temp2[:k] + replacement3 + temp2[k+1:]
                    #    mutation.append(temp3)
                    mutation.add(temp2)
            #mutation.add(temp1)

def mutations(word):
    mutation = list()
    mutation.append(word)
    for i in range(len(word)):
        for replacement1 in 'ATCG':
            temp1 = word[:i] + replacement1 + word[i+1:]
            for j in range(len(word)):
                for replacement2 in 'ATCG':
                    temp2 = temp1[:j] + replacement2 + temp1[j+1:]
                    #for k in range(len(word)):
                    #    for replacement3 in 'ATCG':
                    #        temp3 = temp2[:k] + replacement3 + temp2[k+1:]
                    #    mutation.append(temp3)
                    mutation.append(temp2)
    return set(mutation)


def hamming_distance(s1,s2):
	return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


# get all mutations
for i in range(len(DNA) - kmers + 1):
    word = DNA[ i : ( i + kmers ) ]
    getMutations(word, mutation)
mutationsList = list(mutation)

def calK (mutation, DNA):
    temp = 0
    for i in range(len(mutation)):
        temp = temp + DNA.count(list(mutation)[i])
    return temp


# calculate all the frequencies
frequency = list('0')* len(mutationsList)
for i in range(len(frequency)):
    frequency[i] = 0
for i in range(len(mutationsList)):
        for j in range(len(DNA) - kmers + 1):
            s2 = DNA[ j : ( j + kmers ) ]
            if hamming_distance(mutationsList[i],s2)<=mismatch:
                frequency[i] = int(frequency[i]) + 1                

# get the output
maxium = max(frequency)
count = frequency.count(maxium)
resultList = list()
temp = -1
for i in range(count):
    result = frequency[temp + 1:].index(maxium) + temp + 1
    resultList.append(mutationsList[result])
    temp = result

resultSet = set(resultList)
resultStr = ' '.join(resultSet)

        
