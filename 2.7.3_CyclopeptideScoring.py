""" Mass Spectrometry Meets Golf """
""" Step 3 """

# dictionary of amino acid masses
aa_masses = {"G":57, "A":71, "S": 87, "P":97, "V":99, "T":101, "C":103, "I": 113, "L": 113, "N":114, "D":115,
             "K":128, "Q": 128, "E":129, "M": 131, "H":137, "F":147, "R": 156, "Y": 163, "W":186}

peptide = "PEEP"
spectrum = "0 97 97 97 100 129 194 226 226 226 258 323 323 355 393 452"
spectrum = spectrum.split(" ")
spectrum = [int(i) for i in spectrum]

def CyclopeptideScoring(peptide, spectrum):
    """ Compute the score of a cyclic peptide against a spectrum. """
    score = 0
    pep_len = len(peptide)
    peptide2 = peptide + peptide
    for i in range(1, pep_len):
        for j in range(pep_len):
            peps = peptide2[j: j + i]
            #print peps
            mass = 0
            for k in peps:
                mass += aa_masses[k]
            #print mass
            if mass in spectrum:
                score += 1
                spectrum.remove(mass)
    #print score
    mass = 0
    for k in peptide:
        mass += aa_masses[k]
    if mass in spectrum:
        #print mass
        score += 1
    if 0 in spectrum:
        score += 1
    return score

def LinearScoring(peptide, spectrum):
    """ Compute the score of a linear peptide against a spectrum. """
    score = 0
    pep_len = len(peptide)
    for i in range(1, pep_len + 1):
        for j in range(pep_len - i + 1):
            peps = peptide[j: j + i]
            #print peps
            mass = 0
            for k in peps:
                mass += aa_masses[k]
            #print mass
            if mass in spectrum:
                score += 1
                spectrum.remove(mass)
    #print score
    if 0 in spectrum:
        score += 1
    return score

print CyclopeptideScoring(peptide, spectrum)
