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

ts = 0
tv = 0
dic = {'A':'G','G':'A','C':'T','T':'C'}
for i in range(len(content[0])):
    if content[0][i] == dic[content[1][i]]:
        ts += 1
    elif content[0][i] != content[1][i]:
        tv += 1
print float(ts) / float(tv)
