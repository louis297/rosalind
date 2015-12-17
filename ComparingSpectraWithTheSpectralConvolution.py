f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
set1 = []
set2 = []
for i in l[0].split():
    set1.append(float(i))
for i in l[1].split():
    set2.append(float(i))

set3 = []
for i in set1:
    for j in set2:
        set3.append(round(abs(i-j),6))

large = 0
x = 0
for i in set3:
    temp = set3.count(i)
    if temp > large:
        x = i
        large = temp

print large
print x
