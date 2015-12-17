f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
name = []
content = []
GC = []
flag = False
for s in l:
    if s[0] == '>':
        if flag:
            name.append(name_temp)
            content.append(content_temp)
        name_temp = s[1:]
        content_temp = ''
        flag = True
    else:
        content_temp += s
name.append(name_temp)
content.append(content_temp)

i0 = 0

for c in content[1]:
    i0 = content[0].find(c,i0) + 1
    print i0,
    i0 += 1
print
