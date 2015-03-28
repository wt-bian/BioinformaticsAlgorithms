def burrows_wheeler(string):
    """ Burrows-Wheeler Transform Construction """
    matrix = []
    for i in xrange(len(string)):
        matrix.append([string[i:], string[i-1]])
    matrix.sort(key=lambda x:x[0])
    return "".join(i[1] for i in matrix)
      


def inv_burrows_wheeler(string):
    """ Reconstruct a string from its Burrows-Wheeler transform."""
    last = []
    temp = {}
    for i in string:
        if i in temp.keys():
            last.append((i, temp[i] + 1))
            temp[i] += 1
        else:
            last.append((i, 1))
            temp[i] = 1
    last = tuple(last)
    last_dict = {}
    for i in xrange(len(last)):
        last_dict[last[i]] = i 
    first = sorted(last, key=lambda x:x[0])
    result = ""
    print first
    position = last_dict[("$",1)]
    for i in xrange(len(string)):
        char = first[position]
        result += char[0]
        position = last_dict[char]
    return result
    
def bwt_last_to_first(string):
    """ Return first, last and last_to_first."""
    last = []
    temp = {}
    for i in string:
        if i in temp.keys():
            last.append((i, temp[i] + 1))
            temp[i] += 1
        else:
            last.append((i, 1))
            temp[i] = 1
    last = tuple(last)
    last_dict = {}
    for i in xrange(len(last)):
        last_dict[last[i]] = i 
    first = sorted(last, key=lambda x:x[0])
    result = ""
    last_to_first = []
    position = last_dict[("$",1)]
    for i in xrange(len(string)):
        char = first[position]
        result += char[0]
        last_to_first.append([position, last_dict[char]])
        position = last_dict[char]
    last_to_first = sorted(last_to_first, key=lambda x:x[1])    
    return [i[0] for i in first], [i[0] for i in last], [i[0] for i in last_to_first]

def bwm(first, last, pattern, last_to_first):
    top = 0
    bottom = len(last) - 1
    while top <= bottom:
        #print top, bottom
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            sub_last = last[top:bottom+1]
            if symbol in sub_last:
                #print symbol, sub_last
                topIndex = sub_last.index(symbol) + top
                bottomIndex = ''.join(sub_last).rfind(symbol) + top
                #print "index", topIndex, bottomIndex
                top = last_to_first[topIndex]
                bottom = last_to_first[bottomIndex]
            else:
                return 0
        else:
            return bottom - top + 1
                
string = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
patterns = ["CCT", "CAC", "GAG", "CAG", "ATC"]
#print inv_burrows_wheeler(string)
#first, last, last_to_first = bwt_last_to_first(string)
#for pattern in patterns:
#    print pattern
#    print bwm(first, last, pattern, last_to_first)

with open("bwmatching.txt") as f:
    string, patterns = f.readlines()
    string = string.strip()
    patterns = patterns.strip().split(" ")
first, last, last_to_first = bwt_last_to_first(string)
result = []
for pattern in patterns:
    #print pattern
    result.append(str(bwm(first, last, pattern, last_to_first)))
print " ".join(result)
