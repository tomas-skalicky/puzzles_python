#!/usr/bin/env python3

'''
Created on Sep 25, 2015
'''
import itertools

def solution(A):
    s = sum(A)
    A.pop()
    return min(abs(s - 2 * x) for x in itertools.accumulate(A))

assert(solution([ 1, 2 ]) == 1)
assert(solution([ 1, 2, 3 ]) == 0)
assert(solution([ 3, 1, 2, 4, 3 ]) == 1)
assert(solution([ 1, 0, -1 ]) == 2)
print('SUCCESS')