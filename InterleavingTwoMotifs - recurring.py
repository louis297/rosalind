##f_name = raw_input("Please Input File Name:")
##f_in = open(f_name,"r")
##s = f_in.read().rstrip()
##l = s.split('\n')
##s1 = l[0]
##s2 = l[1]
s1 = 'CCAATGCGCGTTGCCATCTCGTTCGTTGCCAGCCAATGCCGTTGCCAGTCTCGTTGCCAATGCGTCTCGTTG'
s2 = 'GTCCTCAGTACATTCGTGTCATACGGTGGTGTCATACGGTGGTGTCATACGGTGGTGTCATACGGTGGTGTCATACGGTG'

def interleave(s1, s2):
    if s1 == '':
        return s2
    if s2 == '':
        return s1
    head = ''
    p = 0
    while (s1[p] == s2[p]):
        head += s1[p]
        p += 1
        if p == len(s1) and p == len(s2):
            return head
        elif p == len(s1):
            return head+s2[p:]
        elif p == len(s2):
            return head+s1[p:]
    s1 = s1[p:]
    s2 = s2[p:]
    p1 = s1.find(s2[0])
    p2 = s2.find(s1[0])
    if p1 == -1:
        return head+s1+s2
    if p2 == -1:
        return head+s2+s1
        
    h1 = head + s1[:p1] + interleave(s1[p1:],s2)
    h2 = head + s2[:p2] + interleave(s1,s2[p2:])
    if len(h1) > len(h2):
        return h2
    else:
        return h1
    

print interleave(s1,s2)
