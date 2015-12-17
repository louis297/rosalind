f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = (f_in.read()).rstrip()
n = int(s)

print n-2
