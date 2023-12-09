import math
class Node:
    def __init__(self,code,left,right) -> None:
        self.left = left
        self.right = right
        self.code = code


with open('8.txt') as f:
    lines = f.read().splitlines()

turns = lines[0]
lines =lines[2:]
nodes={}
starts = []
for line in lines:
    code,left,right = line.split(' = ')[0],line.split(' = ')[1].split(',')[0].removeprefix('('),line.split(' = ')[1].split(',')[1].removesuffix(')').lstrip()
    nodes[code]=Node(code,left,right)
    if code[len(code)-1] == 'A':
        starts.append(code)

stepseach =[]
for code in starts:
    reached = False
    i =0
    current:  Node = nodes[code]
    while True:
        if not current.code[len(current.code)-1] == "Z":
            currentTurn = turns[i%len(turns)]
            if currentTurn == 'L':
                current = nodes[current.left]
            else:
                current = nodes[current.right]
            i+=1
            
        else:
            break
    stepseach.append(i)
print(math.lcm(*stepseach))