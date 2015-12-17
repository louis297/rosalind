f_name = raw_input("Please Input File Name:")
f_in = open(f_name,"r")
temp = f_in.read()
temp = temp[:-1]
l = temp.split('\n')
temp = ''
for i in range(1,len(l)):
    temp += l[i]
s = [temp]

temp = s[0]
temp = temp.replace('A','t')
temp = temp.replace('T','a')
temp = temp.replace('C','g')
temp = temp.replace('G','c')
temp = temp[::-1]
s.append(temp.upper())

result = []
temp = ''
flag = False
index = 0
i = 0
d = {"TTT":"F","TTC":"F","TTA":"L","TTG":"L","CTT":"L","CTC":"L","CTA":"L","CTG":"L","ATT":"I","ATC":"I","ATA":"I","ATG":"M","GTT":"V","GTC":"V","GTA":"V","GTG":"V","TCT":"S","TCC":"S","TCA":"S","TCG":"S","CCT":"P","CCC":"P","CCA":"P","CCG":"P","ACT":"T","ACC":"T","ACA":"T","ACG":"T","GCT":"A","GCC":"A","GCA":"A","GCG":"A","TAT":"Y","TAC":"Y","TAA":'',"TAG":'',"CAT":"H","CAC":"H","CAA":"Q","CAG":"Q","AAT":"N","AAC":"N","AAA":"K","AAG":"K","GAT":"D","GAC":"D","GAA":"E","GAG":"E","TGT":"C","TGC":"C","TGA":'',"TGG":"W","CGT":"R","CGC":"R","CGA":"R","CGG":"R","AGT":"S","AGC":"S","AGA":"R","AGG":"R","GGT":"G","GGC":"G","GGA":"G","GGG":"G"}
for ii in range(len(s)):
    while i<(len(s[ii])-3):
        if s[ii][i:i+3] == 'ATG':
            j = i
            temp = ''
            while j<(len(s[ii])-3):
                if d[s[ii][j:j+3]] !='':
                    temp += d[s[ii][j:j+3]]
                else:
                    if temp not in result:
                        result.append(temp)
                    break
                j += 3
        i += 1
            
##            flag = True
##            index = i
##        if flag and (d[s[ii][i:i+3]] !=''):
##            temp+=d[s[ii][i:i+3]]
##        else:
##            if flag:
##                if (temp not in result):
##                    result.append(temp)
##                s[ii] = s[ii][index+3:]
##                i = 0
##                index = 0
##                temp = ''
##                flag = False
##        i += 1
#    if temp != '':
#        result.append(temp)
    i = 0
    index = 0
    temp = ''
    flag = False
for i in range(len(result)):
    print result[i]

