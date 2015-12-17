f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read()
s = s[:-1]
l = s.split('\n')
name = []
content = []
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
for i in range(len(name)-1):
    for j in range(i+1,len(name)):
        if content[i][-3:] == content[j][:3]:
            print name[i],name[j]
        if content[i][:3] == content[j][-3:]:
            print name[j],name[i]
            
