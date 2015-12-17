f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.readline()
s = f_in.read().rstrip()
l = s.split('\n')
s = ''
for i in range(len(l)):
    s += l[i]
n=4
single = []
temp = []
result = [[['A'],['C'],['G'],['T']]]
st = []
stt = ''
for i in range(1,n):
    for j in range(len(result[i-1])):
        for k in range(len(result[0])):
            single = (result[i-1][j])[:]
            single.append(result[0][k][0])
            temp.append(single)
            single = []
    result.append(temp)
    temp = []
temp = result[n-1]
for i in range(len(temp)):
    for j in range(n):
        stt += temp[i][j]
    st.append(stt)
    stt = ''
output = ''
outtemp = 0
for i in range(len(st)):
    for j in range(len(s)-3):
        if s[j:j+4] == st[i]:
            outtemp += 1
            
    output += str(outtemp)+' '
    outtemp = 0
print output
