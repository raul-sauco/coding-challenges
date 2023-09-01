# 338. Counting Bits
# 🟢 Easy
# https://leetcode.com/problems/counting-bits/
#
# Tags: Dynamic Programming - Bit Manipulation

import timeit
from typing import List


# Group numbers by their ln, for each group, assign the same as the
# corresponding item in the previous group + 1.
#
# Time complexity: O(n) - One pass over each digit from 0 to n.
# Space complexity: O(1) - Constant space if we do not take into account
# the output array, O(n) if we do.
#
# Runtime 160 ms Beats 39.35%
# Memory 20.9 MB Beats 29.70%
class DP:
    def countBits(self, n: int) -> List[int]:
        # Base cases
        if not n:
            return [0]
        if n == 1:
            return [0, 1]

        res = [0] * (n + 1)
        res[1] = 1
        factor = 2

        while True:
            # Fill a new interval of [2-3][4-7][8-15]...
            for i in range(factor):
                idx = factor + i
                # This position's last bits will be the same as the same
                # position in the previous group.
                res[idx] = res[i] + 1
                if idx == n:
                    return res
            # Get set for the next interval.
            factor *= 2


# Same idea as above but instead of using a loop to check when we need to
# update the factor, we check when the current index is equal to the factor,
# then multiply by 2.
#
# Time complexity: O(n) - The loop runs once for each value between 0 and n.
# Space complexity: O(1) - Constant space if we do not take into account the
# output array, if we do O(n)
#
# Runtime 134 ms Beats 57.51%
# Memory 20.8 MB Beats 78.91%
class DPOffset:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        factor = 1
        for i in range(1, n + 1):
            if factor * 2 == i:
                factor = i
            res[i] = 1 + res[i - factor]
        return res


def test():
    executors = [DP, DPOffset]
    tests = [
        [0, [0]],
        [1, [0, 1]],
        [2, [0, 1, 1]],
        [5, [0, 1, 1, 2, 1, 2]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.countBits(t[0])
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
