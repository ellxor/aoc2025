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

    # sort to largest ranges first -> prevents range from splitting other range in half
    keys.sort(key=lambda pair: pair[1] - pair[0], reverse=True)

    for i, (a, b) in enumerate(keys):
        part2 += max(b - a + 1, 0)  # some ranges may have been flipped below

        for j, (c, d) in enumerate(keys[i + 1 :]):
            if a <= c <= b:
                c = b + 1
            if a <= d <= b:
                d = a - 1

            keys[i + 1 + j] = (c, d)

    return part1, part2


print(solve([line.rstrip() for line in stdin]))
