import copy
with open('9.txt') as f:
    lines = f.read().splitlines()


def genInvPyramid(diffs,collection): 
    toapp = copy.copy(diffs)
    collection.append(toapp)
    if all(diff == 0 for diff in diffs):
        collection[-1].append(0)
        return collection
    else:
        for i in range(len(diffs)-1):
            diffs[i]=(diffs[i+1]-diffs[i])
        diffs.pop()
        return genInvPyramid(diffs,collection)

fullsum = 0
for line in lines:
    output,listsum = genInvPyramid([int(el) for el in  line.split()],[]),0
    for i in range(len(output)-1,-1,-1):
        if i > 0:
            level = output[i]
            nextLevel: list = output[i-1]
            lastAtnextLevel = nextLevel[0]
            nextLevel.insert(0,lastAtnextLevel-level[0])
            listsum=lastAtnextLevel-level[0]

    fullsum+=listsum
print(fullsum)

