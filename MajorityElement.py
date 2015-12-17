f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
f_read = f_in.readline().rstrip()
l = f_read.split()
k = int(l[0])
n = int(l[1])
data = []
for i in range(k):
    f_read = f_in.readline().rstrip()
    l = f_read.split()
    temp = []
    for j in range(n):
        temp.append(int(l[j]))
    data.append(temp)

half = n/2
result = []
for a in range(k):
    bucket = [0] * 100000
    flag = False
    for i in data[a]:
        bucket[i-1] += 1
    for i in range(99999):
        if bucket[i] > half:
            result.append(i+1)
            flag = True
            break
    if not flag:
        result.append(-1)
for i in result:
    print i
    
