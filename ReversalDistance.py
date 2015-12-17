seq = (0,1,2,3,4,5,6,7,8,9)

data = []
plain = set()
single = []
result = [0]

single.append(seq)
data.append(single)
plain.add(seq)
count = 1

while single:
    last = []
    for ii in single:
        for i in range(9):
            for j in range(i,10):
                a = ii[i:j+1]
                temp = ii[:i] + a[::-1] + ii[j+1:]
                if temp not in plain:
                    plain.add(temp)
                    #result.append(count)
                    last.append(temp)
    data.append(last)
    single = last
    print count
    count+=1

f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
datain = []
temp = []
for line in l:
    if line != '':
        for i in line.split():
            temp.append(int(i))
        datain.append(temp)
        temp = []

dataindex = []
n = len(datain)
for i in range(n/2):
    temp = []
    for j in datain[i*2+1]:
        temp.append(datain[i*2].index(j))
    print temp
    dataindex.append(tuple(temp))

for single in dataindex:
    for i in range(len(data)):
        if single in data[i]:
            print i,
            break

print


##for ii in range(len(data)):
##    for i in data[ii]:
##        print i
##        print ii
##    
