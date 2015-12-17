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
    if data[a].count(0) >= 3:
        result.append([0,0,0])
        print a
        continue
    temp = data[a][::]
    temp.sort()
    flag = False
    for i in range(n-2):
        test = temp[i]
        imin = i+1
        imax = n-1
        while imin < imax:
            sum3 = test + temp[imin] + temp[imax]
            if sum3 == 0:
                result.append([test,temp[imin],temp[imax]])
                flag = True
                break
            elif sum3 > 0:
                imax -= 1
            else:
                imin += 1
        if flag:
            break
    print a
    if not flag:
        result.append(-1)

for a in range(k):
    i1 = i2 = i3 = 0
    if result[a] == -1:
        print -1
        continue
    elif result[a] == [0,0,0]:
        i1 = data[a].index(0) + 1
        i2 = data[a].index(0,i1) + 1
        i3 = data[a].index(0,i2) + 1
        #print i1,i2,i3
    elif result[a][0] == result[a][1]:
        i1 = data[a].index(result[a][0]) + 1
        i2 = data[a].index(result[a][1],i1) + 1
        i3 = data[a].index(result[a][2]) + 1
        #print i1,i2,i3
    elif result[a][0] == result[a][2]:
        i1 = data[a].index(result[a][0]) + 1
        i3 = data[a].index(result[a][2],i1) + 1
        i2 = data[a].index(result[a][1]) + 1
        #print i1,i2,i3
    elif result[a][2] == result[a][1]:
        i1 = data[a].index(result[a][0]) + 1
        i2 = data[a].index(result[a][1]) + 1
        i3 = data[a].index(result[a][2],i2) + 1
        #print i1,i2,i3        
    else:
        i1 = data[a].index(result[a][0]) + 1
        i2 = data[a].index(result[a][1]) + 1
        i3 = data[a].index(result[a][2]) + 1
    if i1 > i2:
        (i1,i2) = (i2,i1)
    if i1 > i3:
        (i1,i3) = (i3,i1)
    if i2 > i3:
        (i2,i3) = (i3,i2)
    print i1,i2,i3
