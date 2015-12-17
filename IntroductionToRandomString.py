f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
lt = s.split('\n')
seq = lt[0]
l = lt[1].split(' ')
A = map(lambda x: float(x), l)

import math

seq_len = len(seq)
seq = seq.replace('A','T')
seq = seq.replace('C','G')
T = seq.count('T')
G = seq_len - T

result = []
for i in A:
    GC_rate = i/2
    AT_rate = 0.5 - GC_rate
    r = pow(GC_rate,G) * pow(AT_rate,T)
    #print r
    result.append(round(math.log(r,10),3))
for i in result:
    print i,

