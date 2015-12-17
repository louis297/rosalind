seq = (0,1,2,3,4,5,6,7,8,9)

data = []
plain = set()
single = []
result = [0]
trace = [[(0,0)]]

single.append(seq)
data.append(single)
plain.add(seq)
count = 1

while single:
    last = []
    lasttrace = []
    for ii in single:
        for i in range(9):
            for j in range(i,10):
                a = ii[i:j+1]
                temp = ii[:i] + a[::-1] + ii[j+1:]
                if temp not in plain:
                    plain.add(temp)
                    #result.append(count)
                    last.append(temp)
                    lasttrace.append((i,j))
    data.append(last)
    trace.append(lasttrace)
    single = last
    print count
    count+=1

while True:
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

    temp = []
    for j in datain[0]:
        temp.append(datain[1].index(j))
    print temp
    dataindex=tuple(temp)


    for i in range(len(data)):
        if dataindex in data[i]:
            print i
            for j in range(i,0,-1):
                (a,b) = trace[j][data[j].index(dataindex)]
                print a+1,b+1
                kk = dataindex[a:b+1]
                dataindex = dataindex[:a] + kk[::-1] + dataindex[b+1:] 
            break

    print '-----------------------------------------------------'


##for ii in range(len(data)):
##    for i in data[ii]:
##        print i
##        print ii
##    
