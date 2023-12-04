with open("2.txt") as f:
    lines = f.readlines()   
    f.close()

acc = 0
games = []
#12 red cubes, 13 green cubes, and 14 blue cubes
maxallowed = {'red':12,'green':13,'blue':14}
for i in range(len(lines)):
    game = lines[i].split(';',-1)
    game[0]=game[0].split(':')[1]
    games.append(game)

for i in range(len(games)):
    b = True
    for subset in games[i]:
        colors = subset.split(',',-1)
        for color in colors:
            count, key = color.split()
            if int(count)>maxallowed[key]:
                b = False
    ti = i+1
    # print( ti,":", b)

    if b:
        acc += ti

# print(subsets)
print(acc)
