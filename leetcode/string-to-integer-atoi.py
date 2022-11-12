# 8. String to Integer (atoi)
# 🟠 Medium
#
# https://leetcode.com/problems/string-to-integer-atoi/
#
# Tags: String

import timeit


# Follow the steps on the problem's description one after the other.
# The ony case that needs to be handled is when the result goes over
# the max, or under the min, for a 32 bit integer, in Python we can
# simply handle that with a conditional.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input string, we visit each character until the end of the digits,
# which could also be the end of the input, and for each, do O(1) work.
# Space complexity: O(1) - We only store 4 integers, a dictionary of
# size 10 and one boolean.
#
# Runtime: 40 ms, faster than 88.98%
# Memory Usage: 13.9 MB, less than 29.59%
class Solution:
    def myAtoi(self, s: str) -> int:
        # Define the boundaries of a 32 bit integer.
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        # The length of the string.
        L = len(s)
        # A map of string digits to numerical digits.
        d = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        i = 0
        # Skip whitespace.
        while i < L and s[i] == " ":
            i += 1
        # Check if there is a sign and read it.
        neg = False
        if i < L and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                neg = True
            i += 1
        # Read digits.
        res = 0
        while i < L and s[i] in d:
            res *= 10
            res += d[s[i]]
            i += 1
        # Ignore anything that comes after the digits.
        # If the result is negative, add the sign.
        if neg:
            res = -res
            return MIN_INT if res < MIN_INT else res
        return MAX_INT if res > MAX_INT else res


def test():
    executors = [Solution]
    tests = [
        ["", 0],
        ["42", 42],
        ["    -0", 0],
        ["   -42", -42],
        ["    -064 abc", -64],
        ["4193 with words", 4193],
        ["91283472332", 2147483647],
        ["-91283472332", -2147483648],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.myAtoi(t[0])
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
