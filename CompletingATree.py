f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = (f_in.read()).rstrip()
l = s.split('\n')

n = int(l[0])

r = n - len(l)

print r
