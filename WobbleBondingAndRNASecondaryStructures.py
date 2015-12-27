f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()


##s = 'AUGCUAGUACGGAGCGAGUCUAGCGAGCGAUGUCGUGAGUACUAUAUAUGCGCAUAAGCCACGU'
c = {'':0, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 
    'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':1, 'UA':1, 'UC':0, 'UG':1, 'UU':0}
def wobble(s):
    if len(s) < 4:
        return 1
    elif s not in c:
        temp = wobble(s[1:])
        for k in range(4, len(s)):
            temp += wobble(s[1:k]) * c[s[0]+s[k]] * wobble(s[k+1:])
        c[s] = temp
        
    return c[s]

print wobble(s)
