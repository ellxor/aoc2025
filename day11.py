from sys import stdin


def count_paths(
    curr,
    nodes,
    memo,
    found_dac=True,
    found_fft=True,
):
    if curr == "out":
        return found_dac and found_fft

    key = (curr, found_dac, found_fft)

    if key in memo:
        return memo[key]

    total = 0

    for child in nodes[curr]:
        total += count_paths(
            child,
            nodes,
            memo,
            found_dac or curr == "dac",
            found_fft or curr == "fft",
        )

    memo[key] = total
    return total


def parse(line):
    node, children = line.split(":")
    return node, children.split()


def solve(input):
    nodes = {node: children for (node, children) in map(parse, input)}

    part1 = count_paths("you", nodes, {})
    part2 = count_paths(
        "svr",
        nodes,
        {},
        found_dac=False,
        found_fft=False,
    )

    return part1, part2


print(solve([line.rstrip() for line in stdin]))
