f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
n = int(l[0])
ln = l[1].split()
a = []
for i in ln:
    a.append(int(i))
result = 0
b = a[:]
a.sort(reverse=True)
#i=n-1
#while i>0:
n -= 1
for i in a:
    temp = b.index(i)
    result += n-temp
    b.remove(i)
    n -= 1
    #a = a[:-1]
    #i -= 1

print result
