from itertools import combinations, product
from sys import stdin


def parse(line):
    tokens = [token[1:-1] for token in line.split()]
    indicator, wiring, joltage = tokens[0], tokens[1:-1], tokens[-1]

    indicator = tuple((c == "#") for c in indicator)
    wiring = [tuple(map(int, token.split(","))) for token in wiring]
    joltage = tuple(map(int, joltage.split(",")))

    wiring = [tuple(int(i in w) for i, _ in enumerate(indicator)) for w in wiring]
    return indicator, wiring, joltage


def build_parity_table(wiring, count):
    table = {parity: [] for parity in product(range(2), repeat=count)}
    zeros = tuple(0 for _ in range(count))

    for length in range(len(wiring) + 1):
        for subset in combinations(wiring, length):
            jolt = tuple(sum(c) for c in zip(zeros, *subset))
            parity = tuple(j % 2 for j in jolt)
            table[parity].append((len(subset), jolt))

    return table


def solve_part2(table, joltage, seen):
    if all(j == 0 for j in joltage):
        return 0

    if joltage in seen:
        return seen[joltage]

    parity = tuple(j % 2 for j in joltage)
    presses = 10**10

    for length, diff in table[parity]:
        if all(d <= j for d, j in zip(diff, joltage)):
            divide = solve_part2(
                table, tuple((j - d) // 2 for d, j in zip(diff, joltage)), seen
            )

            presses = min(
                presses,
                length + 2 * divide,
            )

    seen[joltage] = presses
    return presses


def solve(input):
    part1, part2 = 0, 0

    for puzzle in map(parse, input):
        indicator, wiring, joltage = puzzle
        table = build_parity_table(wiring, len(joltage))

        part1 += table[indicator][0][0]
        part2 += solve_part2(table, joltage, {})

    return part1, part2


print(solve(stdin))
