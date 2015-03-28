def trie_construction(patterns):
    """ Construct Trie(Patterns) by iteratively adding each string from
Patterns to the growing trie."""
    trie = dict()
    count = 1
    for pattern in patterns:
        current_node = trie
        for i in pattern:
##            if any(i == k[0] for k in current_node.keys()):
##                temp = [k[1] for k in current_node.keys() if i == k[0] ][0]
##                current_node = current_node[(i, temp)]
##            else:
##                current_node[(i,count)] = {}
##                current_node = current_node[(i,count)]
##                count += 1
            current_node = current_node.setdefault(i,{})
    return trie



def prefix_trie_matching(text, trie):
    symbol = text[0]
    n = 0
    v = trie
    while True:
        if symbol in v.keys():
            if len(v[symbol]) == 0:
                return True
            else:
                n += 1
                if n >= len(text):
                    return False
                v = v[symbol]
                symbol = text[n]
        else:
            return False

def trie_matching(text, trie):
    for i in range(len(text)):
        if prefix_trie_matching(text[i:], trie):
            yield i

def trie_to_tree(trie):
    for k, v in trie:
        if len(v) == 1:
            branch = k+v.keys()[0]
            trie[branch] = v.values()[0]
            trie.pop(k, None)
            trie_to_tree(trie[branch])
        elif len()

string = "ATAAATG$"
a = []
for i in range(len(string)):
    a.append(string[i:])
b = trie_construction(a)
print b
#c = list(trie_matching("AATCGGGTTCAATCGGGGT",b))
#print " ".join(str(i) for i in c)
        

##def print_trie(trie):
##    for k, v in trie.items():
##        if len(v) > 0:
##            for i in v.keys():
##                f.write("%d->%d:%s\n" % (k[1], i[1], i[0]))
##            print_trie(v)
##        else:
##            pass    
##a = []
##with open("C:\Users\Bian W\Downloads\dataset_294_4.txt") as f:
##    for i in f.readlines():
##        a.append(i.strip())
##print a[0:5]
##
##f = open("result.txt", "wb")
##b = trie_construction(a)
##
##
##for k in b.keys():
##    f.write("0->%d:%s\n" % (k[1], k[0]))
##
##print_trie(b)
##
##f.close()
