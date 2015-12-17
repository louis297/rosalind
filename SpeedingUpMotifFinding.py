##seq = 'CAGCATGGTATCACAGCAGAG'
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
l = l[1:]
seq = ''.join(l)
temp = []
result = []
length = len(seq)
for i in range(len(seq)):
    result.append(0)

for i in range(1,len(seq)-1):
    if seq[i] == seq[0]:
        result[i] = 1
        temp.append(i)
if seq[-1] == seq[0]:
    result[-1] = 1

for i in range(2,len(seq)):
    if not temp:
        break
    temp1 = temp
    temp = []
    for j in temp1:
        if seq[i-1] == seq[j+1]:
            if j != length-2:
                temp.append(j+1)
            result[j+1]=i

for i in result:
    print i,
