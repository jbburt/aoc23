from functools import reduce

with open("day2/input.txt", "r") as f:
    lines = f.readlines()

colors = ["red", "green", "blue"]
games = dict()
for line in lines:
    game, outcomes = line.split(":")
    gameid = int(game.split(" ")[-1])
    sets = []
    for cubeset in outcomes.strip().split(";"):
        thisset = {c: 0 for c in colors}
        for countcolor in cubeset.split(","):
            count, color = countcolor.strip().split(" ")
            thisset[color] = int(count)
        sets.append(thisset)
    games[gameid] = sets

tot = 0
for gameid, gamesets in games.items():
    possible = True
    for gameset in gamesets:
        if gameset["red"] > 12 or gameset["green"] > 13 or gameset["blue"] > 14:
            possible = False
            break
    if possible:
        tot += gameid
print(tot)


tot = 0
for gamesets in games.values():
    mins = {c: 0 for c in colors}
    for gameset in gamesets:
        for color, n in gameset.items():
            mins[color] = max(mins[color], n)
    power = reduce(lambda x, y: x * y, mins.values(), 1)
    tot += power
print(tot)
