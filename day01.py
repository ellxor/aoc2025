from sys import stdin


def solve(input):
    direction = {"L": -1, "R": +1}
    part1, part2 = 0, 0
    curr = 50

    for line in input:
        old = curr
        curr += direction[line[0]] * int(line[1:])
        part2 += abs(curr) // 100  # count number of times wrapped
        part2 += curr <= 0 and old != 0  # count times passing true 0
        curr %= 100
        part1 += curr == 0  # count number of times 0 is hit exactly

    return part1, part2


print(solve([line for line in stdin]))
