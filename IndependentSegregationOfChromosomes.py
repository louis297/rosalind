import math

def c(m,n):
    return math.factorial(n)/ math.factorial(n-m) / math.factorial(m)
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
f_read = f_in.read().rstrip()
n = int(f_read)
n *= 2
t1 = []
t2 = []
for i in range(1,n+1):
    t1.append(c(float(i),float(n)))
for i in range(len(t1)):
    temp = 0
    for j in range(i,len(t1)):
        temp += t1[j]
    t2.append(temp)

ap = float(pow(2,n))

for i in t2:
    print round(math.log(i/ap,10),3),
