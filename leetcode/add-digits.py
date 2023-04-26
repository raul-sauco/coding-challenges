# 258. Add Digits
# 🟢 Easy
#
# https://leetcode.com/problems/add-digits/
#
# Tags: Math - Simulation - Number Theory

import timeit


# The straightforward solution is to recursively or iteratively compute
# the sum of some digits, for example the last two, until the value only
# has one digit.
#
# Time complexity: O(log(n)) - In each iteration, we divide by 100.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 34 ms Beats 62.21%
# Memory 13.8 MB Beats 39.79%
class Iterative:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = num // 10 + num % 10
        return num


# Using math, we can compute the digital root of a value using the mod
# of the value and the base-1.
#
# Time complexity: O(1) - Constant time.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 56 ms Beats 6.65%
# Memory 16.3 MB Beats 39.79%
class Math:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0


def test():
    executors = [
        Iterative,
        Math,
    ]
    tests = [
        [0, 0],
        [38, 2],
        [2147483647, 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.addDigits(t[0])
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
