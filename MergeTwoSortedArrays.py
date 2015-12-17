f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
f_out = open("MergeTowSortedArraysOutput.txt","w",0)
s = f_in.read()
s = s[:-1]
s.replace('\n',' ')
l = s.split()
i = 0
n = int(l[0])
a = []
b = []
result = []
res = ''
ia = ib = 0
flag = False
for i in range(n):
    a.append(int(l[i+1]))
m = int(l[n+1])
for i in range(n+2,len(l)):
    b.append(int(l[i]))
for i in range(m+n):
    if a[ia]<b[ib]:
        result.append(a[ia])
        ia += 1
    else:
        result.append(b[ib])
        ib += 1
    if ia==n:
        break;
    if ib==m:
        flag = True
        break
if not flag:
    for i in range(ib,m):
        result.append(b[i])
else:
    for i in range(ia,n):
        result.append(a[i])
for i in range(n+m):
    f_out.write(str(result[i])+' ')
f_in.close()
f_out.close()

