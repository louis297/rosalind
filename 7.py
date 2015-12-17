import string
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read()
result = ''
i = 0
for i in range(len(s)):
    if s[i] == 'T':
        result+='A'
    if s[i] == 'A':
        result+='T'
    if s[i] == 'C':
        result+='G'
    if s[i] == 'G':
        result+='C'
result = result[::-1]
print result
