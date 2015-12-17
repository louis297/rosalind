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

result = []
single = []
def distance(s1,s2):
    length = len(s1)
    dif = 0
    for i in range(length):
        if s1[i] != s2[i]:
            dif += 1
    return round(float(dif)/float(length),5)

for i in range(len(content)):
    for j in range(len(content)):
        single.append(distance(content[i],content[j]))
    result.append(single)
    single = []

for line in result:
    for num in line:
        print num,
    print
