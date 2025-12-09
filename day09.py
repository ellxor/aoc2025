from itertools import combinations
from sys import stdin


def point_in_shape(x, y, boundaries):
    cross = 0

    for (px, py), (qx, qy) in boundaries:
        if min(px, qx) <= x <= max(px, qx) and y == py == qy:
            return True

        if min(py, qy) <= y <= max(py, qy) and not (y == py == qy):
            if x == px == qx:
                return True

            cross += x < px

    return cross % 2 == 1


def no_collisions(boundaries, a, b):
    for p, q in boundaries:
        c1 = min(a[0], b[0]) >= max(p[0], q[0])
        c2 = max(a[0], b[0]) <= min(p[0], q[0])
        c3 = min(a[1], b[1]) >= max(p[1], q[1])
        c4 = max(a[1], b[1]) <= min(p[1], q[1])

        if not (c1 or c2 or c3 or c4):
            return False

    return True


def solve(input):
    points = [tuple(map(int, line.split(","))) for line in input]
    boundaries = [(p, points[i + 1]) for i, p in enumerate(points[:-1])]
    boundaries.append((points[-1], points[0]))

    c = [
        (a, b, (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1))
        for a, b in combinations(points, 2)
    ]

    c.sort(key=lambda x: x[2], reverse=True)
    part1, part2 = c[0][2], 0

    for a, b, size in c:
        ax, ay = a
        bx, by = b

        if no_collisions(boundaries, a, b):
            if point_in_shape(ax, by, boundaries) and point_in_shape(bx, ay, boundaries):
                part2 = size
                break

    return part1, part2


print(solve([line.rstrip() for line in stdin]))
