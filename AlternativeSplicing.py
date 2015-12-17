f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = (f_in.read()).rstrip()
l = s.split()

n = int(l[0])
m = int(l[1])

def ff(a):
    r = 1
    for i in range(2,a+1):
        r *= i
    return r

result = 0

for i in range(m,n+1):
    result += ff(n) / ff(i) / ff(n-i)
    result %= 1000000

print result
