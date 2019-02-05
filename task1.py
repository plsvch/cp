#поиск сложноподчиненных предложений
inwords=open('words.txt')
inconst=open('const.txt')
intext=open('text.txt')
outfile=open('outfile.txt', 'w')

import re
output=[]
words=[]
const=[]
for line in inwords.readlines(): words.append(line.strip())
for line in inconst.readlines(): const.append(line.strip())
text=intext.read()
ortext=re.sub('\n','',text).split('. ')
worktext=list(map(lambda x: x.lower(), ortext))
#проверка 1
for i in range(0, len(worktext)):
    for j in range(0, len(words)):
        temp=re.findall(words[j]+' ', worktext[i])
        if temp!=[] and ',' in worktext[i]:
            #print(temp)
            strtemp=''.join(temp)
            #print(strtemp)
            t=ortext[i].index(strtemp)
            ortext[i] = re.sub(ortext[i][t:t + len(strtemp)], ortext[i][t:t + len(strtemp)].upper(), ortext[i])
            #print(ortext[i])
            if ortext[i] not in output: output.append(ortext[i])
#проверка 2
for i in range(0, len(worktext)):
    for j in range (0, len(const), 2):
        temp1=re.findall(const[j]+' ', worktext[i])
        temp2=re.findall(const[j+1]+' ', worktext[i])
        if temp1!=[] and temp2!=[] and ',' in worktext[i]:
            strtemp1=''.join(temp1)
            strtemp2 = ''.join(temp2)
            t1=ortext[i].index(strtemp1)
            t2 = ortext[i].index(strtemp2)
            ortext[i] = re.sub(ortext[i][t1:t1 + len(strtemp1)], ortext[i][t1:t1 + len(strtemp1)].upper(), ortext[i])
            ortext[i] = re.sub(ortext[i][t2:t2 + len(strtemp2)], ortext[i][t2:t2 + len(strtemp2)].upper(), ortext[i])
            if ortext[i] not in output: output.append(ortext[i])
outfile.write(str(output))
print(output)
inwords.close()
inconst.close()
intext.close()
outfile.close()
