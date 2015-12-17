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

result = ''
last = ''

seq = []

#find head
for i in range(len(content)):
    flag = True
    for j in range(len(content)):
        if i != j and content[i][:len(content[i])/2] in content[j]:
            flag = False
            break
    if flag:
        result += content[i]
        last = content[i]
        del content[i]
        break

#find others

temp = []
pos = 9999
ind = 9999
while(content):
    flag = False
    for j in range(len(content)):
        if last[(len(last)-1)/2 :] in content[j]:
            #print "*************************************"
            temp.append(j)
            if pos > content[j].rindex(last[(len(last)-1)/2 :]) + len(last)-(len(last)-1)/2:
                pos = content[j].rindex(last[(len(last)-1)/2 :]) + len(last)-(len(last)-1)/2
                ind = j
                
                #print content[j],ind,pos,content[j][pos:]
                #print j,'\t',len(content),'\t',len(content[j])-pos,'\t',pos
                flag = True
    if flag:
        last = content[ind]
        result += last[pos:]
        #print "*************************************"
        #print result
    temp.reverse()
    #print temp
    for i in temp:
        del content[i]
    temp = []
    pos = 9999
    ind = 9999
    flag = False

print result
            
    
    
###find order
##for i in range(len(content)-1):
##    for j in range(len(content)):
##        if j not in seq and content[seq[-1]][len(content[i])/2:] in content[j]:
##            temp = content[j].index(content[seq[-1]][len(content[i])/2:])
##            temp += (len(content[i])+1)/2
##            seq.append(j)
##            pos.append(temp)
##            break
##
### link all sequence
##result = content[seq[0]]
##for i in range(1,len(content)):
##    result += content[seq[i]][pos[i]:]
