import string
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read()
i = s.find('\n')
sa = s[0:i]
sb = s[(i+1):-1]
result = []
i = 0
while (sb in sa[i:]):
    j=sa[i:].find(sb)+1
    result.append(i+j)
    i = i+j
output = ''
for i in result:
    output += str(i)
    output += ' '
output = output[:-1]
print output
