with open("day1/input.txt", "r") as f:
    text = f.read()

# problem 1
print(
    sum(
        int(d[0] + d[-1])
        for d in "".join(
            filter(lambda c: c.isnumeric() or c == "\n", text)
        ).splitlines()
    )
)

# problem 2
convert = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find(s: str, reverse: bool = False) -> str:
    i = -1 if reverse else 0
    term = (-1 if reverse else 1) * len(s)
    op = "__lt__" if not reverse else "__gt__"
    while getattr(i, op, term):
        if s[i].isnumeric():
            return s[i]
        else:
            sub = s[i:]
            for k, v in convert.items():
                if sub.startswith(k):
                    return v
        i += -1 if reverse else 1


total = 0
for line in text.splitlines():
    val = int(find(line) + find(line, reverse=True))
    total += val
print(total)
