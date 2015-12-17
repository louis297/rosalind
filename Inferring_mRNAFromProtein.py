f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
p = {
    'A':4,
    'C':2,
    'D':2,
    'E':2,
    'F':2,
    'G':4,
    'H':2,
    'I':3,
    'K':2,
    'L':6,
    'M':1,
    'N':2,
    'P':4,
    'Q':2,
    'R':6,
    'S':6,
    'T':4,
    'V':4,
    'W':1,
    'Y':2,
    }
k = 1
for c in s:
    k *= p[c]
    k %= 1000000
k *= 3
k %= 1000000
print k
