"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift 
will take you up to the water source, but this is as far as he can bring you. 
You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem:
they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise.
"Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; 
it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine,
but nobody can figure out which one. If you can add up all the part numbers in 
the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of 
the engine. There are lots of numbers and symbols you don't really understand, 
but apparently any number adjacent to a symbol, even diagonally, is a
"part number" and hould be included in your sum. (Periods (.) do not count
as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent 
to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent
to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. 
What is the sum of all of the part numbers in the engine schematic?

"""
combs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

with open("day3/input.txt", "r") as f:
    X = [list(x.rstrip(" ")) for x in f.read().rstrip("\n").split("\n")]

total = 0
height = len(X)
width = len(X[0])
nums = []
symbols = []
stars = {}
innum = False
# find spatially extended numbers
for i, row in enumerate(X):
    for j, x in enumerate(row):
        # check symbol
        if not (X[i][j] == "." or X[i][j].isnumeric()):
            symbols.append((i, j))
            if X[i][j] == "*":
                stars[(i, j)] = (0, [])
        if not innum:
            if x.isdigit():
                innum = True
                nums.append((i, j))
            else:
                pass
        else:
            if not x.isdigit():
                innum = False
                nums[-1] = (*nums[-1], j)
    if innum:
        innum = False
        nums[-1] = (*nums[-1], width)

parts = []
for i, left, right in nums:
    found = False
    for j in range(left, right):
        for i2, j2 in symbols:
            if abs(i - i2) <= 1 and abs(j - j2) <= 1:
                parts.append(int("".join(X[i][left:right])))
                found = True
                break
        if found:
            for i2, j2 in stars.keys():
                if abs(i - i2) <= 1 and abs(j - j2) <= 1:
                    n, nums = stars[(i2, j2)]
                    stars[(i2, j2)] = (n + 1, nums + [parts[-1]])
            break

print(sum(parts))


# A gear is any * symbol that is adjacent to exactly two part numbers.
# Its gear ratio is the result of multiplying those two numbers together.
# What is the sum of all of the gear ratios in your engine schematic?

total = 0
for n, nums in stars.values():
    if n == 2:
        total += nums[0] * nums[1]
print(total)
