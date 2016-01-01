debug = False
if not debug:
    f_name = raw_input("Please Input File Name:")
    f_in = open(f_name,"r")
    s = (f_in.read()).rstrip()
    l = s.split('\n')
    s1 = l[0]
    s2 = l[1]
else:
    s1 = 'AACCTTGG'
    s2 = 'ACACTGTGA'
len1 = len(s1)
len2 = len(s2)

t = {}
result = ''
track = {}
for i in range(len1):
    for j in range(len2):
        if s1[i] == s2[j]:
            tt = 1
        else:
            tt = 0
        tm = max(t.get((i-1,j),0),
                 t.get((i,j-1),0),
                 t.get((i-1,j-1),0) + tt)
        t[(i,j)] = tm
        if tm == t.get((i-1,j),0):
            track[(i,j)] = (i-1,j,0)
        elif tm == t.get((i,j-1),0):
            track[(i,j)] = (i,j-1,0)
        else:
            track[(i,j)] = (i-1,j-1,tt)

print t[(len1-1,len2-1)]
i = len1-1
j = len2-1
pos1 = []
pos2 = []
while i>=0 and j>=0:
    (i,j,tt) = track[(i,j)]
    #print i,j,tt,s1[i+1]
    if tt:
        pos1.append(i+1)
        pos2.append(j+1)
pos1.reverse()
pos2.reverse()
print pos1,pos2
t1 = t2 = 0
for i in xrange(len(pos1)):
    result += s1[t1:pos1[i]] + s2[t2:pos2[i]] + s1[pos1[i]]
    t1 = pos1[i]+1
    t2 = pos2[i]+1
result += s1[t1:] + s2[t2:]
print result
