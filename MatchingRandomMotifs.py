f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
ll = l[0].split()

N = int(ll[0])
x = float(ll[1])
seq = l[1]

AT = seq.count('A') + seq.count('T')
GC = seq.count('C') + seq.count('G')


rate = pow(x/2,GC) * pow( (1-x)/2,AT)

result = 1 - pow(1-rate,N)

print round(result,3)
