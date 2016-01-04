debug = True
if debug:
    f_name = raw_input("Please Input File Name:")
    f_in = open(f_name,"r")
    s = (f_in.read()).rstrip()
    l = s.split('\n')
    seq = l[0]
    s = l[1:]
else:
    seq = 'GACCACGGTT'
    s = ['ACAG']
    s.append('GT')
    s.append('CCG')

ls = len(s)
matrix = [[0] * ls for i in xrange(ls)]

def is_disjoint(s1, s2):
    pos1 = []
    for i in xrange(len(seq)-len(s1)+1):
        if seq[i] == s1[0]:
            pos1.append(i)
##    if debug:
##        print pos1,s1,s2
    for i in pos1:
        p1 = 1
        p2 = 0
        p = 1
        flag = True
        if len(seq[i:]) < len(s1)+len(s2):
            break
        if seq[i:i+len(s1)+len(s2)] == s1+s2 or seq[i:i+len(s1)+len(s2)] == s2+s1:
            continue
        while p1!=len(s1) and p2!=len(s2):
            if seq[i+p] == s1[p1]:
                p1 += 1
                p += 1
            elif seq[i+p] == s2[p2]:
                p2 += 1
                p += 1
            else:
                flag = False
                break
        if flag:
            if p1 == len(s1):
                if s2[p2:] == seq[i+p:i+p+len(s2)-p2]:
                    if debug:
                        print i,s1,s2,seq[i:i+len(s1)+len(s2)]
                    return 1
            if p2 == len(s2):
                if s1[p1:] == seq[i+p:i+p+len(s1)-p1]:
                    if debug:
                        print i,s1,s2,seq[i:i+len(s1)+len(s2)]
                    return 1
    return 0

for i in xrange(ls):
    for j in xrange(i, ls):
        matrix[i][j] = is_disjoint(s[i],s[j]) or is_disjoint(s[j],s[i])

for i in xrange(ls):
    for j in xrange(i, ls):
        matrix[j][i] = matrix[i][j]

for i in matrix:
    for j in i:
        print j,
    print
