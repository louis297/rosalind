debug = False
if not debug:
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
    


for i in xrange(ls):
    for j in xrange(i, ls):
        matrix[i][j] = is_disjoint(s[i],s[j])

for j in xrange(ls):
    for i in xrange(j, ls):
        matrix[j][i] = matrix[i][j]

for i in matrix:
    for j in i:
        print j,
    print
