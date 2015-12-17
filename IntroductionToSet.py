f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = (f_in.read()).rstrip()
l = s.split('\n')

n = int(l[0])
s1 = l[1][1:-1]
s2 = l[2][1:-1]

tl1 = s1.split(', ')
tl2 = s2.split(', ')

l1 = []
l2 = []
for i in tl1:
    l1.append(int(i))
for i in tl2:
    l2.append(int(i))

r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []

for i in range(1,n+1):
    if i in l1 or i in l2:
        r1.append(i)
    if i in l1 and i in l2:
        r2.append(i)
    if i in l1 and not (i in l2):
        r3.append(i)
    if not (i in l1) and i in l2:
        r4.append(i)
    if not (i in l1):
        r5.append(i)
    if not (i in l2):
        r6.append(i)

print r1
print r2
print r3
print r4
print r5
print r6


