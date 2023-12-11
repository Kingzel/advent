import numpy as np
import math
with open('11.txt') as f:
    lines = f.read().splitlines()

tp =[]
for line in lines:
        temp =[]
        for ch in line:
            temp.append(ch)
        tp.append(temp)
tp =np.asarray(tp)

print('\n\n')

toext =[[],[]]
locs = []
for i in range(len(tp)):
     if not '#' in tp[i]:
        toext[0].append(i)

             
     
for i in range(len(tp[0])):    
    if not '#' in list(tp[:,i]):
        toext[1].append(i)

for i in range(len(tp)):
    for j in range(len(tp[i])):
             if tp[i][j]=='#':
                     emptyRowsBefore=len([x for x in toext[0] if x <= i])
                     emptyColsBefore=len([x for x in toext[1] if x <= j])
                     newi = 1000000*emptyRowsBefore+i-emptyRowsBefore
                     newj = 1000000*emptyColsBefore+j-emptyColsBefore
                     locs.append((newi,newj))

result = 0
for first in range(len(locs)):
     for second in range(first+1,len(locs)):
          result+=abs(locs[first][0]-locs[second][0])+abs(locs[first][1]-locs[second][1]) 
print(result)







