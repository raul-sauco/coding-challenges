# 326. Power of Three
# 🟢 Easy
#
# https://leetcode.com/problems/power-of-three/
#
# Tags: Math - Recursion

import re
import timeit
from math import log

# 1e4 calls
#
# » IterativeMultiply   0.01302   seconds
# » IterativeDivision   0.01749   seconds
# » RecursiveDivision   0.02359   seconds
# » LogBase3            0.01375   seconds
# » CandidatesArray     0.01957   seconds
# » GreatestModule      0.01079   seconds
# » Base3Conversion     0.06819   seconds

# Start at 1 and keep multiplying by 3 until the result is either n or
# greater, if it is n, then n is a power of 3, if greater, it is not.
#
# Time complexity: O(log(n)) - We will loop log3(n) times.
# Space complexity: O(1) - Constant space.
#
# Runtime: 125 ms, faster than 59.50%
# Memory Usage: 13.8 MB, less than 57.97%
class IterativeMultiply:
    def isPowerOfThree(self, n: int) -> bool:
        # Start with the lowest exponent of 3, 3^0.
        res = 1
        # Iterate while res < n, this loop will not run for n < 2
        # returning false for all negative inputs.
        while res < n:
            # Multiply by 3.
            res *= 3
        # res either matches n or it is greater than.
        return res == n


# Keep dividing by 3 while the value is a multiple of 3, when it
# stops being a multiple of 3, check if the value is 1. This solution
# is faster than the multiplication, probably because it detects non
# multiples faster, instead of having to iterate up all the way to the
# input value.
#
# Time complexity: O(log(n)) - We will loop a max of log3(n) times.
# Space complexity: O(1) - Constant space.
#
# Runtime: 88 ms, faster than 89.67%
# Memory Usage: 13.9 MB, less than 16.98%
class IterativeDivision:
    def isPowerOfThree(self, n: int) -> bool:
        # Return earlier for inputs known to not be valid.
        if n < 1:
            return False
        # Iterate over the converted input while it is divisible by 3.
        while n % 3 == 0:
            n /= 3
        # Return whether the last value is 1.
        return n == 1


# Recursive version of the iterative division solution.
#
# Time complexity: O(log(n)) - We will loop a max of log3(n) times.
# Space complexity: O(log(n)) - The call stack will grow to log3(n).
#
# Runtime: 80 ms, faster than 94.70%
# Memory Usage: 14 MB, less than 16.98%
class RecursiveDivision:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (
            n == 1 or (n % 3 == 0 and self.isPowerOfThree(n / 3))
        )


class LogBase3:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        # 243 is a special case, at least in Python and Java.
        if n == 243:
            return True
        # Use Python's log function. Integer division by 1 converts the
        # result from float to integer.
        return log(n, 3) % 1 == 0


# Since we have such a small search space, it is worth precomputing all
# powers of 3 up to 2^31 and then just checking if n is one of them.
#
# Time complexity: O(1) - One comparison.
# Space complexity: O(1) - Constant space.
#
# Runtime: 97 ms, faster than 83.24%
# Memory Usage: 13.9 MB, less than 57.97%
class CandidatesArray:
    def isPowerOfThree(self, n: int) -> bool:
        candidates = {
            1,
            3,
            9,
            27,
            81,
            243,
            729,
            2187,
            6561,
            19683,
            59049,
            177147,
            531441,
            1594323,
            4782969,
            14348907,
            43046721,
            129140163,
            387420489,
            1162261467,
        }
        return n in candidates


# If we look at the candidates, we can see that the biggest of them must
# be divisible by any power of 3 smaller, or equal, to itself. This is a
# nice clean solution easy to read but slightly harder to understand.
#
# Time complexity: O(1)
# Space complexity: O(1)
#
# Runtime: 114 ms, faster than 70.00%
# Memory Usage: 13.9 MB, less than 16.98%
class GreatestModule:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (1162261467 % n == 0)


# Same as any power of 2 in base2 will be a single 1 digit followed by
# all 0s, so will be a power of 3 in base3. We can convert the input to
# a string in base3, then check if it matches the pattern.
#
# Time complexity: O(log(n)) - The conversion to string is probably
# implemented using divmod or a similar operation.
# Space complexity: O(1) - We save a string of max length 20.
#
# Runtime: 168 ms, faster than 26.18%
# Memory Usage: 13.8 MB, less than 57.97%
class Base3Conversion:
    def isPowerOfThree(self, n: int) -> bool:

        # Define an integer to any base function.
        # https://stackoverflow.com/a/28666223/2557030
        def numberToBase(n, b):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n % b))
                n //= b
            return digits[::-1]

        # Convert to base 3 and check that the result is in the pattern
        # 1 followed by any number of 0
        return n > 0 and bool(
            re.match(r"^1(0)*$", "".join(map(str, (numberToBase(n, 3)))))
        )


def test():
    executors = [
        IterativeMultiply,
        IterativeDivision,
        RecursiveDivision,
        LogBase3,
        CandidatesArray,
        GreatestModule,
        Base3Conversion,
    ]
    tests = [
        [-9, False],
        [0, False],
        [1, True],
        [9, True],
        [27, True],
        [243, True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isPowerOfThree(t[0])
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
