# 263. Ugly Number
# 🟢 Easy
#
# https://leetcode.com/problems/ugly-number/
#
# Tags: Math

import timeit


# Divide the input by each of the three factors as long as it is
# possible, if the remainder is not 1, return false.
#
# Time complexity: O(log(n)) - At each step we divide the input by
# either 2, 3, or 5.
# Space complexity: O(1)
#
# Runtime: 32 ms, faster than 95.18%
# Memory Usage: 13.8 MB, less than 60.08%
class Iterative:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        for factor in (2, 3, 5):
            while not n % factor:
                n /= factor
        return n == 1


# Use math to solve the problem. If the input is a divisor of 30^32
# (2 * 3 * 5) ^ 32, then its only factors are the these numbers.
#
# Time complexity: O(1) - There is only one computation, so it should be
# considered O(1)? But the computation involves a fairly big number,
# locally it is slower than the O(log(n)) solution.
# Space complexity: O(1) - Even though it uses a pretty large integer.
#
# Runtime: 32 ms, faster than 95.18%
# Memory Usage: 13.8 MB, less than 60.08%
class Math:
    def isUgly(self, n: int) -> bool:
        return n > 0 == 30**32 % n


def test():
    executors = [
        Iterative,
        Math,
    ]
    tests = [
        [6, True],
        [1, True],
        [0, False],
        [14, False],
        [-6, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isUgly(t[0])
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
