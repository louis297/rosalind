import string
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.readline()
# s = ''
result = ''
i = 0
while s:
    result += f_in.readline()
    s = f_in.readline()
print result
