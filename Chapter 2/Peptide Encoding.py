translation = {'AAA':'K','AAC':'N','AAG':'K','AAT':'N','ACA':'T','ACC':'T',
               'ACG':'T','ACT':'T','AGA':'R','AGC':'S','AGG':'R','AGT':'S',
               'ATA':'I','ATC':'I','ATG':'M','ATT':'I','CAA':'Q','CAC':'H',
               'CAG':'Q','CAT':'H','CCA':'P','CCC':'P','CCG':'P','CCT':'P',
               'CGA':'R','CGC':'R','CGG':'R','CGT':'R','CTA':'L','CTC':'L',
               'CTG':'L','CTT':'L','GAA':'E','GAC':'D','GAG':'E','GAT':'D',
               'GCA':'A','GCC':'A','GCG':'A','GCT':'A','GGA':'G','GGC':'G',
               'GGG':'G','GGT':'G','GTA':'V','GTC':'V','GTG':'V','GTT':'V',
               'TAA':' ','TAC':'Y','TAG':' ','TAT':'Y','TCA':'S','TCC':'S',
               'TCG':'S','TCT':'S','TGA':' ','TGC':'C','TGG':'W','TGT':'C',
               'TTA':'L','TTC':'F','TTG':'L','TTT':'F'}

strings =''.join([line.rstrip() for line in open('C:\\Users\\Bian W\\Downloads\\B_brevis.txt')])
AA = 'VKLFPWFNQY'

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

strings2 = revCom(strings)

protein1 = ''
for i in range(int(len(strings)/3)):
    protein1 = protein1 + translation[strings[3*i:3*i+3]]
protein2 = ''
for i in range(int(len(strings)/3)):
    if (3*i+4) > len(strings):
        break
    protein2 = protein2 + translation[strings[3*i+1:3*i+4]]
protein3 = ''
for i in range(int(len(strings)/3)):
    if (3*i+5) > len(strings):
        break
    protein3 = protein3 + translation[strings[3*i+2:3*i+5]]
protein4 = ''
for i in range(int(len(strings)/3)):
    protein4 = protein4 + translation[strings2[3*i:3*i+3]]
protein5 = ''
for i in range(int(len(strings)/3)):
    if (3*i+4) > len(strings):
        break
    protein5 = protein5 + translation[strings2[3*i+1:3*i+4]]
protein6 = ''
for i in range(int(len(strings)/3)):
    if (3*i+5) > len(strings):
        break
    protein6 = protein6 + translation[strings2[3*i+2:3*i+5]]

resultList = list()
temp = -1
for i in range(protein1.count(AA)):
    result = protein1[temp+1:].index(AA) + temp + 1
    resultList.append(strings[result*3:result*3+len(AA)*3])
    temp = result

temp = -1
for i in range(protein2.count(AA)):
    result = protein2[temp+1:].index(AA) + temp + 1
    resultList.append(strings[result*3+1:result*3+1+len(AA)*3])
    temp = result

temp = -1
for i in range(protein3.count(AA)):
    result = protein3[temp+1:].index(AA) + temp + 1
    resultList.append(strings[result*3+2:result*3++2+len(AA)*3])
    temp = result

temp = -1
for i in range(protein4.count(AA)):
    result = protein4[temp+1:].index(AA) + temp + 1
    resultList.append(revCom(strings2[result*3:result*3+len(AA)*3]))
    temp = result

temp = -1
for i in range(protein5.count(AA)):
    result = protein5[temp+1:].index(AA) + temp + 1
    resultList.append(revCom(strings2[result*3+1:result*3+1+len(AA)*3]))
    temp = result

temp = -1    
for i in range(protein6.count(AA)):    
    result = protein6[temp+1:].index(AA) + temp + 1
    resultList.append(revCom(strings2[result*3+2:result*3+2+len(AA)*3]))
    temp = result

