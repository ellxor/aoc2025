from sys import stdin


def solve(input):
    points = [tuple(map(int, line.split(","))) for line in input]

    def dist(a, b):
        (x1, y1, z1), (x2, y2, z2) = a, b
        return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

    connections = [
        (i, j, dist(points[i], points[j]))
        for i in range(len(points))
        for j in range(i + 1, len(points))
    ]

    connections.sort(key=lambda c: c[2])  # this sorts far too many items...
    circuits = list(range(len(points)))  # each point has its own circuit ID
    merged, part1, part2 = 0, 0, 0

    for i, (a, b, _) in enumerate(connections):
        if i == 1000:
            sizes = [circuits.count(i) for i in range(len(points))]
            sizes.sort(reverse=True)  # as does this...
            part1 = sizes[0] * sizes[1] * sizes[2]

        if circuits[a] == circuits[b]:
            continue

        circuits = [circuits[a] if x == circuits[b] else x for x in circuits]
        merged += 1

        if merged == len(points) - 1:
            part2 = points[a][0] * points[b][0]

    return part1, part2


print(solve([line.rstrip("\r\n") for line in stdin]))
