with open("2.txt") as f:
    lines = f.readlines()   

acc = 0
games = []
for i in range(len(lines)):
    game = lines[i].split(';',-1)
    game[0]=game[0].split(':')[1]
    games.append(game)

for i in range(len(games)):
    maxallowed = {'red':0,'green':0,'blue':0}
    for subset in games[i]:
        colors = subset.split(',',-1)
        for color in colors:
            count, key = color.split()
            maxallowed[key] = max(maxallowed[key],int(count))
    
    t = 1
    for elem in list(maxallowed.values()):
        t*=elem
    print(maxallowed.values())
    print(games[i],t)
    acc +=t


print(acc)