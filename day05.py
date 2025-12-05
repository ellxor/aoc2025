from sys import stdin


def solve(input):
    index = input.index("")
    keys, test = input[:index], input[index + 1 :]

    keys = [tuple(map(int, key.split("-"))) for key in keys]
    test = list(map(int, test))

    part1, part2 = 0, 0

    for t in test:
        for a, b in keys:
            if a <= t <= b:
                part1 += 1
                break

    keys.sort(key=lambda pair: pair[0])
    min = 0

    for a, b in keys:
        part2 += max(b - max(min, a) + 1, 0)
        min = max(min, b + 1)

    return part1, part2


print(solve([line.rstrip() for line in stdin]))
