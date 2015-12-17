import string
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read()
s = s[:-1]
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
index = 0
for i in range(len(content)):
    gc_temp = content[i].count('G') + content[i].count('C')
    GC.append( float(gc_temp) / float (len(content[i]))*100 )
    if GC[i] > GC[index]:
        index = i
print name[index]
print GC[index]

