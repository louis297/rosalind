import string
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read()
i = 0
a = c = g = t =0
while s[i] != '\n':
    if s[i] == 'A':
        a+=1
    if s[i] == 'G':
        g+=1
    if s[i] == 'T':
        t+=1
    if s[i] == 'C':
        c+=1
    i+=1
print a,c,g,t
