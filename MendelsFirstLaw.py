import string
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read()
s = s[:-1]
l = s.split(' ')
a = float(l[0])
b = float(l[1])
c = float(l[2])
total = a*b + b*c + c*a + a*(a-1)*0.5 + b*(b-1)*0.5 + c*(c-1)*0.5
domi = a*(b+c) + a*(a-1)*0.5 + 0.75*b*(b-1)*0.5 + 0.5*b*c
result = domi / total
print result
