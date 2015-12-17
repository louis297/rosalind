f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
sn = f_in.readline()
sn = sn[:-1]
n = int(sn)
s = f_in.read()
s = s[:-1]
l = s.split(' ')
a = []
result = 0
k = 0
for i in range(n):
    a.append(int(l[i]))
for i in range(1,n):
    k = i
    while k>0 and a[k]<a[k-1]:
        (a[k],a[k-1]) = (a[k-1],a[k])
        result += 1
        k = k - 1
print result
