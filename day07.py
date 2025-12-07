from sys import stdin


def propagate(grid, x, y, counts):
    if y == len(grid):
        return 0, 1  # only count when gets to end for part2

    if (x, y) in counts:
        return 0, counts[(x, y)]  # if seen before, no need to continue for part 1 or 2

    if grid[y][x] == "^":
        a1, a2 = propagate(grid, x - 1, y, counts)
        b1, b2 = propagate(grid, x + 1, y, counts)

        p1 = 1 + a1 + b1  # add one to count number of splits
        p2 = a2 + b2

        counts[(x, y)] = p2
        return p1, p2

    return propagate(grid, x, y + 1, counts)


def solve(input):
    x, y = input[0].index("S"), 0
    return propagate(input, x, y, {})


print(solve([line.rstrip("\r\n") for line in stdin]))
