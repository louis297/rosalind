f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read()
s = s[:-1]
l = s.split(' ')
a = []
for i in range(6):
    a.append(float(l[i]))
result = 2*(a[0]+a[1]+a[2]) + 1.5*a[3] + a[4]
print result
