f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
temp = f_in.read().rstrip()
l = temp.split('\n')
n = int(l[0])
ll = l[1].split()
A = []
for i in ll:
    A.append(int(i))

