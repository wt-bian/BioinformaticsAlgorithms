def HammingDistance(pattern1, pattern2):
    """ Calculate the Hamming distance """
    distance = 0
    if len(pattern1) == len(pattern2):
        for i in range(len(pattern1)):
            if pattern1[i]!=pattern2[i]:
                distance += 1
        return distance
    else:
        assert 0, "Two patterns have different lengths."

def Neighbors (pattern, d):
    """ Input: a string Pattern and an integer d.
        Output: the collection of strings Neighbors(Pattern, d) """
    if d == 0:
        return [pattern]
    elif len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = []
    suffix_neighbors = Neighbors(pattern[1:],d)
    for i in suffix_neighbors:
        if HammingDistance(pattern[1:], i) < d:
            for j in ['A', 'C', 'G', 'T']:
                neighborhood.append(j + i)
        else:
            neighborhood.append(pattern[0] + i)
    return set(neighborhood)

def MotifEnumeration(dna, k, d):
    """ Input: intergers k and d, followed by a collection of strings DNA.
        Output: all (k,d)-motifs in DNA. """
    patterns = []
    k_mers = []
    for ind_1 in dna:
        for ind_2 in range(len(ind_1)-k+1):
            k_mers.append(ind_1[ind_2:ind_2+k])
    for pattern in set(k_mers):
        for ind_3 in Neighbors(pattern, d):
            mismatch_ind3 = Neighbors(ind_3, d)
            check_1 = True
            for ind_4 in dna:
                check_2 = False
                for ind_5 in mismatch_ind3:
                    if ind_5 in ind_4:
                        check_2 = True
                if not check_2:
                    check_1 = False
            if check_1:
                patterns.append(ind_3)
    return set(patterns)

dna = ['TGTTTGGGCCGCTTCATAAACAAAT','CGTATGGCATATAGCTGAAATGTTC',
       'CTTTTTGAACTGTTGGCCACACCCA','TGTTATTTTTCCCCACTTCAGCTAA',
       'GATAATGAGCGTTGCTAAGCTGTTA','TGTTTACAACGGTCATGTGTCCATG']
for i in MotifEnumeration(dna, 5, 1):
    print i
