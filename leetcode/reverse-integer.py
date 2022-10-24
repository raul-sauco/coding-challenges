# 7. Reverse Integer
# 🟠 Medium
#
# https://leetcode.com/problems/reverse-integer/
#
# Tags: Math

import timeit


# Decompose the input into its constituent digits, then reverse them and
# construct a value that has all digits at their corresponding place, to
# do that, we can use the fact that we are using base 10 and multiply
# each number by 10^i where i is its order in the resulting digit.
#
# Time complexity: O(n) - With n the number of digits in the input or
# O(log(n)) with n the value of the input, at each iteration of the
# loop we divide this value by 10.
# Space complexity: O(n) - With n the number of digits in the input, we
# store a list of the input's value digits.
#
# Runtime: 72 ms, faster than 16.21%
# Memory Usage: 13.9 MB, less than 64.41%
class ByDigits:
    def reverse(self, x: int) -> int:
        # Work with the absolute value.
        num = abs(x)
        # Split the number into its digits.
        digits = []
        while num > 0:
            num, digit = divmod(num, 10)
            digits.append(digit)
        # 2^31 with its last digit chopped off, we use this value to
        # check overflow because we are reconstructing the reversed
        # integer from most significant to least significant digit.
        MAX = 147483648
        res = 0
        power = 1
        # Start adding the digits at their corresponding place.
        # 12345 => 1 * 10_000 + 2 * 1_000 + 3 * 100 + 4 * 10 + 5 * 1
        for digit in reversed(digits):
            # Check if adding this digit at the start of this value
            # would overflow.
            if ((x > 0 and res >= MAX) or (x < 0 and res > MAX)) and digit > 1:
                return 0
            res += digit * power
            power *= 10
        # Remember to add the sign if needed.
        return res if x >= 0 else -res


# Same logic as the previous version but merge the two loops into one.
#
# Time complexity: O(log(n)) - Where n is the value of the input x, for@
# each iteration of the input we divide the value by 10, the loop will
# run log(n) times.
# Space complexity: O(1) - We only use constant space besides input and
# output values.
#
# Runtime: 57 ms, faster than 60.21%
# Memory Usage: 13.8 MB, less than 97.07%
class OneLoop:
    def reverse(self, x: int) -> int:
        # 2^31 // 10
        MAX = 214748364
        num = abs(x)
        res = 0
        while num:
            # Pop the last digit.
            num, digit = divmod(num, 10)
            # Check if adding the current digit would result in integer
            # overflow using 32 bit integers. We check both negative and
            # positive integer overflow depending on the sign of x.
            if res > MAX or (
                res == MAX and ((x > 0 and digit > 7) or (x < 0 and digit > 8))
            ):
                return 0
            # If safe, add the current digit to the reversed integer.
            res = res * 10 + digit
        # Readd the sign and return the reversed integer.
        return res if x >= 0 else -res


def test():
    executors = [
        ByDigits,
        OneLoop,
    ]
    tests = [
        [0, 0],
        [120, 21],
        [123, 321],
        [-123, -321],
        [8463847412, 0],  # MAX_INT + 1
        [1534236469, 0],
        [-9463847412, 0],  # MIN_INT - 1
        [1463847412, 2147483641],
        [7463847412, 2147483647],  # Max positive value when reversed.
        [-8463847412, -2147483648],  # Max negative value when reversed.
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.reverse(t[0])
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
