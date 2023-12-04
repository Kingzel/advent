max_allowed = {'red': 12, 'green': 13, 'blue': 14}
games = [line.split(';')[1].split(',') for line in open("2.txt").readlines()]

acc = sum(i + 1 for i, game in enumerate(games) if all(int(count) <= max_allowed[key] for subset in game for count, key in (color.split() for color in subset)))

print(acc)
