debug = False
if not debug:
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
while i>=0 and j>=0:
    (i,j,tt) = track[(i,j)]
    #print i,j,tt,s1[i+1]
    if tt:
        result+=s1[i+1]
##if debug:
##    for i in track:
##        print i,track[i]
print result[::-1]
