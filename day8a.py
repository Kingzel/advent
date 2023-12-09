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
for line in lines:
    code,left,right = line.split(' = ')[0],line.split(' = ')[1].split(',')[0].removeprefix('('),line.split(' = ')[1].split(',')[1].removesuffix(')').lstrip()
    nodes[code]=Node(code,left,right)

reached = False
i =0
current:  Node = nodes['AAA']
while True:
    if not current.code == "ZZZ":
        currentTurn = turns[i%len(turns)]
        if currentTurn == 'L':
            current = nodes[current.left]
        else:
            current = nodes[current.right]
        i+=1
        
    else:
        break
print(i)