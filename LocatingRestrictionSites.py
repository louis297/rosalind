f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.readline()
s = f_in.read()
s = s[:-1]
l = s.split('\n')
s = ''
start = []
length = []
for t in l:
    s += t
for i in range(len(s)-3):
    j = 12
    while j >= 4:
        if i+j > len(s):
            j -= 1
            continue
        t1 = s[i:i+j]
        temp = t1[::-1]
        temp = temp.replace('A','t')
        temp = temp.replace('G','c')
        temp = temp.replace('T','a')
        temp = temp.replace('C','g')
        temp = temp.upper()
        if t1 == temp:
            start.append(i+1)
            length.append(j)
            #break
        temp = ''
        j -= 1
for i in range(len(start)):
    print start[i],length[i]
