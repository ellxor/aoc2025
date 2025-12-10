from functools import reduce
from itertools import chain, combinations
from sys import stdin

import z3


def parse(line):
    tokens = [token[1:-1] for token in line.split()]
    indicator, wiring, joltage = tokens[0], tokens[1:-1], tokens[-1]

    indicator = sum([(c == "#") << i for i, c in enumerate(indicator)])
    wiring = [sum([1 << int(n) for n in token.split(",")]) for token in wiring]
    joltage = list(map(int, joltage.split(",")))

    return indicator, wiring, joltage


def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def solve_part1(puzzle):
    (indicator, wiring, _) = puzzle

    for subset in powerset(wiring):
        if indicator == reduce(lambda a, b: a ^ b, subset, 0):
            return len(subset)

    assert False, "failed to solve puzzle"


def solve_part2(puzzle):
    (_, wiring, joltage) = puzzle
    vectors = [[(w >> bit) & 1 for bit in range(len(joltage))] for w in wiring]
    coeffs = [z3.Int(f"c_{i}") for i, _ in enumerate(vectors)]

    solver = z3.Optimize()
    solver.minimize(z3.Sum(coeffs))

    for ci in coeffs:
        solver.add(ci >= 0)

    for i, j in enumerate(joltage):
        solver.add(j == z3.Sum(c for c, v in zip(coeffs, vectors) if v[i]))

    assert solver.check()
    model = solver.model()

    return sum([model[c].as_long() for c in coeffs])


def solve(input):
    puzzles = [parse(line) for line in input]

    part1 = sum(map(solve_part1, puzzles))
    part2 = sum(map(solve_part2, puzzles))

    return part1, part2


print(solve(stdin))
