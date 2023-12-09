import copy
with open('9.txt') as f:
    lines = f.read().splitlines()


def genInvPyramid(diffs,collection): 
    toapp = copy.copy(diffs)
    collection.append(toapp)
    if all(diff == 0 for diff in diffs):
        return collection
    else:
        for i in range(len(diffs)-1):
            diffs[i]=(diffs[i+1]-diffs[i])
        diffs.pop()
        return genInvPyramid(diffs,collection)
fullsum = 0
for line in lines:
    output,listsum = genInvPyramid( [int(el) for el in  line.split()],[]),0
    for i in range(len(output)-1,-1,-1):
        if i > 0:
            level = output[i]
            nextLevel = output[i-1]
            lastAtnextLevel = nextLevel[-1]
            nextLevel.append(level[-1]+lastAtnextLevel)
            listsum=level[-1]+lastAtnextLevel
    fullsum+=listsum
print(fullsum)

