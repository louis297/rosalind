f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
DNA = ''
s = f_in.read()
s = s[:-1]
l = s.split('\n')
intron = []
name = []
flag = False
for s in l:
    if s[0] == '>':
        if flag:
            intron.append(intron_temp)
        name_temp = s[1:]
        intron_temp = ''
        flag = True
    else:
        intron_temp += s
intron.append(intron_temp)
DNA = intron[0]
del intron[0]
for i in range(len(intron)):
   #while (DNA.find(intron[i])) != -1:
        DNA = DNA[:DNA.find(intron[i])] + DNA[DNA.find(intron[i])+len(intron[i]):]
d = {"TTT":"F","TTC":"F","TTA":"L","TTG":"L","CTT":"L","CTC":"L","CTA":"L","CTG":"L","ATT":"I","ATC":"I","ATA":"I","ATG":"M","GTT":"V","GTC":"V","GTA":"V","GTG":"V","TCT":"S","TCC":"S","TCA":"S","TCG":"S","CCT":"P","CCC":"P","CCA":"P","CCG":"P","ACT":"T","ACC":"T","ACA":"T","ACG":"T","GCT":"A","GCC":"A","GCA":"A","GCG":"A","TAT":"Y","TAC":"Y","TAA":'',"TAG":'',"CAT":"H","CAC":"H","CAA":"Q","CAG":"Q","AAT":"N","AAC":"N","AAA":"K","AAG":"K","GAT":"D","GAC":"D","GAA":"E","GAG":"E","TGT":"C","TGC":"C","TGA":'',"TGG":"W","CGT":"R","CGC":"R","CGA":"R","CGG":"R","AGT":"S","AGC":"S","AGA":"R","AGG":"R","GGT":"G","GGC":"G","GGA":"G","GGG":"G"}
protein = ''
for i in range(0,len(DNA),3):
    protein += d[DNA[i:i+3]]
print protein
