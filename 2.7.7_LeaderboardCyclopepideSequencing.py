""" Mass Spectrometry Meets Golf """
""" Step 7 """

import operator

# dictionary of amino acid masses
aa_masses = {"G":57, "A":71, "S": 87, "P":97, "V":99, "T":101, "C":103, "I": 113, "L": 113, "N":114, "D":115,
             "K":128, "Q": 128, "E":129, "M": 131, "H":137, "F":147, "R": 156, "Y": 163, "W":186}


def CyclopeptideScoring(peptide, spectrum):
    """ Compute the score of a cyclic peptide against a spectrum. """
    score = 0
    pep_len = len(peptide)
    peptide2 = peptide + peptide
    for i in range(1, pep_len):
        for j in range(pep_len):
            peps = peptide2[j: j + i]
            mass = 0
            for k in peps:
                mass += aa_masses[k]
            if mass in spectrum:
                score += 1
                spectrum.remove(mass)
    mass = 0
    for k in peptide:
        mass += aa_masses[k]
    if mass in spectrum:
        score += 1
    if 0 in spectrum:
        score += 1
    return score

def Trim(leaderboard, spectrum, n):
    """ Input: A collection of peptides Leaderboard, a collection of integers Spectrum, and an integer N.
        Output: The N highest-scoring linear peptides on Leaderboard wih respect to Spectrum."""
    score_dict = {}
    for j in leaderboard:
        score_dict[j] = CyclopeptideScoring(j, list(spectrum))
    sorted_score = sorted(score_dict.items(), key=operator.itemgetter(1))[::-1]
    #print sorted_score
    for i in range(len(sorted_score)):
        if sorted_score[i][1] == 82:
            print sorted_score[i]
##    for i in range(len(sorted_score)):
##        if sorted_score[i][0] == "EPFVAWAL":
##            print "The rank of 'EPFVAWAL':", i
##            print sorted_score[i]
##            print sorted_score[416:419]
    if n - 1 <= len(sorted_score):
        score_cutoff = sorted_score[n-1][1]
        for j in range(n,len(leaderboard)):
            if sorted_score[j][1] < score_cutoff:
                break
        return [item[0] for item in sorted_score[:j]]        
    else:
        return [item[0] for item in sorted_score]

def Expand(leaderboard):
    aa = ['A', 'C', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'M', 'L', 'N', 'Q', 'P', 'S', 'R', 'T', 'W', 'V', 'Y']
    expanded_leaderboard = []
    if leaderboard == [""]:
        for i in aa:
            expanded_leaderboard.append(i)
    else:
        for i in leaderboard:
            for j in aa:
                expanded_leaderboard.append(i+j)
    return expanded_leaderboard

def LeaderboardCyclopeptideSequencing(spectrum, n):
    """ Implemetn LeaderboardCyclopeptedSequencing.
        Input: An integer N and a collection of integers Spectrum.
        Output: LeaderPeptide after running this algorithm. """
    leaderboard = [""]
    leaderpeptide = ""
    leaderscore = 0
    while True:
        leaderboard = Expand(list(leaderboard))
        for i in list(leaderboard):
            mass = 0
            for j in i:
                mass += aa_masses[j]
            if mass == max(spectrum):
                score_temp = CyclopeptideScoring(i, list(spectrum))
                if score_temp > leaderscore:
                    leaderpeptide = i
                    leaderscore = score_temp
                    print leaderscore, leaderpeptide
                    break
            elif mass > max(spectrum):
                leaderboard.remove(i)
        if len(leaderboard) == 0:
            break
        leaderboard = Trim(leaderboard, spectrum, n)
##        if "EPFVAWAL" in leaderboard:
##            print "YES!!! It's here!!!"
##            assert 0
        print leaderboard[0:2], len(leaderboard)
        #print leaderpeptide
    return leaderpeptide

#PEPFVAWALYDAIKCSQTHYN

spectrum = "0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322"
spectrum = spectrum.split(" ")
spectrum = [int(i) for i in spectrum]
n = 1000

print max(spectrum)
leaderpeptide = LeaderboardCyclopeptideSequencing(spectrum, n)
output = "-".join([str(aa_masses[i]) for i in leaderpeptide])
print output

#print Expand(["A","C"])
#print len(Expand(["A","C"]))
