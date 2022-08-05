#!/usr/bin/env python
# -*- coding: utf-8 -*-

def checkValidString(s):
    lo = hi = 0
    for c in s:
        if c == '(':
            lo += 1
        else:
            lo -= 1
        # // lo += 1 if c == '(' else -1
        # hi += 1 if c != ')' else -1
        if c != ')':
            hi += 1
        else:
            hi -= 1
        print(c, ":", lo, hi)
        if hi < 0: break
        lo = max(lo, 0)
    return lo == 0


if __name__ == '__main__':
    #  print(checkValidString("(***)"))
    print(checkValidString(")(*"))
