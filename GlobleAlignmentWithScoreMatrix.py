f_in = open("blosum62.txt")
s = f_in.read().rstrip()
l = s.split('\n')
aa = ''.join(l[0].split())
b62 = {}
i = 0
for single in l[1:]:
    temp = single.split()[1:]
    for j in range(len(temp)):
        b62[(aa[i],aa[j])] = int(temp[j])
    i += 1

f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = (f_in.read()).rstrip()
l = s.split('\n')
name = []
content = []
flag = False
for s in l:
    if s[0] == '>':
        if flag:
            name.append(name_temp)
            content.append(content_temp)
        name_temp = s
        content_temp = ''
        flag = True
    else:
        content_temp += s
#name.append(name_temp)
content.append(content_temp)

s1 = content[0]
s2 = content[1]
len1 = len(s1)
len2 = len(s2)

t = {}
for i in range(len1):
    t[(i,-1)] = -5 * (i+1)
for i in range(len2):
    t[(-1,i)] = -5 * (i+1)
track = {}
for i in range(len1):
    for j in range(len2):
        tt = b62[s1[i],s2[j]]
        tm = max(t.get((i-1,j),0)-5,
                 t.get((i,j-1),0)-5,
                 t.get((i-1,j-1),0) + tt)
        t[(i,j)] = tm
##        if tm == t.get((i-1,j),0)-1:
##            track[(i,j)] = (i-1,j,-1)
##        elif tm == t.get((i,j-1),0)-1:
##            track[(i,j)] = (i,j-1,-1)
##        else:
##            track[(i,j)] = (i-1,j-1,tt)
print t[(len1-1,len2-1)]

##for i in range(len1):
##    for j in range(len2):
##        print t[(i,j)],
##    print
