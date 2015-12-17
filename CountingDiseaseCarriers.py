f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split()
A = []
for i in l:
    A.append(float(i))
B = []

import math

for i in A:
    q = math.sqrt(i)
    p = 1-q
    temp = i + 2*p*q
    B.append(round(temp,3))

for i in B:
    print i,
