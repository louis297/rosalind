import string
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read()
i = 0
result = ''
while s[i] !='\n':
    if s[i] == 'T':
        result += 'U'
    else:
        result += s[i]
    i+=1;
print result
