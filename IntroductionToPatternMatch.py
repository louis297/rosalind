f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = (f_in.read()).rstrip()
l = s.split('\n')

count = 2
#nodecount = 2
cm = []
node = []
for i in range(10000):
    cm.append([])
    node.append(' ')

for seq in l:
    now = 1
    for nuc in seq:
        flag = True
        for nextnode in cm[now]:
            if node[nextnode] == nuc:
                now = nextnode
                flag = False
                break
        if flag:
            cm[now].append(count)
            node[count] = nuc
            now = count
            count += 1

for i in range(1,count):
    for n in cm[i]:
        print i,n,node[n]
                
