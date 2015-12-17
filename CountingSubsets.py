f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = (f_in.read()).rstrip()

n = int(s)
r = 1

for i in range(n):
    r *= 2
    r = r % 1000000

print r
