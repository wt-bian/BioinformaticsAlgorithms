DNA = 'GCCTGTTTTTTCACGCTGGCGCGGATGCCTGCTGTTTTGGATCTGTTTTGCCTGTTCACGTTGCTTTTCACGTTTTCTGGCGCTTTTTTGGATGCGCTTCACGGGATGCGCGGATGGATCTGGCCTGTTGCGGATTTCTGGGATGCTTGGATCACGCACGCACGGGATCTGCACGCACGGGATCACGTTCTGGCGCGCCACGCTGCACGGCCTGGGATGCCACGCTGCTGGGATGGATGGATGCGCTTGCTTGCCTGGCGCGGATGGATTTGGATCTGCTGTTTTCACGCACGCTGGGATGCCACGGGATTTTTTTGCTTGGATGCCTGCTGGCCTGGCCTGCTG'
kmers = 10
mismatch = 3


def getMutations(word):
    mutation = set()
    mutation.add(word)
    for i in range(len(word)):
        for replacement1 in 'ATCG':
            temp1 = word[:i] + replacement1 + word[i+1:]
            for j in range(len(word)):
                for replacement2 in 'ATCG':
                    temp2 = temp1[:j] + replacement2 + temp1[j+1:]
                    for k in range(len(word)):
                        for replacement3 in 'ATCG':
                            temp3 = temp2[:k] + replacement3 + temp2[k+1:]
                            mutation.add(temp3)
                    #mutation.add(temp2)
            #mutation.add(temp1)
    return mutation

mutationsList = list()
for i in range(len(DNA) - kmers + 1):
    word = DNA[ i : ( i + kmers ) ]
    mutationsList = mutationsList + list(getMutations(word))



from itertools import groupby
result = max((len(list(g)),v) for v, g in groupby(sorted(mutationsList)))[1]
