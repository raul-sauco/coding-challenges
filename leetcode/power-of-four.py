# 342. Power of Four
# 🟢 Easy
#
# https://leetcode.com/problems/power-of-four/
#
# Tags: Math - Bit Manipulation - Recursion

import timeit
from math import log


# A very simple way is to keep generating powers of 4 until we have a
# value that either matches or is greater than n.
#
# Time complexity: O(log(n)) - Each time we multiply by 4.
# Space complexity: O(1) - Constant space.
#
# Runtime: 30 ms, faster than 96.09%
# Memory Usage: 13.9 MB, less than 54.38%
class Recursive:
    def isPowerOfFour(self, n: int) -> bool:
        # Start with 4^0, do not consider negative exponents because
        # n is an integer.
        p = 1
        # While the power is <= than the input.
        while p <= n:
            # If the power equals the input, return True.
            if p == n:
                return True
            # Find the next power of 4.
            p *= 4
        # If we have an integer bigger than n and it is not a power of 4
        # the input is not a power of 4.
        return False


# A power of 4 converted to binary will be a single 1 followed by an
# even number of 0s, could be 0 0s. Check if the input matches.
#
# Time complexity: O(1) - Only comparison and bit manipulation.
# Space complexity: O(1) - Constant space.
#
# Runtime: 55 ms, faster than 41.22%
# Memory Usage: 13.9 MB, less than 54.38%
class BitManipulation:
    def isPowerOfFour(self, n: int) -> bool:
        # Check that the number is:
        # - Greater than 0
        # - Only contains one 1 by doing binary and with n-1.
        # - The only 1 is in an even position by doing binary and with
        #   a value that in binary is 1010101010101... 32 bits long
        return n > 0 and n & (n - 1) == 0 and n & 1431655765 == n


# We can also use the built-in log function and check if the result is
# an integer.
#
# Time complexity: O(1) - Not sure how log is implemented but probably
# O(1)
# Space complexity: O(1) - Constant space.
#
# Runtime: 36 ms, faster than 88.55%
# Memory Usage: 13.8 MB, less than 54.38%
class Log4:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        return log(n, 4) % 1 == 0


def test():
    executors = [
        Recursive,
        BitManipulation,
        Log4,
    ]
    tests = [
        [1, True],
        [5, False],
        [16, True],
        [4096, True],
        [65536, True],
        [262143, False],
        [262144, True],
        [-2147483648, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.isPowerOfFour(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
