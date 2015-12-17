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

s1 = 's'+content[0]+'e'
s2 = 's'+content[1]+'e'
len1 = len(s1)
len2 = len(s2)

t = {}
track = {}
for i in range(len1):
    for j in range(len2):
        if s1[i] == s2[j]:
            tt = 2
        else:
            tt = 0
        tm = max(t.get((i-1,j),0)-1,
                 t.get((i,j-1),0)-1,
                 t.get((i-1,j-1),0) + tt)
        t[(i,j)] = tm
        if tm == t.get((i-1,j),0)-1:
            track[(i,j)] = (i-1,j,-1)
        elif tm == t.get((i,j-1),0)-1:
            track[(i,j)] = (i,j-1,-1)
        else:
            track[(i,j)] = (i-1,j-1,tt)

print t[(len1-1,len2-1)]
i = len1-1
j = len2-1
#p1 = [len1-track[(len1-1,len2-1)][0]]
#p2 = [len2-track[(len1-1,len2-1)][1]]
p1 = []
p2 = []
##if not track[(i,j)][2]:
##    p1 = [len1-track[(len1-1,len2-1)][0]]
##    p2 = [len2-track[(len1-1,len2-1)][1]]
##    print "kkkkkkkkk"
it = len1-1
jt = len2-1
tt=[]
while i>=0 and j>=0:

    (it,jt,tt) = track.get((it,jt),(0-1,-1,1))
    if tt>0:
        p1.append(i-it)
        p2.append(j-jt)
        #print i,it,j,jt
        i = it
        j = jt
#p1.append(max(i,1))
#p2.append(max(j,1))
result = 0
for n in range(len(p1)):
    result += max(p1[n],p2[n])-1
print result      
