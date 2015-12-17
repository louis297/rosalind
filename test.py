f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
lt = s.split('\n')
ltt = lt[0].rstrip()
ll = ltt.split()
n = int(lt[1])

single = []
temp = []
result = []
for i in range(len(ll)):
    single.append([ll[i]])
result.append(single)
#result.append([[ll[0],ll[1]],[ll[1],ll[0]]])
if n > 1:
    for i in range(1,n):
        for j in range(len(result[i-1])):
            for k in range(len(result[0])):
                single = (result[i-1][j])[:]
                single.append(result[0][k][0])
                temp.append(single)
                single = []
        result.append(temp)
        temp = []
temp = result[n-1]
output = ''
for i in range(len(temp)):
    for j in range(n):
        output += str(temp[i][j])
    print output
    output = ''
