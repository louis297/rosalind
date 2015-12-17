f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
n = int(s)
total = 1
for i in range(1,n+1):
    total *= i
print total
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
temp = result[n-1]
output = ''
for i in range(len(temp)):
    for j in range(n):
        output += str(temp[i][j]) + ' '
    output += '\n'
print output
