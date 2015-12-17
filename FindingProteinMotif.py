import re
import urllib

f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
f_read = f_in.read().rstrip()

all_name = f_read.split()


for s in all_name:
    seq = []
    url="http://www.uniprot.org/uniprot/"+s+".fasta"
    handle = urllib.urlopen(url)
    for line in handle:
        seq.append(line.rstrip())
    seq = seq[1:]
    seq = ''.join(seq)
    #print seq
    R = re.compile(ur"N[^P][ST][^P]")
    flag = False
    n = 0
    result = []
    while (n < len(seq)-3):
        Match = R.match(seq[n:])
        if Match != None :
            flag = True
            result.append(n+1)
        n += 1    
    #result = R.finditer(seq)
    if(flag):
        print s
        for i in result:
            print i,
        print

