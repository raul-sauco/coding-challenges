# 1071. Greatest Common Divisor of Strings
# 🟢 Easy
#
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
#
# Tags: Math - String

import timeit
from math import gcd


# If both input strings are formed by concatenating the same substring,
# then concatenating them should be an associative operation, we can
# use that to check if they have a GCD string. Once we know that they do,
# we know that the length of the GCD string will be the length of the
# GCD of their respective lengths.
#
# Time complexity: O(m+n) - We need to iterate both input strings to
# concatenate them and check if they have a GCD. The `gcd` function
# takes O(log(m*n)) time.
# Space complexity: O(m+n) - The concatenated strings use extra memory.
#
# Runtime 22 ms Beats 99.41%
# Memory 13.8 MB Beats 98.52%
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # A function to return the GCD between two numbers using the
        # Euclidean algorithm. Iterative version with O(1) space.
        def euc(a: int, b: int) -> int:
            if a < b:
                a, b = b, a
            while b:
                a, b = b, a % b
            return a

        # If the result of concatenating the strings is the same
        # independently of the order in which we concatenate them, then
        # they are both formed of the same substrings.
        return (
            str1[: gcd(len(str1), len(str2))]
            if str1 + str2 == str2 + str1
            else ""
        )


def test():
    executors = [Solution]
    tests = [
        ["LEET", "CODE", ""],
        ["ABCABC", "ABC", "ABC"],
        ["ABABAB", "ABAB", "AB"],
        ["ABABABAB", "ABAB", "ABAB"],
        ["ABBAABBA", "ABBA", "ABBA"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.gcdOfStrings(t[0], t[1])
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
