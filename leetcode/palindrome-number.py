# 9. Palindrome Number
# 🟢 Easy
#
# https://leetcode.com/problems/palindrome-number/
#
# Tags: Math

import timeit


# Reverse the integer and compare the original one with the reversed
# version.
#
# Time complexity: O(log(n)) - The complexity comes from reversing the
# number, on each step, we divide the number by 10.
# Space complexity: O(1) - The algorithm uses constant memory.
#
# Runtime: 189 ms, faster than 6.78%
# Memory Usage: 13.9 MB, less than 16.33%
class ReverseAndCompare:
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

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return self.reverse(x) == x


# We can improve the previous solution if we realize that we only need
# to reverse half the number and compare that reversed half with the
# remaining value.
#
# Time complexity: O(log(n)) - The complexity comes from reversing the
# number, on each step, we divide the number by 10.
# Space complexity: O(1) - The algorithm uses constant memory.
#
# Runtime: 145 ms, faster than 28.87%
# Memory Usage: 13.9 MB, less than 16.33%
class ReverseHalf:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        num, rev = x, 0
        while num > rev:
            num, mod = divmod(num, 10)
            rev = rev * 10 + mod
        return num == rev or num == rev // 10


def test():
    executors = [
        ReverseAndCompare,
        ReverseHalf,
    ]
    tests = [
        [10, False],
        [121, True],
        [1221, True],
        [-121, False],
        [12321, True],
        [123321, True],
        [1234321, True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isPalindrome(t[0])
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
