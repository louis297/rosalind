f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split()
n = int(l[0])
k = int(l[1])
result = 1
for i in range(n,n-k,-1):
    result *= i
    result %= 1000000
print result
