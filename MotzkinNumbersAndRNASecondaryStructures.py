f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
seq = ''.join(l[1:])

pair = {'A':'U','U':'A','G':'C','C':'G'}

length = len(seq)

temp = []
matrix = []
for i in range(length+2):
    temp = []
    for j in range(length+2):
        temp.append(0)
    matrix.append(temp)

for left in range(length-1):
    if seq[left] == pair[seq[left+1]]:
        matrix[left][left+1] = 2
    else:
        matrix[left][left+1] = 1
##for left in range(length):
##    matrix[left][left] = 1
for left in range(length-2):
    matrix[left][left+2] = matrix[left][left+1]
    if seq[left+2] == pair[seq[left]] or seq[left+2] == pair[seq[left+1]]:
        matrix[left][left+2] += 1

for left in range(length+1):
    for right in range(length+1):
        if right == left-1:
            matrix[left][right]=1
for i in matrix:
    print i
       
matrix[0][0] = 1
for i in range(3,length):
    for left in range(length-i):
##        if i%2==0:
##            matrix[left][left+i] = 0
##            continue
        temp = 0
##        pos = seq.find(pair[seq[left]],left)
##        while pos != -1:
##            temp = int(( temp + matrix[left+1][pos-1] * matrix[pos+1][left]+1) % 1000000)
            #print left,pos,i,temp
            #print left+1,pos-1,matrix[left+1][pos-1]
            #print pos+1,left+i,matrix[pos+1][left+i]
##            pos = seq.find(pair[seq[left]],pos+1)
        for k in range(2,i+2):
            print left,k,i,temp
            print left+1,left+k-2,matrix[left+1][left+k-2]
            print left+k,left+i,matrix[left+k][left+i]
            temp += matrix[left+1][left+k-2] * matrix[left+k][left+i]
            temp %= 1000000
        print temp
        matrix[left][left+i] = temp + matrix[left][left+i-1]
            
result = matrix[0][length-1]

print result
for i in matrix:
    print i
