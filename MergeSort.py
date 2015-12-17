f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
n = int(l[0])
ln = l[1].split()
a = []
for i in ln:
    a.append(int(i))
a.sort()
for i in a:
    print i,
print

