f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
n = int(l[0])
m = int(l[1])
ln = l[2].split()
lm = l[3].split()
a = []
b = []
for i in range(n):
    a.append(int(ln[i]))
for i in range(m):
    b.append(int(lm[i]))
temp = (n+1)/2
it = (n-1)/2
flag = False
result = []
mid = 0
for i in b:
    low = 0
    high = n-1
    while low <= high:
        if a[low] == i:
            result.append(low+1)
            flag = True
            break
        if a[high] == i:
            result.append(high+1)
            flag = True
            break
        mid = low+((high-low)/2)
        if a[mid] == i:
            result.append(mid+1)
            flag = True
            break
        if i < a[mid]:
            high = mid - 1
        if i > a[mid]:
            low = mid + 1
    if flag:
        flag = False
    else:
        result.append(-1)
    
for i in result:
    print i,
print

    