##resultStr = ' '.join(resultList)
##
##'AUGGGGCGGUGGCGUGGCCGAAGGCAAGUCGAUGACAGUAGUUGUGGCCGCGCAGGCGCAGAGUCCCGAGUUCCACCCCUGUCAAGAGUAACUAUGGCACAUAUCGAUAUCCUGAUCCGAAAUAUCUCGGUGCUGGAUGAGGCUUCCGGUGUACCAUGGAUGCGAACUGCGCAGACGUGUCAGAGUCAACUGAAUAAUGUACGAUCUCAGCCAAUGCGCCGCAAGAUCGCUUUCUAUGAGGGCGUGAGCCUAAUUAUCGUGAACAUUCAACGUGGCUCGGCCCGCAUCAGGGGUAACUUGCCCACCAGGAGAGCACCCCGUAUUGCAUGUCUUCCGAGCCAAGGUAUAGUGCUUCAUAGACUCAAUACGGAGUCGCGCGGCCGGAACCAGGUCGGGCAGGUCAACCAUCAGGCUGCCGAUGGGUACGGGUUUAUGCGCAAGACUGAAAGGAAUGGUGUACUGCCAGCAGACACAUCCGGACAUGAGUUGUCACAGUACAGCGUCAGUGCCGCUGAUGCGUCUCUGACUCGAACACACGGGGUACUGUCGGGACGUACUCAGGUGCAUCUUUUGAGCCUUGAAUUCGUGUUACCACAACCAAUUAACCGACAAGGGCCAUGUAACGUUACGAGCGUGGUCCAACGGCCUGAGCAACGUGCCAUGAACAUCCUCCUUCUACUUUUCCCUCUCCCGCCUGCAAGCACAGGACCAUCACAGGGCACCCGACCCAACAUUACCCUAGACGAUGGUUCUGAAAGUGUUUGGUAUACAUCGACCGUGACUUGUAAGCGGACCCACACAAUCAACCAUCACGUUCUUUAUUUACCGAAUAGAAGGCGUAGGUUACCGGGAACGGCCUCGGUCUCCUCAAAUCGGUCGGAUCAAGUAAUUUGCCCGUCGUCACCUAAAGCAGUACGUUUAGAAAGUCUAAUCGCUCGCCCAUCAGCGAACACCAUUCUAUGGUAUCCGAUGCAUUAUAUGUGGUGGAAGCCGAAUUAUGCCUGCUUCCACGUCGGGAAUAUUACACGUCACGGGGUACGCUCCACUAUGUUAAUAACAUGCAGUUGUAUAGCCCCAUAUUCCCGUAGAGUGUUGCGUAUUAAGCGCAACACAGGUAUGGUAUUGAGCAUUUUGCGUGACGUUAAGUGGAAUAUCGCUUAUGAGGGAUAUGGAAACGAAACUUGUCCACCUAGCACUCACUACGUAGUGACGUACUACUUAAUUGUUAAUCAGAACUGCCCGCCAACCAGUUACCUGUCUACGCACUUACUGAGCAGGCGUUGUUCAGAAAGGUACUAUAGUUUUGUAUGCCUCGUGCCCGGGCGAGAUUUUCGAGGAGCGUCCCCAGUGCUUUCGUUCCAGUGGAGUUUAGGGCCUCAGACUAAGGAAAGCGUGCCUUCCAUAAUACAUAGCGCAUCGUCAAAGAGCGACCGCUUAAGUUUGUAUGCUGGGCUUGAUCCAGAAAAGAUACGUGAAUUAAGUGCAAAGUGGUUGCCCGAAUUGUUCUCUCAUAGCCCUUACCGUUAUAUGCUUGACUUCAGCAAUAGUCUCAUACGUUUCCUCCUCCUAAUCCGAUCGUUCCGGAAGCGUGUGCGUGGAGGUGCCGAAUGGCCGACCGGAUCUCCCAUGUGGCUACUUGCCAUACGGGACUGUAAGCUUUCGGUAUUCAAAAAGUCUCUGCCAAAUAAUGGGGUUGGGCGCCAACCCAGAUUCAGGGCCCAAAAUUGUGUUAGCCAAUAUGGGGACGCAAGUCUCAGACGUAGUAAGCAGGGUGUCCACCCAUUUCUGAAGGUGCUGGCUGUCUUAGACACAUACCAGUGCUGUUCAUACCUUCUCGAGCGUACUCGCUCUAUCAACCCUUCGUCAUAUCGGUUCUUUUCUUCCUACAGACGCAACGCCCACGACCGCUCCACUUCUAGCUGUCGAAAGUGUGUAGUCCAAGGGCACUAUCCAUACUUAACUACAUUUCUCCUUACUUCUGUCGGCGGAAUCAGUGACCGACUCUAUAUAAUACGUCAGGAAAGGAUGGAUGGGUGCGACGCACUGACCCCGACAAUCCAUCUUGAAUUAGCCGGGCCCCUCAUACCCGAUGUAUGUUUUCAGCCACUUUUGACGGGAUUACUGUUUGGUUCUACUUUCUUGGUGGGCCAUUUGGUCCACGCUCAGAAUCGCAGAGCUGGGCGGACCCAGCAGCCAAUCUCUACCCUAUACCCGGAAGUCAAGAACCCUUCAGUAGCGUCCAAGUAUUUUACAUAUCGACCGCAUACUACGCAAGCCAUCAACAGGGUUCCUGUAGUCCUAUUAUUCUGGUGUAGAUCUUACGUGGCCCCUCUCGAUCCAGAAAGCCUCUUGUGGCUAGAGAAACCCAAGCGCUCCUUUUGCCAAACUCCACACUGCAGCUUAAGGUUCCCCCUAUGUUAUCAAUCUUGUGCUUUGCGUCGGGUCUUACCCGUGCGCGAAGCGGCCUCGACUUUCAAAAAUGCGCGAGAAGGGUUGACUUGUUUCGAUCUCGAUUCUUGGUCACUUGCGACCUCAGAAAGUAAAUUGUUUUGUUGUCGCGAGGCUAUCUUAAGCCAGUCUUUCCCUCCUCGACCACUGUCCACUUGCCGCCCAGUCACAUCUCCUCUCGCGACCAGCAAAAGCGCCCACUUAGGUCAGCGGUUACCAUCGCCACGCUCUUCUAUGACGUUGAGGCAUCUUCAGCCACUGGGAGUGUCCAAUACUAGAUCCAGUUUUUAUGACCUCGACUUAAUUAAAGGGGGUAUCCGAGCGCUCGCGACUAGGCACAUGGAAUCUAAAGCUAUACACCUCCAGGCUUUGUACAUGGAGGGGGGAAACGUUAGAAAAAUUCCAAUUCAGCCGCGAAGCACAUCUGGCGUGAAGCUUGUAGCGCAUCGCGUUAAUUGCUGCAUCAAAGUAUUAACCCUGAUACUCCCACUAUACGGGGGGGUCUGGAGUACUCUUUGUGACUCUAUAUGCGAGCCGCGUGCCGACGGGUCCGCUCUCUCGCGGAUAAUUCAUAAGGGAAGGGAGGGCUUUGAUGUAAGCACGCUACACCUCUCCCGGACCGUUGACGAUCCGACAUCGAAAGACGGGCACGUUAUCGAAGACGCGACUCUACCAUCUGUAUUGUACCGACUAACUUGUCCGCCACGCUUUACUUCUUAUGUUCGUGAUAACAUGCGCCCUAAGAGUGCAGCGGAGGACUUAGUAAACACAACGUUAUCGGGAGUAAAACUCGUGGGAGUUUGCCACAGCAGACGCCUCGCGCUAGGUUUUAUCCUCCAAAGAGUAGCCGUCGAUCGAAUCGAAUUGCGAGUAAAUCUCAUACAUCCCAUUCCGGCUAUGGCCCUGAUUCUCGACUCGCGUAACAACCGCUAUGCGCGUCCUCUCCGUCUCUUCCUCGUUAUCAGCCCCUACCUCACCGUGUUGUCGGGAAAGUCACCGUAUAUGUUCAGCCCUAGAACUCGUACGUAUAUUACAAUUCGAUUCUCGCCACGCGGAUACCUAGAUCCAAGGCAGUUACGAGGGCUGCCUUUCAACAUAGACAGAACUACGCCAUCUAUCGCACAAGAAACCCGCUUACAUCAAAACAUUAACCCGAUAAAACGUCCCAUCUUAUUAACGCUCCGGGGGUUAUCGUGGAGCAAGUUAUUCGAGAGGUCCAAGUUGAUCAGUAUCUUGAUUUACGGACCCGAUUAUGGGAGAAAUGAUCAGGACGGCGACAGGUUAUCGAGAUUCGGCCCUCUCAACUAUUCAAGCAACUGUAGUGCACGACAUCACGCUCACGGUAACACAGCACGCUGUAGCGGGGCCCUCUCUCACGAGCUCAAGGGACUUAACAGUACUUCGCAAUGGGCUUGUGUAGAAUUACUUAACCUAAAUGUAGAAAAUCUCUCCUUUCGUGGUCGCAGCUCCAGCAAACGCCGCAAGGGCCGAUUAUUUUGUCUUUAUAAACGUGUAUUCGUCGUCCAGGGUGAGAGCAUCGGACUUAACAAUUUUCCCGUAACCCGUGGCUUCCCUGUAACUUGCCAGCUCAUGCACCUUCCUACUCCGACUUUGUACUCACGAUGUAACUCCGGAGUUCGCAGAAAACCUUACGGAACUGAUCCUCUGAUAUCAUCCGGACUUGUAAAUACUCUGGUAGGGGAACCACCAGUCGCUGUGCAUCUACGAGCAGGGUGUCGACACACGACAGCGGUAUGCCGUGGACCGAGUCAGGUUCGAUCCAAUUGUCACAUGCCAUUGGCCCCGCUCUUCGUACGGUUUAUGUUGUUUGCAUUCUGCCUAGUACUGCGUAAAUCACUUCGCACUUCAGCAUUCUUUAAAGAAAUUAAGUAUCCAUUGACGCCCGUGCGUCUUGGGUCGUGUCCCGUACUCAUCGCUGAACUUCGAAUAGAUCUUCUGCGCUGUAGUGGAAUAGCGAGGAAUCUUUUGAAUACCGGGACCUGGCGUAGGCCAGCCAGGGUAAACGCCGAGUACACUGCGUCCACUACUCGAGGGCCGGACCGCGACGCGCGUUACGGGGUACUUGCAAGUUUUCACAGAUAUGAAGAAAAUAGUCCGCUUCCGUUUCUUUACGACUCUGAUACUCUCCAACCCUCUACACGAUGUUCAACUCUUACCUAUCCCAUCCCCACGUUUCGAGCAAGUAUCCUCCUGCCCUGUAGGCCGAAUGGUGGGGACGCUUCGUGUGCGGGUGACUGUUGGGCUCAACACCUUACACCUCAUGUGAUGGGUAAUGGAAGGCCCCUGGACCAUGGAAUCCCGCCGGACGCGAGUUCAUGGCCCCCGCCGGUGUACCUCGCAAAAAAGGAACUACGGAAUCGUACUCGCCAAGCCGUAAGGCAGCAGAUCCUAUACCGCUUCCUCUACAAGUGGAAGUACACAGAUUAUGGAUGUCAGCUCCGACAUAAGCGGGAUAGACCGUGUAUUGAGGCAUGCAUUUCGAGAGGAUGCGACGCUCCCUCACAUCCGCACUUUUCACUGCAGCGCCUCUGUUCGCCCGCGCCGAUGCUUCAAAUUCAACAGUAUCUGACUCUCCGGAGUACGCAUAGCCAUGUGGUUCGAAGUUUUUGGUCGACAGGCUCAGUCAGCACAUACGGAGACUUGGAAAGGGGAGAUGCACUUGCUACUGCGGUUCGCGCAGGGGGUUGUUUCUUGCGCAAUCGUCUGGUUAGCCCCCAAGAUCCGCAGCGCUCACGGAGUUUAGCAUUACGCCCCGCCUGUCGGAGGGUCGGGCCUAUAGCAAAGCAAACUACGGACACGGAGACCCUGAUUUUACGGUUCGAACCCAUCCCCUUAAAUAUUAGGAUCAUGCGAGGCCCCGUGCCACGACAUACCCUUCCUACUCGCAGUAGCGAGAGUUGUUUUCUCUGUGUGGGACAGGGGUUGGACCUCAGUGGCAAUGUAAGUUCCUUUCCCAGCGUCGCACGACUACCUGAUGUGGUUUCUGAAUUCUCGCCAGCCGCGAUUAAACGUGCGAAUCUAGAAUUCACACCGCGCGCUAACUCGGGCCCAAGGACGGGUAGUGUAGUUAAUGUUAAUGUUCAGCUCGUCGACCCAAGAACUCAGACUGGGGUCCCCAGUUGGCCGGGUUUUUUGGAGCGCGAAAUCGUUGGAGCGUUGUCCGGUAGUACUCCUGCCGGGAUUCGGCCCACAUAUUAUAAUUCCAGGGCGAGAGACGUGAUUCGCUCACUGUCUCAAUCCAACUCGGUUACCUUCAGUCCUCAAGUGUCCAAAAGAUAUAAUAAAACGAGUCGAGCAGACCCGUAUCACGUGGGUAGCCGCGGCCAACCCGCUGGAUUCCACGUAGGAGGGUUAGAACUUCGACUUCUCGGGGGUUCAUGCACACCCUGGUUAGCUGGGGGGGACCUUUGGUGCCCUGGAAGAACGGUACUGGCUGAUCAUAAUGGCACGCAGUUCGGACAGGACAAGUUCACGCGAAAGCGUCUCUUACGCGAGUAUCUGGGACCUGGUACCUUCUUAGGACUCCGGGUCUUUCGGCAUAUCAGUGGUCCAAUGCAUAAUCUCCGUUAUUAUAUGGAUGGCGCAGAUUUCCUCACACAACCGUAUACGACUUGUUAUCAUGAACGACAAAAUUGGGGCACCAAAUCGUCCGAUCAACUGCAAUACGAUCGAAACGAUUAUACCAAGGUAAACGACGGCCUAUGUACCUUGGACUGCCGCGUUCAUGUCCUUUGUACGGUGACUUCACUGGAUACAGUAAUCAUCAACAGCCACGAACCGCACGUACCCUCGUUACAUGCGCACACUCGGUCCGCCAGGCGGGUCUACAUUACGAAACAGGGCAUUACAAUUCUGGGUAGGUUUCGAAGAUCAAUUCAAACGAUAGCUCAUCUUAGUUCCGGCAAUAGCCCUCCUUUCCUAGACAAACACGGACAGGUGAUAACUCGGAGGGAUUCCCCCGAUGGAUUAGCGGUCGAAACGCCCGGGCAACGGUCAGCUCACGAGUACGUGUAUAACGUGCCAUCAAACCGGCCCUGUAUGCCGGUGACUAUAGAUAGCUACUCCACAUCGGGGGCUCGAAGGGACUACUCGUUAGCGGGACGUUCUUGCGUAUACAUUUUGGCCCUUGCGCCUCCUAGGAUGACUUUCAAGGAGAGGGGGUCUCCAAUAGACCAAACCAUUUGUUUUAUUAGAGUAAAUGAUCUGACUUCCAGUGAGGCCAGCCUCCUUCCCCUCGCGAUUAUAUUGUGCCGCAGAAGGGCGAACUUCCGACCUAGUGUCUCGACGUGUAGUGUCGGGCUGGCCACCCCAAGACGCGUCUGGCAGAGCAAGUCUGCGUUCAAGAGCCCUGUAAGUUCCGAGAACGGCGAAGCACGGAACCAGACAAUGGCACAGCAUACCACAUAUAAACGCGGUGCAUCAAGGCGAUUCGGGGUUCUAAGAGAUCUUGCGUUGUGCGGAAAAUGGCAUUCCGACCAUGUGGUCGGAAAUCUUGCAGACAUAAUAGCGACAGGUAUUAGAAGUUAUCAGACAAUGCGAGGUGGUGUUCGUGCGACUGGAGCUCGCUACUAUGGCCGUGUCUUCAACGACUUACGACUGAGGAAAAGCGCAGUACUCUCCCCGGAGACCGAAUUUUUCCUACCUCCCGGGAUGCGGUGUGUCGUCAGCAUUGGUAGGGAUCGAAACCGGGCUAUGCAACUCAGUCCACCUGCUGACCACCGACUCGAUAGGUUCGAAGAUCUUAUUGAGUAUUCAUCGUCCACCGGUGUUAUUUGGUCAGCAGUAGCGCCGGGACUCCCACAACCCCUUCGAUUGUAUAAAAGUCGAAUCUACUGUAGGAUUAUUCGGAAUUUCGCCCGCUAUCGCGAAAAGUUUAAGAUCUUCCUUUCGCUCGGGGUCGGAUUGAUACUAGCCGUCGGGGUACAGUCGGCCUAUAAUGGACUGGAACACCAGCGCGGCCACCCUGACAGCAUGCGAGUACUCGCAUGUCCAUCCCAAUCGUCGCUUUCUCUAGUCAUACGCCUCAAGUACCUCCUUGUUUCGAGAGGCUCCGAUCGCAACAAGGACUACACACUGGCACUCCUCUGGACUGCGACUGACUUAUACUUGUCGCCCUUCUUAAUACCUCGUUUCGUGCGCGCUCAUUAUCUUCCAGACGUUUCGAGGAUCCUCUGUAUCAUACGUGUCGAGCCAGGGUUCGUCAUGCGGUGCAUAACCCCUUCACUCCUUCGUCUCGAUACCACCUUACGCACCAAACAGGGCGCCUCUAAGUCCACGCCGCGACUGUACGUGGCCCACUCAGGCGGGACCGCACGAAUCGGAGAGCGGUUAACCAGAUUUACAGUAAGCGGCCUGUACAUCUAUAGCAGAGCAAGCCGCCUAGGAUUUUCAAAUUGGUCAAUUUCUAGAAUAAGUGACGUCGACAUCCGCAGGUACGUAACUAAGCUACGGGGGUUCGAGGAAACCGGGAUCAUACCAGAGUUCUCGUCAGUUGAUUUAUCAUUCCGUGUAGGCGUAAUGGACCGCCAGCGGUGGGUGGUAAUCUCCGACAGUCCCAAAAACUAUACUGAACAUCACUACAUGGAGUCGGCCGUGUGUGGGGUACCAUCCCUAAAACUUUCAUCAACUUGCCUCGUGGUCACAGUCUACGGGGACAGGGGGGCUUGGGUGCAGUUAGCACAUAUUUACGCCACAUCUAUGUUCUAUAUUAAUUGGCUCGGCUACGUCUUACGAUCGAAGCGAAGCCAGGUAACAGCUGGGGCACAACCGCAUCGAAGGCAGUUUAUUCAACACUAUGGGAUCAUCAGUAUAGCAUACGGGUUUCUAGAAUAUGUGGGAGCACAAGCCGGGACAAAUUUAGCUUCCAAUACUAUAGCUACGGUGACGGCGUAUAGAGAUAGCUGUUGUCAGCCACGAGCGGUUCGCCUCCGGGCUGGGUUCCGCUGUCACUCACCAGCGUACGGGGACUCACAGGAUAUACAAAUAGUAUCGCUCCUAAUGCGUGAUGGUACUGUCUAUCAUACAAUACAGAGCAUCAACCACGGCCCAGGGGUAGUUGACAUUGCGAUAGGUAUUACGACGGAAGAACAGCACAAACCGCCCCCUCCGAUCGCGCCAUUGUGGCUGCGAAUCCGUGGUUAUCAAGUAGCAUCUUGUGCGUACAGUGUAUACACACGUGAAAAACUAACUCGACGAUGUCUAAUGGACGCUCAGUUAGCUCACCAUAGUACCAUGUAA'
##
##
##def test(x):
##    protein = ''
##    nucleotides = x
##    for i in range(int(len(nucleotides)/3)):
##        y = nucleotides[3*i:3*i+3]
##        if translation[y] == ' ':
##            break
##        protein = protein + translation[nucleotides[3*i:3*i+3]]
##    return protein