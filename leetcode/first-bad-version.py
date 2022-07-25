# 278. First Bad Version
# 🟢 Easy
#
# https://leetcode.com/problems/first-bad-version/
#
# Tags: Binary Search - Interactive
#
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

import timeit


def isBadVersion(val):
    return val >= 45


# Binary search with a twist, looking for the leftmost item that matches
# a given condition. The condition needs to be tested via a function call.
#
# This problem displays a good example of why it is important for software
# engineers to understand algorithms, and not be completely reliant on
# libraries. The problem can be solved using binary search, but the fact
# that we don't have an array of items, and instead need to call the API to
# check 'if the version is a bad one'
#
# Runtime: 53 ms, faster than 28.22% of Python3 online submissions for First Bad Version.
# Memory Usage: 13.8 MB, less than 96.88 % of Python3 online submissions for First Bad Version.
class Solution:
    def firstBadVersion(self, n: int) -> int:
        good = 0  # The first bad could be the first one '1'
        bad = n
        while bad - good > 1:
            mid = (bad + good) // 2
            if isBadVersion(mid):
                # Could be a version before
                bad = mid
            else:
                # Could be this one or a version after
                good = mid
        return bad


def test():
    executors = [Solution]
    tests = [
        [100000, 45],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for t in tests:
                sol = executor()
                result = sol.firstBadVersion(t[0])
                expected = t[1]
                assert result == expected, f"{result} != {expected} for {t[0]} using {executor.__name__} solution"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
