from sys import stdin


def remove_stacks(grid, focus):
    width = len(grid[0])
    height = len(grid)
    total = 0

    next = [row.copy() for row in grid]
    delta = set()

    for x, y in focus:
        if grid[y][x]:
            nbors = [
                (x + dx, y + dy)
                for dx in range(-1, 2)
                for dy in range(-1, 2)
                if not (dx == 0 and dy == 0)
                if x + dx >= 0 and x + dx < width
                if y + dy >= 0 and y + dy < height
            ]

            if sum([grid[ny][nx] for (nx, ny) in nbors]) < 4:
                next[y][x] = False
                delta.update(nbors)
                total += 1

    return total, next, delta


def solve(input):
    grid = [[c == "@" for c in line] for line in input]
    focus = set([(x, y) for y in range(len(grid)) for x in range(len(grid[0]))])

    part1, grid, delta = remove_stacks(grid, focus)
    part2 = part1

    while True:
        removed, grid, delta = remove_stacks(grid, delta)
        part2 += removed

        if not removed:
            break

    return part1, part2


print(solve([line.rstrip() for line in stdin]))
