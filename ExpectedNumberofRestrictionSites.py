f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
lt = s.split('\n')
n = int(lt[0])
seq = lt[1]
l = lt[2].split()
A = []
for i in l:
    A.append(float(i))

length = len(seq)
seq = seq.replace('A','T')
seq = seq.replace('C','G')
T = seq.count('T')
G = seq.count('G')
result = []

for i in A:
    GC_rate = i/2
    AT_rate = 0.5 - GC_rate
    r = pow(GC_rate,G) * pow(AT_rate,T) * (n-length+1)

    result.append(round(r,3))

for i in result:
    print i,
