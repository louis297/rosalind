f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
ll = l[1].split()
seq = []
for i in ll:
    seq.append(int(i))
lis_inc = []
lis_inc.append([seq[0]])
length_inc = []
length_inc.append(1)
lis_dec = [[seq[0]]]
length_dec = [1]
for i in range(1,len(seq)):
    m = 0
    temp = []
    for j in range(i):
        if seq[i] > seq[j]:
            if m < length_inc[j]:
                m = length_inc[j]
                temp = lis_inc[j]
    lis_inc.append(temp+[seq[i]])
    length_inc.append(len(lis_inc[i]))
for i in range(1,len(seq)):
    m = 0
    temp = []
    for j in range(i):
        if seq[i] < seq[j]:
            if m < length_dec[j]:
                m = length_dec[j]
                temp = lis_dec[j]
    lis_dec.append(temp+[seq[i]])
    length_dec.append(len(lis_dec[i]))
m = 0
pos_max = 0
for i in range(len(length_inc)):
    if m < length_inc[i]:
        m = length_inc[i]
        pos_max = i
for i in lis_inc[pos_max]:
    print i,
print
m = 0
pos_max = 0
for i in range(len(length_dec)):
    if m < length_dec[i]:
        m = length_dec[i]
        pos_max = i
for i in lis_dec[pos_max]:
    print i,
print
