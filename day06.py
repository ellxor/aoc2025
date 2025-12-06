from itertools import groupby
from math import prod
from sys import stdin


def solve(input):
    # part 1
    ops = input[-1].split()
    rows = [list(map(int, row.split())) for row in input[:-1]]
    cols = [[row[i] for row in rows] for i in range(len(ops))]

    # part2
    transposed = [
        int("0" + "".join([input[i][j] for i, _ in enumerate(input[:-1])]).strip())
        for j, _ in enumerate(input[0])
    ]

    chunks = [
        list(group) for k, group in groupby(transposed, key=lambda x: x != 0) if k
    ]

    def calculate(cols):
        return sum([sum(col) if op == "+" else prod(col) for col, op in zip(cols, ops)])

    return calculate(cols), calculate(chunks)


print(solve([line.rstrip("\r\n") for line in stdin]))
