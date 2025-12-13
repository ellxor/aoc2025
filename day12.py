from sys import stdin


def parse(line):
    area, counts = line.split(":")
    return tuple(map(int, area.split("x"))), list(map(int, counts.split()))


def solve_puzzle(puzzle, areas, patterns):
    (x, y), counts = puzzle

    puzzle_area = sum(a * c for a, c in zip(areas, counts))
    grid_area = x * y

    if grid_area < puzzle_area:
        return False  # if there are more shaded area than available it cannot be solved

    if (x // 3) * (y // 3) >= sum(counts):
        return True  # simple solution of tiling all the tiles in a grid

    assert False, "orienting tiles is not implemented"


def solve(input):
    patterns = [input[i * 5 + 1 : i * 5 + 4] for i in range(6)]
    puzzles = map(parse, input[6 * 5 :])

    areas = [sum(row.count("#") for row in p) for p in patterns]
    part1 = sum(solve_puzzle(puzzle, areas, patterns) for puzzle in puzzles)

    return part1


print(solve([line.rstrip() for line in stdin]))
