f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
seq = ''.join(l[1:])

nu = {'A':'U','U':'A','C':'G','G':'C'}
count = 0


def f(a,b):
    r = 1
    if a<b:
        (a,b) = (b,a)
    for i in range(b):
        r*= (a-i)
    
    return r

##for i in range(len(seq)-2):
##    for j in seq[i+2:]:
##        if nu[seq[i]] == j:
##            count += 1
##            print i,seq[i],j

c = seq.count('C')
g = seq.count('G')
a = seq.count('A')
u = seq.count('U')

count = f(g,c) * f(u,a)

print count
