import string
f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
name = []
content = []
A = [0] * 1000
G = [0] * 1000
C = [0] * 1000
T = [0] * 1000
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
name.append(name_temp)
content.append(content_temp)
result = ''
for i in range(len(content[0])):
    for j in range(len(content)):
        if content[j][i] == 'A':
            A[i] += 1
        if content[j][i] == 'G':
            G[i] += 1
        if content[j][i] == 'C':
            C[i] += 1
        if content[j][i] == 'T':
            T[i] += 1
    n = max(A[i],G[i],C[i],T[i])
    if A[i] == n:
        result += 'A'
        continue
    if G[i] == n:
        result += 'G'
        continue
    if C[i] == n:
        result += 'C'
        continue
    if T[i] == n:
        result += 'T'
output_A = ''
output_C = ''
output_G = ''
output_T = ''
for i in range(len(content[0])):
    output_A += str(A[i])
    output_A += ' '
output_A = output_A[:-1]
for i in range(len(content[0])):
    output_G += str(G[i])
    output_G += ' '
output_G = output_G[:-1]
for i in range(len(content[0])):
    output_C += str(C[i])
    output_C += ' '
output_C = output_C[:-1]
for i in range(len(content[0])):
    output_T += str(T[i])
    output_T += ' '
output_T = output_T[:-1]


print result
print "A:",output_A
print "C:",output_C
print "G:",output_G
print "T:",output_T
