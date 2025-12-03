from sys import stdin


def find_max_joltage(bank, count):
    total = 0

    for i in range(count, 0, -1):
        # must leave at least (i - 1) digits free after
        next_digit = max(bank[: len(bank) - (i - 1)])
        bank = bank[bank.index(next_digit) + 1 :]
        total = 10 * total + next_digit

    return total


def solve(input):
    banks = [list(map(int, line.rstrip())) for line in input]
    part1, part2 = 0, 0

    for bank in banks:
        part1 += find_max_joltage(bank, 2)
        part2 += find_max_joltage(bank, 12)

    return part1, part2


print(solve([line for line in stdin]))
