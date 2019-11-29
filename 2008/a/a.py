# python 3.7.2
# https://code.google.com/codejam/contest/dashboard?c=32013#s=p0

def intake():
    N = int(input())
    for c in range(1, N+1):
        ne = int(input())  # number of engines
        engines = {input(): n for n in range(ne)}
        nq = int(input())  # number of queries
        queries = [input() for _ in range(nq)]
        switches = solve(engines, queries)
        print('Case #{}: {}'.format(c, switches))


def is_power_of_two(number):
    return number & (number-1) == 0


def solve(engines: dict, queries) -> int:
    switches = 0  # number of switches required
    control = 0
    mask = 2**len(engines) - 1  # flag for each engine
    for q in queries:
        n = engines[q]
        control = control | 2**n
        if control == mask:
            switches += 1
            control = 2**n  # set to current active engine
        # print('{}->{:05b}'.format(n, control))
    return switches


def main():
    intake()


if __name__ == '__main__':
    main()