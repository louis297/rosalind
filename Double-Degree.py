f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split()
l = [int(a) for a in l]
nodes_amount = l[0]
lines = l[1]
nodes = l[2:]
dic = {}
for i in xrange(lines):
    (node1, node2) = (nodes[2*i], nodes[2*i+1])
    if node1 in dic:
        dic[node1].append(node2)
    else:
        dic[node1] = [node2]
    if node2 in dic:
        dic[node2].append(node1)
    else:
        dic[node2] = [node1]

for i in xrange(1, nodes_amount+1):
    if i in dic:
        t = 0
        for j in dic[i]:
            t += len(dic[j])
        print t,
    else:
        print 0,
