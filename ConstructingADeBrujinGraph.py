f_name = raw_input("Please Input File Name:")
#f_name = raw_input()
f_in = open(f_name,"r")
s = (f_in.read()).rstrip()
l = s.split('\n')
##name = []
##content = []
##flag = False
##for s in l:
##    if s[0] == '>':
##        if flag:
##            name.append(name_temp)
##            content.append(content_temp)
##        name_temp = s
##        content_temp = ''
##        flag = True
##    else:
##        content_temp += s
###name.append(name_temp)
##content.append(content_temp)
dic = {'A':'T','T':'A','G':'C','C':'G'}
cd = {}
def rc(seq):
    r = ''
    for i in seq[::-1]:
        r+=dic[i]
    return r
ll = []
for i in l:
    revc = rc(i)
    cd[i] = revc
    cd[revc] = i
    ll.append(revc)

l1 = zip(l,range(len(l)))
l2 = zip(ll,range(len(ll)))
content = l+ll
content = list(set(content))
length = len(content)

r = set()
pre = []
suf = []



for i in content:
    r.add((i[:-1],i[1:]))

rr = []

for i in r:
    rr.append("("+i[0]+', '+i[1]+')')
    
rr.sort()
for i in rr:
    print i
