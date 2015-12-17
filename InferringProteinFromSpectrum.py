protein = {"A":71.03711,"C":103.00919,"D":115.02694,"E":129.04259,
           "F":147.06841,"G":57.02146,"H":137.05891,"I":113.08406,
           "K":128.09496,"L":113.08406,"M":131.04049,"N":114.04293,
           "P":97.05276,"Q":128.05858,"R":156.10111,"S":87.03203,
           "T":101.04768,"V":99.06841,"W":186.07931,"Y":163.06333}

f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
A = []
for i in l:
    A.append(float(i))

A.sort(reverse=True)
pkeys = protein.keys() 
result = ''

mass = A[0]
L = A[1:]
L.sort()
S = []
s1 = []
for i in range((len(L)-1)/2):
    S.append((L[i],L[len(L)-1-i]))
now = L[0]
del L[0]
del L[-1]
s1.append(now)
result = ''
i = 0
while L:
    
    flag = True
    for j in pkeys:
        if abs( protein[j] - L[i] + now) < 0.01:
            s1.append(L[i])
            flag = False
            now = L[i]
            t1 =  L[i]
            t2 =  L[len(L)-i-1]
            L.remove(t1)
            L.remove(t2)
            i = 0
            break
    i += 1

##S = []
##s1 = [L[0]]
##s2 = [L[-1]]
##for i in range((len(L)-1)/2):
##    S.append((L[i],L[len(L)-1-i]))
##    
##for i in range(1,(len(L)-1)/2):
##    (a,b) = S[i]
##    flag = True
##    for j in pkeys:
##        if abs( protein[j] - S[i][0] - S[i-1][0]) < 0.01:
##            s1.append(S[i][0])
##            s2.append(S[i][1])
##            flag = False
##            break
##    if flag:    
##        s1.append(S[i][1])
##        s2.append(S[i][0])
    


for i in range(len(s1)-1):
    temp = s1[i] - s1[i+1]
    for j in pkeys:
        if abs(protein[j] - abs(temp)) < 0.01:
            result += j
            break

print result
