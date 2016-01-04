f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split()
nodes = int(l[0])
pairs = int(l[1])
l = l[2:]
dic = {}
for j in l:
    i = int(j)
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in xrange(1, nodes+1):
    print dic[i],

