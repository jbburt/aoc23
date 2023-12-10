with open("day4/input.txt", "r") as f:
    lines = f.readlines()


def getset(string):
    return set(list(map(int, string.strip().split())))


cards = dict()

# problem 1
tot = 0
for il, line in enumerate(lines):
    card, substr = line.split(":")
    card_number = int(card.strip().split()[-1])
    cards[card_number] = dict.fromkeys(["nums", "win"])
    nums = substr.split("|")
    for i, toparse in enumerate(nums):
        if i == 1:  # my nums
            cards[card_number]["nums"] = getset(toparse)
            n = len(cards[card_number]["nums"].intersection(cards[card_number]["win"]))
            tot += int(2 ** (n - 1))
        elif i == 0:  # winning nums: parsed first
            cards[card_number]["win"] = getset(toparse)
print(tot)

# ensure cards' keys are sorted
cards = {k: cards[k] for k in sorted(list(cards.keys()))}

# problem 2
counts = {k: 1 for k in cards.keys()}
for cardnum, sets in cards.items():
    n = len(sets["nums"].intersection(sets["win"]))
    if n > 0:
        for i in range(1, 1 + n):
            k2 = cardnum + i
            counts[k2] += counts[cardnum]
print(sum(counts.values()))
