f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
temp = f_in.readline().rstrip()
l = temp.split()
k = int(l[0])
n = int(l[1])
single = []
data = []
for i in range(k):
    temp = f_in.readline().rstrip()
    l = temp.split()
    for j in l:
        single.append(int(j))
    data.append(single)
    single = []

result = []
for a in range(k):
    flag = False
    for i in range(n):
        if data[a][i] <= n and -data[a][i] <= n :
            for j in range(i+1,n):
                if data[a][i] + data[a][j] == 0:
                    result.append([i+1,j+1])
                    flag = True
                    break
        if flag:
            break
    if len(result) == a:
        result.append([-1])

for i in range(k):
    for j in result[i]:
        print j,
    print

