f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = (f_in.read()).rstrip()
l = s.split('\n')
seq = l[0]
k = int(l[1])
ll = l[2:]
loc = []
length = []
for i in ll:
    t = i.split()
    loc.append(int(t[2]))
    length.append(int(t[3]))
l = zip(loc,length)

sl=sorted(l,key=lambda t:t[1],reverse=True)
 
