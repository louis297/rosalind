f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = (f_in.read()).rstrip()
l = s.split('\n')

length = len(l)
seql = len(l[0])
d = length - len(l[0])

result = l[0]
del l[0]
for i in range(d):
    pos = 0
    for j in range(len(l)):
        if l[j][:-1] == result[i+1:]:
            pos = j
            break
    result += l[pos][-1]
    del l[pos]

print result
