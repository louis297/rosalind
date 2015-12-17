f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
seq = ''.join(l[1:])

nu = {'A':'U','U':'A','C':'G','G':'C'}
count = 0


def f(a):
    r = 1
    for i in range(2,a+1):
        r *= i
    return r

##for i in range(len(seq)-2):
##    for j in seq[i+2:]:
##        if nu[seq[i]] == j:
##            count += 1
##            print i,seq[i],j

gc = seq.count('C')
ua = seq.count('U')

count = f(gc) * f(ua)

print count
