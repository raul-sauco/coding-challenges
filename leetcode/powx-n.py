# 50. Pow(x, n)
# 🟠 Medium
#
# https://leetcode.com/problems/powx-n/
#
# Tags: Math - Recursion


import timeit

from numpy import log


# There is a simple solution where we simulate the operation multiplying
# the number by itself n times.
#
# Time complexity: O(n)
# Space complexity; O(1)
#
# The test cases are probably designed to make this solution fail with
# Time Limit Exceeded, and make us find a better solution.
class Simulate:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        exp = abs(n)
        for _ in range(exp):
            res *= x

        if n < 0:
            return round(1 / res, 5)
        return round(res, 5)


# Use divide-and-conquer and recursion to perform only a log(n) number
# of operations. We will recursively divide the problem into two smaller
# problems and multiply the result.
#
# i.e. (x, 5) => (x, 3) * (x, 2)
#
# Time complexity: O(log(n)) - We divide the exponent by 2 each call.
# Space complexity; O(log(n)) - We will have log(n) recursive calls.
#
# This solution should be valid but it fails the LeetCode tests, I
# believe the problem is that the tests use an internal function and
# only round the end result, instead of rounding every intermediate
# one.
#
# Expected 54.83676 differs from result 54.83508.
class LogRecursion:
    def myPow(self, x: float, n: int) -> float:
        # Base case, 0 to any power is still 0.
        if x == 0:
            return 0
        # Base case, any base to the power of 0 is 1.
        if n == 0:
            return 1
        # Handle negative exponents early, we will check the sign of n
        # before the return and adjust.
        exp = n if n > 0 else -n
        # Base case, any number to the power of 1 is itself.
        if exp == 1:
            return x if n > 0 else 1 / x
        # Divide-and-conquer by dividing the exponent into two halves.
        res = self.myPow(x * x, exp // 2)
        # If we have a negative exponent, we need to multiply once more.
        if n % 2 == 1:
            res *= x
        # Take care of negative exponents.
        if n < 0:
            return round(1 / res, 5)
        return round(res, 5)


# Similar to the previous solution but define an internal function and
# only round the final result to pass the LeetCode tests.
#
# Time complexity: O(log(n)) - We divide the exponent by 2 each call.
# Space complexity; O(log(n)) - We will have log(n) recursive calls.
#
# Runtime: 79 ms, faster than 5.43% of Python3 online submissions for
# Pow(x, n).
# Memory Usage: 14 MB, less than 19.38% of Python3 online submissions
# for Pow(x, n).
class Recursion:
    def myPow(self, x: float, n: int) -> float:
        def p(base: float, exp: int) -> float:
            # Base case, 0 to any power is still 0.
            if base == 0:
                return 0
            # Base case, any base to the power of 0 is 1.
            if exp == 0:
                return 1
            # Base case, any number to the power of 1 is itself.
            if exp == 1:
                return base
            # Divide-and-conquer.
            res = p(base * base, exp // 2)
            # If we have an odd exponent, we need to multiply once more.
            if exp % 2 == 1:
                res *= base
            return res

        # Initial call to the recursive function.
        res = p(x, abs(n))
        # Take care of negative exponents.
        if n < 0:
            return round(1 / res, 5)
        return round(res, 5)


# We can also use math to calculate the result, but it does not feel too
# different from just calling pow(x, n).
#
# Runtime: 67 ms, faster than 9.67% of Python3 online submissions for
# Pow(x, n).
# Memory Usage: 13.9 MB, less than 19.38% of Python3 online submissions
# for Pow(x, n).
class Math:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        elif x < 0:
            if n % 2 == 0:
                res = 2 ** (n * log(abs(x)) / log(2))
            else:
                res = -1 * 2 ** (n * log(abs(x)) / log(2))
        else:
            res = 2 ** (n * log(x) / log(2))
        return res


def test():
    executors = [
        Simulate,
        # LogRecursion, # Fails due to rounding intermediate results.
        Recursion,
        Math,
    ]
    tests = [
        [0.44894, -5, 54.83508],
        [2.00000, 0, 1.00000],
        [0.00000, 10, 0.00000],
        [2.00000, 10, 1024.00000],
        [2.10000, 3, 9.26100],
        [2.00000, -2, 0.25000],
        [2.00000, 1, 2.00000],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for idx, t in enumerate(tests):
                sol = executor()
                result = sol.myPow(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {idx} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
