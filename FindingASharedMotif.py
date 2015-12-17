# This program might take up to 1 minute to calculate

def find(first,other,num):
    l = len(first)
    for i in range(l,0,-1):
        for j in range(l):
            if (i+j) >= l:
                break
            temp = first[j:j+i]
            if other.count(temp) == num:
                return temp
    


f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = (f_in.read()).rstrip()
l = s.split('\n')
name = []
content = []
flag = False
for s in l:
    if s[0] == '>':
        if flag:
            name.append(name_temp)
            content.append(content_temp)
        name_temp = s
        content_temp = ''
        flag = True
    else:
        content_temp += s
#name.append(name_temp)
content.append(content_temp)
first = content[0]
other = ''
for i in range(1,len(content)):
    other += content[i]
result = find(first,other,len(content)-1)
print result
