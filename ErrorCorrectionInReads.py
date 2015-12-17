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

seqlen = len(content[0])

correct = set()
wrong = []
rc = []

length = len(content)
i = 0

def rev_comp(seq):
    rev = seq[::-1]
    rc = ''
    dic = {'A':'T','T':'A','G':'C','C':'G'}
    for nuc in rev:
        rc += dic[nuc]
    return rc
    
for i in content:
    rc.append(rev_comp(i))
    rc.append(i)
    
for i in content:
    if rc.count(i) == 1:
        wrong.append(i)
    else:
        correct.add(i)

rcset = set()
for i in correct:
    rcset.add(i)
    rcset.add(rev_comp(i))

for sw in wrong:
    for sr in rcset:
        count = 0
        flag = True
        for i in range(seqlen):
            if count>1:
                flag = False
                break
            if sw[i] != sr[i]:
                count += 1
        if flag:
            print sw + '->' + sr
            break
                
        

##while (i<length):
##    if content[i] in content[i+1:]:
##        correct.append(content[i])
##        temp = content[i][:]
##        del content[i]
##        delindex = []
##        #######################################
##        for j in content[i:]:
##            if j == temp:
##                delindex.append(
##            
##
##    else:
##        wrong.append(content[i])
##        i += 1
