""" Mass Spectrometry Meets Golf """
""" Step 7 """

import operator
from collections import Counter

# dictionary of amino acid masses
aa_masses = {"G":57, "A":71, "S": 87, "P":97, "V":99, "T":101, "C":103, "I": 113, "L": 113, "N":114, "D":115,
             "K":128, "Q": 128, "E":129, "M": 131, "H":137, "F":147, "R": 156, "Y": 163, "W":186}


def CyclopeptideScoring(peptide, spectrum):
    """ Compute the score of a cyclic peptide against a spectrum. """
    score = 0
    #print peptide
    pep_len = len(peptide)
    peptide2 = peptide + peptide
    for i in range(1, pep_len):
        for j in range(pep_len):
            peps = peptide2[j: j + i]
            mass = sum(peps)
            if mass in spectrum:
                score += 1
                spectrum.remove(mass)
    #print peptide
    if sum(peptide) in spectrum:
        score += 1
    if 0 in spectrum:
        score += 1
    return score

def Trim(leaderboard, spectrum, n):
    """ Input: A collection of peptides Leaderboard, a collection of integers Spectrum, and an integer N.
        Output: The N highest-scoring linear peptides on Leaderboard wih respect to Spectrum."""
    score_dict = {}
    for j in range(len(leaderboard)):
        score_dict[j] = CyclopeptideScoring(leaderboard[j], list(spectrum))
    sorted_score = sorted(score_dict.items(), key=operator.itemgetter(1))[::-1]
    if n - 1 <= len(sorted_score):
        score_cutoff = sorted_score[n-1][1]
        for j in range(n,len(leaderboard)):
            if sorted_score[j][1] < score_cutoff:
                break
        return [leaderboard[item[0]] for item in sorted_score[:j]]        
    else:
        return [leaderboard[item[0]] for item in sorted_score]

def Expand(leaderboard, extended_alphabet):
    expanded_leaderboard = []
    if leaderboard == [""]:
        for i in extended_alphabet:
            expanded_leaderboard.append([i])
    else:
        for i in leaderboard:
            for j in extended_alphabet:
                expanded_leaderboard.append(i+[j])
    return expanded_leaderboard

def LeaderboardCyclopeptideSequencing(spectrum, n, extended_alphabet):
    """ Implemetn LeaderboardCyclopeptedSequencing.
        Input: An integer N and a collection of integers Spectrum.
        Output: LeaderPeptide after running this algorithm. """
    leaderboard = [""]
    leaderpeptide = ""
    leaderscore = 0
    while True:
        leaderboard = Expand(list(leaderboard),extended_alphabet)
        #print leaderboard
        for i in list(leaderboard):
            mass = sum(i)
            if mass == max(spectrum):
                score_temp = CyclopeptideScoring(i, list(spectrum))
                if score_temp > leaderscore:
                    leaderpeptide = i
                    leaderscore = score_temp
                    print leaderscore, leaderpeptide
            elif mass > max(spectrum):
                leaderboard.remove(i)
        if len(leaderboard) == 0:
            break
        leaderboard = Trim(leaderboard, spectrum, n)
        print leaderboard[0], len(leaderboard)
    return leaderpeptide

def SpectralConvolution(spectrum):
    result = []
    for i in range(len(spectrum)):
        for j in range(i + 1, len(spectrum)):
            if abs(spectrum[j]-spectrum[i]) != 0:
                result.append(abs(spectrum[j]-spectrum[i]))
    return result

def ExtendedMasses(convolution, m):
    convolution = [i for i in convolution if (i >= 57) and (i <= 200)]
    occurrences = Counter(convolution)
    sorted_occurrences = sorted(occurrences.items(), key=operator.itemgetter(1))[::-1]
    #print len(occurrences), len(sorted_occurrences)
    if m - 1 <= len(sorted_occurrences):
        occur_cutoff = sorted_occurrences[m-1][1]
        for j in range(m,len(sorted_occurrences)):
            if sorted_occurrences[j][1] < occur_cutoff:
                break
        return [item[0] for item in sorted_occurrences[:j]]        
    else:
        return [item[0] for item in sorted_occurrences]

spectrum = "905 918 285 275 1523 1162 1100 991 1607 493 1002 1309 1443 156 1299 525 1289 1358 97 399 769 260 284 1531 250 559 245 114 1434 529 719 768 443 1446 1521 1131 1044 1584 147 1574 363 502 520 1409 718 1476 1461 406 1168 1278 1634 633 416 953 1333 804 87 485 1202 716 780 803 1219 1073 1315 1402 1236 200 1436 1434 1329 1271 137 128 1315 287 672 147 1018 1618 1049 908 547 599 959 1506 730 865 917 648 666 667 1305 877 621 1375 553 606 590 1322 813 384 319 1174 1446 1196 893 97 1031 844 1337 569 215 519 1152 287 1471 0 190 762 804 312 828 269 941 1228 1201 1054 1593 916 450 1721 103 816 1537 677 530 131 275 1005 184 1624 198 1590 397 1122 1620 412 388 632 1191 1452 1324 690 163 681 1624 1089 406 805 917 113 703 346 1437 1574 1608 856 1003 1192 392 1558 1168 1565 1055 1115 1088 101 432 952 278 553 1040 422"
spectrum = spectrum.split(" ")
spectrum = [int(i) for i in spectrum]
n = 500
m = 20

extended_alphabet = ExtendedMasses(SpectralConvolution(list(spectrum)), m)
print extended_alphabet, len(extended_alphabet)
print max(spectrum)
leaderpeptide = LeaderboardCyclopeptideSequencing(spectrum, n, extended_alphabet)
output = "-".join(str(i) for i in leaderpeptide)
print output

