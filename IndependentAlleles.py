import math

def c(m,n):
    return math.factorial(n)/ math.factorial(n-m) / math.factorial(m)
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
f_read = f_in.read().rstrip()
l = f_read.split()
k = int(l[0])
N = int(l[1])
k2 = int(math.pow(2.0,float(k))+0.001)
rate = []
result = 0
for i in range(k2+1):
    temp = pow(0.75,i)*pow(0.25,k2-i)*c(i,k2)
    rate.append(temp)
for i in range(k2-N+1):
    result += rate[i]
print result
