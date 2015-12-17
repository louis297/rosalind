f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read()
s = s[:-1]
l = s.split()
m = int(l[1])
n = int(l[0])

adult = [0,1]
baby = [1,0]
for i in range(2,m):
    adult.append(adult[i-1] + baby[i-1])
    baby.append(adult[i-1])
for i in range(m,n):
    adult.append(adult[i-1] + baby[i-1] - baby[i-m])
    baby.append(adult[i-1])
print adult[n-1]+baby[n-1]
