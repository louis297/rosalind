import string
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
temp = f_in.read()
i = 0
s = ''
sa = sb = sc = sd = ''
while temp[i] != '\n':
    s+=temp[i]
    i+=1
while temp[i] != ' ':
    sa+=temp[i]
    i+=1
i+=1
while temp[i] != ' ':
    sb+=temp[i]
    i+=1
i+=1
while temp[i] != ' ':
    sc+=temp[i]
    i+=1
i+=1
while temp[i] != '\n':
    sd+=temp[i]
    i+=1
a = string.atoi(sa)
b = string.atoi(sb)
c = string.atoi(sc)
d = string.atoi(sd)
result = s[a:(b+1)]+' '+s[c:(d+1)]
print result
