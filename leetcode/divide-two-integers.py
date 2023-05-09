# 29. Divide Two Integers
# 🟠 Medium
#
# https://leetcode.com/problems/divide-two-integers/
#
# Tags: Math - Bit Manipulation

import timeit


# This solution is based on the fact that the quotient of a division is
# equal to the number of times the divisor goes into the dividend.
# We can use bitwise operations to get the quotient.
#
# Time complexity: O(log2(n)) - In each iteration we divide the initial
# dividend by 2.
# Space complexity: O(1) - We only store integer values.
#
# Runtime 50 ms Beats 9.81%
# Memory 16.4 MB Beats 11.94%
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Determine if the result will be negative
        negative = (dividend > 0 and divisor < 0) or (
            dividend < 0 and divisor > 0
        )
        # The problem has a constraint of -2147483648 to 2147483647
        upper_bound = 1 << 31 if negative else (1 << 31) - 1
        # Equivalent to using abs()
        dividend = 0 - dividend if dividend < 0 else dividend
        divisor = 0 - divisor if divisor < 0 else divisor
        # Convert the dividend to a binary list
        dividend = [int(x) for x in bin(dividend)[2:]]
        current_dividend = 0
        result = 0
        for next_digit in dividend:
            current_dividend = (current_dividend << 1) + next_digit
            if divisor <= current_dividend:
                current_dividend -= divisor
                new_digit = 1
            else:
                new_digit = 0
            result = (result << 1) + new_digit
        result = min(result, upper_bound)
        if negative:
            result = 0 - result
        return result


def test():
    MIN_ALLOWED = -2147483648
    MAX_ALLOWED = 2147483647
    executors = [Solution]
    tests = [
        [1, 1, 1],
        [0, 1, 0],
        [10, 3, 3],
        [7, -3, -2],
        [1 << 31, 1, MAX_ALLOWED],
        [1 << 31, -17, -126322567],
        [MIN_ALLOWED, -1, MAX_ALLOWED],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.divide(t[0], t[1])
                exp = t[2]
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
