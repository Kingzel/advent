import numpy as np
with open('11.txt') as f:
    lines = f.read().splitlines()

tp =[]
for line in lines:
        temp =[]
        for ch in line:
            temp.append(ch)
        tp.append(temp)
tp =np.asarray(tp)

# print(tp.shape)
print('\n\n')

toext =[[],[]]
locs = []
for i in range(len(tp)):
     if not '#' in tp[i]:
        toext[0].append(i)

             
     
for i in range(len(tp[0])):    
    if not '#' in list(tp[:,i]):
        toext[1].append(i)
c=0
for row in toext[0]:        
    tp = np.insert(tp,row+c,tp[row+c],axis = 0)
    c+=1
c=0
for col in toext[1]: 
    tp = np.insert(tp,col+c,list(tp[:,col+c]),axis = 1)
    c+=1

for i in range(len(tp)):
    for j in range(len(tp[i])):
             if tp[i][j]=='#':
                 locs.append((i,j))

result = 0
# print(np.abs(locs[4][0]-locs[8][0])  + np.abs(locs[4][1]-locs[8][1]),locs[4],locs[8] )
for first in range(len(locs)):
     for second in range(first+1,len(locs)):
          result+=np.abs(locs[first][0]-locs[second][0])+np.abs(locs[first][1]-locs[second][1]) 
# print(tp,locs,tp.shape,sep="\n")
print(result)
        

     


# print(tp)






