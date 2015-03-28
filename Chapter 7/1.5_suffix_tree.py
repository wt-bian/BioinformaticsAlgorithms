from suffix_tree import *


string = "TTGGGCGTTCGCAAAACCTTGCAAACCTGTGCACCACACAAATTAAGATTCTGTCTAACTGCAGACCCATATTTCATTGAGCGCAACCGTGAGTTTCTAAGTTACAAATGGATCTGTTCGACTTGCAGTCATAGGTGATTTATAATGCTACGCAGGACAGAGTGACATCTTTGGTGCTCCACCGCCTCCCCATAAAAGCGCGCGTGACTTCTTCTTGGGGGGCATATCCCTCCAGGGCTACCCCTTCTTTATACGTCTTAAGGGAAATGATGCTATGTTAACTGTTGCTAGAGTCCGGCGTGCTGATTGTATAACCAGGCCTCTCACATATCGCAGTAAGCTAGTCCGCTTACCCTCAAGTAGCATCCAAACCCATGTTGGCTTATGCAACTAACCCTCCTGACGCACGATTGGCTAAGTCTCATTCACCTGTACGTGCCACCGTAGCTACCTGCGCTATGCTGAGCCCACCATGAAGACTTACCTAAGATCTGATATCGATCCAATGATTCGGGGGTGGACGTCGTGATTTCACGACCGGTGACTACCATGCCTATGAAGCCATTATGTGGAGACGAGACCTTCTGGTGCAGCTGCATCTCGATGGGGAGATGGCCAACTTCGCACACATTGACGAGAAAGACTAGTACACGCGGGTAGGACATGGATTCTACCCGAGAAGATGACTTCTCCACAGTCCCATTGGAGATAGTAGCACGGTTGCACAAGCGAACTAGGGGAGGTTAATTGAGGGGCAGTCGAAGGGTACGAGCTGCCTGAGCCGGCTTTGGTCGCCATGGATATATAGATCGGGAGCGGCTAGATGGCTCTATTTGTGTTGCCATTGCACCCGCTTCATACGGGCGGGGAACCTACAACACTGTTCCGTGTCTAGCAACAGCGGCGACGCCTCACAATCATCAAAATATTGGGCAGTATGCTGCGGCGTGATTGATCCTAAACTGGGATCGCTGAACGCCGTGCGCTATTTTGGACAGTGAGGGAGCTGAAATTACTGTACCACCCCGTACGCCGTGCCTAGCAACTACTCGGTTCAATTACGTCTGTACTCGGTATTCCGCGGTACTGCCAGCTCTGTTATTTGGAATCCACCGGCGGAAACTTTCCTGTACATCATGGACCGCTAATCCAATTCGACCCCTCTGGTGAGGCCCACAGGGTCCCAGAGGTGAGACAAAAAATGTACTAGGGTTCCATGCCAACTGGACGGTCTGACCTCCAACTCACCAGACAGGGTTAGAGGTCCGTTTTCTCGTTTCCACCATTCCAGCCTCGTGCCCATAGCGCAGATTTGGAACAATTGTGAACCCTCAGCCGTGCATAGGATCATGCATTACTCGGAGTTTGTCCAAGTGACATGTGGAACTGGAACCACACCGAGCGGAGTGCTCTGCCTGATATAGGCGCTCATGGTGCGGCTAGTACGACTGCAGCGGTTTGCTAAGGCGGCACAGTTCGGAGCGTCTACCCAACCAAAGTCCAGTTGTTGCACTATGCCTGTCGACAGAGCGGGCTAACGGACCTTCATAGCACCTCGGCCAGTGCCATTCGAAGTCATTGTACGGCGTGAGAGTATGCCCCACCCTACAGGGCACGAGGAAGAGGTGTCATGAAGTCGACTGTGCTAAGTTCGGCGAGCAAACTTTCTAGACGAGGTATTTAGGTAGGCGTCCCCCCTGGATAGTGGTCGATGTGCTCAAGACTTCGGGTCTGAAACAAGTGGCGCTGTGTAGAACGACGCATTGACAAACGCTATGTTTATGCGGACTATAGGGTTATTCTTCGTACCACGTGTTACTGATTTGCAAGTGTCCGAACTCGGCACGAAACGAACCTATGATTGAGGCTAGCTATTGGGGATGTTCGCTCCGGACTCCCGACCAGCCGTCTGAGAGCAAGAACTGGGGTGCCGTGGTTTCTTATATTTTATTGTAGCGCTCACAAGTTCTAAGCGAAAAGAGTGCTGTAGAAGCTGCGTGGACAACTTCTTACGTATTTATTACTCTCCCCATTTGGCTCGAAGTACAGCTCACTGGTGGGGACTGCGCTTTAAGTGAGAGAGTGATCTCTGAAGGGTCACAGCCCGCAGTTAGAAGCTTCCCTTCCCCTCATCTCGCATAGAGATGTCGCAAACCATTTTCTGCAACAGTTAGATTGTGCCCGAGATTAATTGGCCTATCTTACGCGGTATACTCCCGAATAAAGAAGCTGGTGGTCCGCCTGGGGAGTCAGTCTTAAGCATTGATGCGCGGCATAGGCACTTTTGATGTAACAGCATTGATAGCTGACTGAGAGAGCGTTAGGCACGAAGCATCCATTAGCTCAGTTGCTCCACCAACAGCAAGTCGAGGCTCTTTCGGTCCGTAACCTATCGGGTTTGTCACCCGCCTTGTCTAGGGGAACCCATGTCTAGTGGTATGGTTTTAGGGAATTGGATGACACGTTGTCCTCTACGGGGAGAGTGAGCAACCGTCGTTCGCGTCTACTTTTCCCTAGATTGGTGGGGAAAAAAAGTATGTCAAGCACAACCATTTAGCCTGATGGACCAGATAATGCTGTAATATGAGCCCGTCGTACGAACTCACTCAGGTGTACAGAGGCGCGGGGATGTCGTTGATGCGCCCCGTCCGTACACGGACCAACACCCCGCTCGAGGAACCCAGGCTCCCTCTATTTATTAAACTGCCCAGAATAAGTGTGCTGGCACCGCATTCGTACATCCGGACGGTTGCTTCTGAGGACATGAATCTCGTGCCCACAGCTTAAGACGTTAGCGCGGACGAGTCCCACAATTGTATACCCGGCTTGTTGCATAAGGCGTGACATTTGGGCCCAACTATATGTACACGTGTGGGGACCCTGCTCGCATTTGGAGGAGCTCGGTGTTACAGTCAACCGGGGCGCTGTACGGGTTCTTTAGTGTGGTGGTCCTTACTGGTAGCCCCTTTATGCCAAGGCCTATATACTCACAGCGCGCGTAACGTCCACCGCGTGCTCTAATTCAAGTGCCGTACATGGTCTGGCATGGCTAGTTAAACGTAACTGGTAGTGAATATGTTTCATAACCTCGAGAGGTGTAGTGTCGGGGTATAAATGGCGTTAAACCACAGGCTGAAGGCATGGCGTACCTTAGTGAGCACGGATAAAATCGGAGCCATGACCAGCCTCTGTATCAATGCGTGTTCCGCCATGATTACATAAACGGGGCAGTACACGATATCTCTTCCTGTTAGACGCCCCTAACGCAAGGATCTGTTGGCAACTGCCGCTAATACGTTTGTGAGCCATAGAATCCCATAGCACGCTAGGGACTTTTGGTTGGTCCGCGCTCTTCCTTCCAGAGCGCCCGCTTAGGCATTGAGGGGCGAAGGTTACAACCGTGTTAGCGGGTCGTCGTCGTTATTTGGCATACAGGGGAGCATTATACAGTTCTTAAATGAGAGAACCGGTACTTCACGCGAGGTTTACAGTACAGGAATGAGCTCGACACTATATCCGTATAGCCATGTGAAAAGTGTGTGCTCTGTCCGGCGTCACGCTGCTCCGCGAAGTATCTATGGCTCTTTTGGTGCTCCACCGCCTCCCCATAAAAGCGCGCGTGACTTCTTCTTGGGGGGCATATCCCTCCAGGGCTACCCCTTCTTTATACGTCTTAAAGAGAGGGACACGGAGCTGGTGGCACGACAACTTCCAGCGCGATCGACGACTTTTGGAGTCAGGGTGGCAATTCATCGATACTTTTTCGGCGGAATGACGTAGTGAGACCCATTGGCTGAACTTGAGGATGTATGGGTTGAATGCACGGTGACCTAGAGGTTCAATTCCGGAAGACGGACCAGACCTGCTAACGCAGGGGCTACGAACACCCTTTTCTTTAGCGCGCACGGCACATAACATTATCGCTGAAATGATCGACTCTCCTTTTTTCGGGGTACTGCTGGTTTTGCTCCGTATCCCCGCATAGACAACAGTTTTAAAGTTGGGTATAGCAAGGTTGTTAGTAAGGCTGGCGGCGACCTACAAACCGGTTGCTTGCGACGTAATAGGTGACACGACGTAATCCTTTGCTTGTGCTGTCGCGTTATCTATACGCATTAAAGAATTAAAGTTTCTAGGTGATGTCATGGTTACGGGTCCGCCCTAGTACGTCCGAACAAACCTCGACCATGGTAGTCCTAATATTGCCCATACCGTGTCATCCATGTTTTTTTTGACAAGGTTTCATAGTCGGCCTGAGAGGTTCATCATGCCCCTTTGTGGATCTGCTGCGCGTGCGAGCTACATTCGGACTTGGTGATCAAAATGTCCCCCGCCCAAAGCTAGAGTCGCTTACCTGCGAGGTCCGAGCCCACGCCAAGCTGCGGCGTGGTGCCAATCGGTCCTGCATAACTATCAGATCAACGGCATCGCTGATAATCGGTGGTTGTGCGTATTTATCTACTGTATGTGTCTTCGTCCCACGCAGCAATGGAAACCCTTGTCATTAGAAATTTTTAAGATAAGAACCGCGGCCGGGCGGAGTCAGCTACGAAAGCCTGCGGACCACTCGGCGCCTTATGGAAGAAAGTCCCTGAATTTACCCTTCAGAAAACCTATGTAATTACTACGTGATTGGGATGATGTCTTCCCACCTGATTGACGCGAGTGTGTTATTTCCGTCTGTTTGGCTGGATAGTTCGCTGGAGCACTAGGGAATGTCGTATCCCATATGAAGGCGACCTATCTCCTAGGGTCGATACTCATAGGTGTCCATGGGAGCTTGCGGGCTGGGTGAGGGCCATCATTATTTAAATTCCAGGTGGTTCACCGGCAGTCAACCGCTAAGGCCGATCCGCGAGTGAAAGTAACCCCCTGGGGATCGCCTTCCTTTGCTAGCTTCGCCCCAGGGTATTTCTAAGCAGAGATCATATAAAGTCTGATCGTTCGCGTGTAATGTTGATGGGAGACATGGTCAGACGGAGTTCTCCTCCAAAGTACAGACAGACGGATGTAGCTCGGTTAACCTCTCCTCATGTAGCTAGGTCTCATGAGTCGATTTGATTACGTGGATTCCATGTAAAGACACTCCTCCGCCAATCACTCGAGATGACACGCTTTTCATATGCACACACTTGTAGCCAGAGCCGTAGCCCGACTAACTGACCCACTCCCCACTCCTTCCGGTGTCGAGGATTTCGACCTCGCGTGCAGAGACTCACAACGAGATTCGCTCAAATGGAACCATCGAGCTGCACATATGGAGGACGGTGTCGGAATGGGGCTTGAGTAACGAGGATCATAGACAGGGGACAAACAAGTGAAGGGCTATGATTCTCTATATTGCTCTAATCATAGGCATGGACGGACGATTACCTCGCCTAGCCTTCGGAGTTATAAGAATGTGTGCACGCCAACTCGGGTGCTCCATGACAGGACATACTATTCACGTGCAACGGATTGCTGTACAGTGGCTAGCGTAGGAGTCTCGAGCGCGCCTAGCGTCATAAGGCCCTGTCCCCCCTACGTACTTGAGAGGGGGTGGTGTTAGCGTCCCCATATCCGCCGCGGGGGAGGTCGGCGGCTCTAACGGCCGATTAGTGCTTTGCGATGCGGTTGGTCTTAAGTTTTGTAGCTAGCACATCTGAAGGTAACAGTCGCAAACTGGGAATTATAGTCGAGTTCTCCAGCGGAGGGACGTCTCCGTCTCGAACTCGGATCGGGATCTTGCCTTCAATGGTCCACGCCGGGGGTTACAAACCTCTGGGACGGGTCTCGCCAAATCGAAGCGATTAGAACTTCATCTTATACGTGTGTAGACGCCAGCAAGGGCAGCGAGCAGTACCCCAATAATTACATGGCTTCCTATCTACGTGATTTTTCCACGTGCCATCTTAAATCACAAGCAGGCGGTCTAGTGTGCCAGGCTAATCTAATCTACCTCATAAGCATTTCCCCTCCTCGATTCGTGATGGAGCAAAGGATCTGTAGCTGTTAAGCGATTGGGGGAACAAGCGAGCTAACGATTCGGGGGTAAAACTCATCCGGAGTGTCTCATGTGCTACAACTCCGCGTATCCTGGGGTATCTTAATTGGGGGCCGAGGGTGGGGAGTGAGATACAAGGACGAATGGTCTAGTTTAGCGAACTTGTTAAATTTTGGCGGACGTTGGCCCTTTGAGGGAACTGTCGTAGACGGGATCCTGTGTCGGAGACTGTTCCAGTTCGGAGGGTAGTCTATGGTTCGTCTACAAAATGGACCATGAGTTCCCCGCCTGTCCCGTTTGCGTAGATGACCCCCCACCCCAGGGACATGCCATAGTCATAGTCTGATTACGTAGTCGATTGGCCGCGAGAACACGACGCTACCCTATGTCGTCCAAATCAATATCGACGCAAGTATACGACAAATAGCGGAACCTGAGGACAGCTACCTCAACGCACCGGTCGACACAGTGTACACCGAGACGCGTAGTCATGCTACTGCTGAGTAAGGTCGCCCTGTAAATAGCTCCGGCCTCAACCGAGGGCTATCAGACGGTGCAAGCGTGACTGCTTAATCAAAATACCCCTTTGACATTATCAACTCGGACAGAACTGCTATATGGTCTATTGTAAGTATATGCGGCGTCAGGGTAGATCTTTGGTGCTCCACCGCCTCCCCATAAAAGCGCGCGTGACTTCTTCTTGGGGGGCATATCCCTCCAGGGCTACCCCTTCTTTATACGTCTTAATACACCGTTCTCCCCCATACAGTCACGTCGTAAGCACCGAAGTCCTAAGGACGGCGGCATTACTGCAGTGATGAGTCCAGGAGATATTCAACTTCGTAGTCTCTTACGGCAAAAATTTTAATATAGCTAACTTATCTAAAACCCACGAGATACTCTCGCACCCACCTGGATGGATGCGATAAAGGCCAGCTCTCTCCTAGGTTCTCATTGCATAGTGGTTAACCACCCTCTACTTGGCCTCATTCCGTGGCTGGTTGGTAAGCAAGCAAACCTAACGGGCTGGTACTTATCGCTGGCCAAAGAGGGACCGACCCGCTAACGTAATCTAACCAGGTCCAGCGGGGAGTGCGCTCGGTGCGGGCCCTCGTGGCGTCCGCTGGGCGCAGAACATGTGAGTCGGATCCTTGACACACAATCGTCTCAAGCGAAACAGTAACGCGTCATGAGTCCTCTTAATTGCTCGGGTCCTGGGTCGGAATTCTCTATAAAGTCCGGGGCCAATCTTGCGGACCGCTGGACAACTCGAACCATCCACGCTAAAGGCACCGCAGACATCTACATACAGTCTCTGTAACATGCAGGTCGTATACTGTCACGTGAGGCCCCAAACTGAGGCCATGTGCGATATCTCTACCCCTAGAAGAGAGAAGTTCAATTGACTATCTTAAGCCTAGCAGCAGTCTCTGTTGTGATATCAGCTAGTACTACAGGTTCAACGATCTGTTAAAGAGTCTTAAGTATAGGTTGACTTCGTAGCCCTCCAACCGTACGAAACGCAGGGAATTGTGATATCATTTCGTCCTCTACCGAATTGTCAATAACAGGGCTTAGGTAGTCACCGCTTGCTCTCCAACGATGTCGTCGACTGAATCGAAGCGAGTCAAGGTAAAACATTCAAACGTAGCGAAGGCGATTCAATTGGGTGTCTACGAAGACGCGTATCGGGTGATGGAACATAGTCCCTGCGCCCATGCGAGGCCATAGCTCACAGCGTTAGTATTATAGGAGAACCCGAGGGCCCCCCCTTTACGAGTATCCTAGCGCAAGAGAGGAACATTACTTTTGGGTAATAATCAAATATGCTATCGGCTTATACGTTATTAACTTCTTGCTGGGCGGCTATCAAATCATCTCAGAATTCGTGCGGTATCCACATGGGTGGATGGCTGGACCATAGCCTTTCTGTATTCAGGCAAATTCGGAGAGGCCAACTGCCGATATCTCATACGGGTGTCATGTGAGGGGGGTGGGCAGGTTACATGCCGTGAAATAGCACCAACAAGGGCGTGGTTGTGATTCAAGTCTGTATACCAAATCGCCTCAAGACTGCCCCCCTCACTAATGACGGTAGTAGCGATACAGTGAGAAAGGCTTTCATCCAGAGGAGGCGGTTTTCAGTCACATACCCGTAACCGCGGTTGTGTTATCCCGCTAGGCTAGTCGTACTAGTGTGACATTCATCCAATAGCGACTGGGGCTACAAAAAGGTAAATGAAAACCAAGCGACATAGTGGCTCACTGAACTCTTTACGATCATCCCTCCTTGTACGTGTCCTGCCGCAAGTTATTTGCGTTATAGCGCCATAGCAAGGTAGTGGTAGCGAACGGGTCGTCGAGCCCAAGAAGCGAAGTGAAACCTAGTGGATGGAAAGTTCAAGCGCGACAAGTTTCAAGAACTAACAAAAGTGTTGTGCCATAACACCACCCGGAGAAGTGAAGACCGAAGAAAGTTAACCTCTGGACAAACTAAGGATGGGCTCTAGTAACGGTAGAGTACACCACAGTAATAAGGTCCAAAGTCTTCATACCACTTGATTGGGCGTATCATGCCACATGGTCTTAGTTAAGCTTGAACGCTAGTCCAGTAGGTTGTCGAATGCGGCTATCTGCATTGCCAAATGGTTCACAAGTTGGAACAGGCGCATACGTGATTCGTCCTACGGTCGAGAGGTTTCATAAGTATAGTTCACAAAGTGCTTGTCAGCTGGTGATTCGTGTTTCAGAAAAAACACGAATTGTACGCGGAAAATAGTATCACGGTGTGTTCCTAGGCCCTCGCGCTTTTAACGAACCAGTTCTGTCGATCTGCGATGTAGCTGTCAAACCATAGCAAATGACTTTAGTTAAGGACTTGATAACTATCCGTTTACCTCACTGTAGGAGAGGATCAATACTTTAGCAGACGCGAGGTATGACATCTTGATTTACAGGTCGACTGTAATATCAATTTCTAGGCTGCCACAGGGAGCAATGGTTGGATAACAGAGATCGGCGCGCGTCCCTGTACCCGACCTGCTTATCCCGGCATTAAACCATCTCTATCCCGGGGTAAGCAATGTATGACTCTAGCGAGTATTAACTTGTAGCTTATCTAGCCAGAACAACTGAGCGAATGATGAAGTGCTGATGCAGGCTGCATGTGCGTTTTCGGAAGACTCCCGGTAGGAAAGAAGTCAATGCCTGACTACGTTACGTGGCCAAGTAGGAGCAGCATATGCGACCGAGCGGCAGTCCACACCTGTCCGGAGTTAAACCGACATGTATCCCGAAAGATCGGGTGCAGTGCCAGGCTAGAGGGAAGAGCAGCCGCATGTGACATCATTGCTACCGCCCTCCACTCCATACCATGCCCATTCACCTTCATGAACAGTGTCTTTAAGTTTGAGATGGATGGAAGCGCTATCCACACATCGTCTGAATGCATTCCTCCCGATTATTTTCAACAATGTCATCTGTTGCAGCCTGTGGGGCTGTGACGTTCTCAACATTGATCCAAACGGACCAGTGGACGTGGATCATGATAATAGAGGTTAAACCACGCTCTTGTGGCGGCGATCTTATCTACGAGATAGTGCTTAATAGTCGTACACGCCTCAGATAGTTTGCAATCTACCTAGAACTACCAGTATACGATACATTTTCCACATCTGTTGTACCCGTAAATACACCTCGGATCATAGGGCTCGGTTCTCTTGATGACTTAGTATGAGCGACGCCAGCTGATAGTAGAGGCCTTTCCCCTCCAGCCTGCTCTGGTTCGGCAGTGAAGGTTGTATTCCCATCAATCCTGGCGTCTAGCGCATACGGCTACATTGTTGGCGGAGAACGTCAGTCCCCGGGTGAGGCTTGGGCGAGAGGAAGGCTGTGAAACGAGAGGCGGCAGTATAAGTTGTCCATCTCGAATGCCGACTCCCAAATGCAAGTATTGTTTCGGCCCGATGTCGCCTAGGGATCCGCCATAACTCTTAGATCTCCGGGCTAATGATCCCCAGGAGAACGGAACCAAGTACGTACCCAACAGGCAGTCCTCATGTACAGATGCGACTACAATGTCTTCGCGGTCCCCCCCATATCAGTACCGCATGAACAACCTAAATCTGTAATGACGACTAGCGTCCTCTCGAGACGACTGGCAGCGGAATCGCCTTAGACCACACGCTAGAGTTCTCTTATTGGTAATTGCCAGCGTGAAGCTTACCGCAAATCGCTAAATGTCCCCCATTTCGATTCTGATTCTCGCTGAATGTAGAACCTGCCTTCTCGACG"
stree = SuffixTree(string)

a = repr(stree)
b = [i for i in a.split("\t")[7:] if i.endswith("\n")]
c = [i.strip() for i in b]
d = sorted(c, key = len, reverse = True)
for i in d:
    if string.count(i) > 1:
        print i
        break
    

##print "\n".join([i.strip() for i in b])
##f = open("result.txt", "wb")
##f.write("\n".join([i.strip() for i in b]))
##f.close()