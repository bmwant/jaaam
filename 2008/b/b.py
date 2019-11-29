# python 3.7.2
# https://code.google.com/codejam/contest/dashboard?c=32013#s=p1
from enum import IntEnum


class Priority(IntEnum):
    B_ARV = 1  # arrived from B station (available at A)
    A_ARV = 2  # arrived from A station (available at B)
    A_DPT = 3  # departured from A station (not available at A)
    B_DPT = 4  # departured from B station (not available at B)


def intake():
    N = int(input())

    for c in range(1, N+1):
        T = int(input())
        schedule = []
        NA, NB = [int(n) for n in input().split(' ')]
        for na in range(NA):
            start, end = input().split()
            schedule.append((time_to_int(start), Priority.A_DPT))
            schedule.append((time_to_int(end)+T, Priority.A_ARV))

        for nb in range(NB):
            start, end = input().split()
            schedule.append((time_to_int(start), Priority.B_DPT))
            schedule.append((time_to_int(end)+T, Priority.B_ARV))

        Atrains, Btrains = solve(schedule)
        print('Case #{}: {} {}'.format(c, Atrains, Btrains))


def time_to_int(time_str) -> int:
    hours, minutes = time_str.split(':')
    return 60*int(hours) + int(minutes)


def solve(schedule) -> int:
    Amax = 0
    Bmax = 0
    A = 0  # track number of trains on A station
    B = 0  # track number of trains on B station
    schedule.sort()
    for t, p in schedule:
        if p == Priority.A_DPT:
            A -=1  # train departed from A
        elif p == Priority.A_ARV:
            B += 1  # train can depart from B
        elif p == Priority.B_DPT:
            B -= 1  # train departed from B
        elif p == Priority.B_ARV:
            A += 1  # train can depart from A

        Amax = min(Amax, A)
        Bmax = min(Bmax, B)
    return abs(Amax), abs(Bmax)


def main():
    intake()


if __name__ == '__main__':
    main()