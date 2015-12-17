import string
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
temp = f_in.read()
s = temp[:-1]
l = s.split(' ')
d = {l[0]:0}
for i in l:
    if d.has_key(i):
        d[i] += 1;
    else:
        d[i] = 1;
# print d
i = 0
k = d.keys()
v = d.values()
for i in range(len(k)):
    print k[i],v[i]

