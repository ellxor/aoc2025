def solve(input):
    ranges = [map(int, pair.split("-")) for pair in input.split(",")]  # parse input
    part1, part2 = 0, 0

    for a, b in ranges:
        seen = set()

        for length in range(len(str(a)), len(str(b)) + 1):
            # increase a or decrease b to 'length' number of digits
            start = max(a, 10 ** (length - 1))
            end = min(b, 10**length - 1)

            # number of chunks that number can be divided into
            factors = [f for f in range(2, length + 1) if length % f == 0]

            for factor in factors:
                base = length // factor
                # step to increment all chunks by 1 in parallel
                step = sum([10 ** (i * base) for i in range(factor)])

                # round start up to multiple of step (first repeating number)
                begin = start + step - 1
                begin -= begin % step

                for i in range(begin, end + 1, step):
                    # important to prevent duplicates, e.g. 11,11,11 and 111,111
                    if i not in seen:
                        part1 += i if factor == 2 else 0
                        part2 += i
                        seen.add(i)

    return part1, part2


print(solve(input()))
