import string
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read()
i = s.find('\n')
sa = s[0:i]
sb = s[(i+1):-1]
result = 0
for i in range(len(sa)):
    if sa[i] != sb[i]:
        result+=1
print result
