from math import prod
from sys import stdin


def pad(str, c):
    return str + (c - len(str)) * " "


def solve(input):
    # make sure all lines are same length for part2
    c = max([len(row) for row in input])
    input = [pad(row, c) for row in input]

    part1, part2 = 0, 0

    # part 1
    ops = input[-1].split()
    rows = [list(map(int, row.split())) for row in input[:-1]]

    for i, op in enumerate(ops):
        col = [row[i] for row in rows]
        part1 += sum(col) if op == "+" else prod(col)

    # part 2
    tmp = 0
    mode = ""

    for i, c in enumerate(input[-1]):
        if c != " ":
            mode = c
            part2 += tmp
            tmp = 1 if c == "*" else 0

        val = 0

        for row in input[:-1]:
            if row[i] == " ":
                if val == 0:
                    continue
                break
            val = 10 * val + int(row[i])

        if val != 0:
            tmp = (tmp * val) if mode == "*" else (tmp + val)

    part2 += tmp
    return part1, part2


print(solve([line.rstrip() for line in stdin]))
