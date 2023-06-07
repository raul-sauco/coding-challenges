# 1318. Minimum Flips to Make a OR b Equal to c
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
#
# Tags: Bit Manipulation

import timeit


# Iterate over the least significant bit of the input values, check how
# many operations would take to make that bit in a or b == the bit in c,
# then right shift the three values by one and do it again.
#
# Time complexity: O(log(n)) - We iterate over the number of binary
# digits in the biggest value in the input, that is log2(n)
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 39 ms Beats 81.54%
# Memory 16.2 MB Beats 87.91%
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            if c & 1:
                res += int(not (a & 1 or b & 1))
            else:
                res += (a & 1) + (b & 1)
            a >>= 1
            b >>= 1
            c >>= 1
        return res


def test():
    executors = [Solution]
    tests = [(2, 6, 5, 3), (4, 2, 7, 1), (1, 2, 3, 0)]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minFlips(t[0], t[1], t[2])
                exp = t[3]
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
