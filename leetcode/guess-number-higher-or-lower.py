# 374. Guess Number Higher or Lower
# 🟢 Easy
#
# https://leetcode.com/problems/guess-number-higher-or-lower/
#
# Tags: Binary Search - Interactive

import timeit


# Use binary search, the only difference from standard binary search is
# that instead of checking nums[mid] against the value we are seeking,
# we call an API to check. This problem is very similar to first bad
# version.
#
# Time complexity: O(log(n))
# Space complexity: O(1)
#
# Runtime: 46 ms, faster than 73.32%
# Memory Usage: 13.9 MB, less than 66.34%
class BinarySearch:
    def __init__(self, val: int):
        self.val = val

    def guess(self, num: int) -> int:
        if num == self.val:
            return 0
        if num > self.val:
            return -1
        return 1

    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            pick = (l + r) // 2
            res = self.guess(pick)
            if res == 0:
                return pick
            if res == 1:
                l = pick + 1
            else:
                r = pick - 1
        return l


def test():
    executors = [
        BinarySearch,
    ]
    tests = [
        [1, 1],
        [2, 1],
        [10, 6],
        [2**31 - 1, 1],
        [2**31 - 1, 23124],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor(t[1])
                result = sol.guessNumber(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
