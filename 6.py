import string
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read()
i = 0
sa = '';
sb = '';
while s[i] != ' ':
    sa+=s[i]
    i+=1
i+=1
while s[i] != '\n':
    sb+=s[i]
    i+=1
a = string.atoi(sa)
b = string.atoi(sb)
result = 0
# a<=i<=b, thus the max_range should be b+1
for i in range(a,(b+1),2):
    result += i
print result

