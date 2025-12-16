from heapq import heapify, nlargest
from itertools import combinations
from math import hypot, prod
from sys import stdin


def solve(input):
    points = [tuple(map(int, line.split(","))) for line in input]

    def dist(a, b):
        (x1, y1, z1), (x2, y2, z2) = a, b
        return hypot(x1 - x2, y1 - y2, z1 - z2)

    connections = sorted(
        (
            (dist(pi, pj), i, j)
            for (i, pi), (j, pj) in combinations(enumerate(points), 2)
        ),
        key=lambda p: p[0],
    )

    circuits = list(range(len(points)))  # each point has its own circuit ID
    merged, part1, part2 = 0, 0, 0

    for i, (_, a, b) in enumerate(connections):
        if i == 1000:
            sizes = [circuits.count(p) for p in range(len(points))]
            heapify(sizes)
            part1 = prod(nlargest(3, sizes))

        if circuits[a] == circuits[b]:
            continue

        circuits = [circuits[a] if x == circuits[b] else x for x in circuits]
        merged += 1

        if merged == len(points) - 1:
            part2 = points[a][0] * points[b][0]
            break

    return part1, part2


print(solve([line.rstrip() for line in stdin]))
