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

for i in list(Neighbors("AAGAACTACACC",2)):
    print i
