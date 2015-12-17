f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
n = int(s)
single = []
temp = []
result = []
result.append([[1]])
result.append([[1,2],[2,1]])
if n > 2:
    for i in range(2,n):
        for j in range(len(result[i-1])):
            for k in range(i+1):
                for l in range(k):
                    single.append(result[i-1][j][l])
                single.append(i+1)
                for l in range(k,i):
                    single.append(result[i-1][j][l])
                temp.append(single)
                single = []
        result.append(temp)
        temp = []
nn = 1
for i in range(2,n+2):
    nn *= 2
single = []
temp = []
last = result[n-1]
for i in range(len(result[n-1])):
    for j in range(nn):
        k = j
        for t in range(n):
            if k % 2:
                temp.append(-last[i][t])
            else:
                temp.append(last[i][t])
            k /= 2
        single.append(temp)
        temp = []
print len(single)
output = ''
for i in range(len(single)):
    for j in range(n):
        output += str(single[i][j]) + ' '
    output += '\n'
print output

