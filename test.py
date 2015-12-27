f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
s = f_in.read().rstrip()
l = s.split('\n')
s = ''.join(l[1:])
#s = 'ACCUACGUGCAGCAUAUCGGCGCUCGAUAUAGGGGUGCUACAUGAACGUUACAUCUACUAUAGUACGCUUACGGCAAUAUAUGCGCAUCGCGGUGCGUUAACAGCCGGUACGCGCCGGUACGCUAUAGUUAGCUAUAACGAUAUAAUAUUUUAACAUGCGCCCGUCGCGUAUAACGUACUAGUACCGGUAUAUCGACGGGGCCCCGGUACGCGCCUAGUAGACGCGGCUUACCAUGCAUGAUUAUAAUCGCGUACGAUGGCUUUCGAAAUUAGUAUACCG'
##s = 'AUAUAU'
#s = 'UAGCGUGAUCAC'

##c = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':2, 'CA':0, 'CC':0, 
##    'CG':2, 'CU':0, 'GA':0, 'GC':2, 'GG':0, 'GU':0, 'UA':2, 'UC':0, 'UG':0, 'UU':0}
c = {'':1, 'A':1, 'C':1, 'G':1, 'U':1, 'AA':1, 'AC':1, 'AG':1, 'AU':2, 'CA':1, 'CC':1, 
    'CG':2, 'CU':1, 'GA':1, 'GC':2, 'GG':1, 'GU':1, 'UA':2, 'UC':1, 'UG':1, 'UU':1}

def motzkin(s):
    if s not in c:
        temp = motzkin(s[1:])
        for k in range(1, len(s)):
            temp += int (motzkin(s[1:k]) * (c[s[0]+s[k]]-1) * motzkin(s[k+1:]) % 1000000)
            #print ' ', k, temp+1, s[0],'|', s[1:k],'|', s[k],'|', s[k+1:], '|',s
##        if len(s) % 2:
##            temp += motzkin(s[1:]) - 1
        c[s] = temp
        
    return c[s]

print motzkin(s) % 10**6
