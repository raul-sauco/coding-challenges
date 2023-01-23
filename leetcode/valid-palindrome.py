# 125. Valid Palindrome
# 🟢 Easy
#
# https://leetcode.com/problems/valid-palindrome/
#
# Tags: Two Pointers - String

import re
import timeit


# Solution using string.join and filter to clean up the non
# alphanumerical characters, then two pointers with a while loop to
# check if the remaining characters are a palindrome.
#
# Time complexity: O(n) - One pass to clean up the input and another to
# check if the remaining characters form a palindrome.
# Space complexity: O(1) - Only pointers stored in memory though maybe
# join and filter may use extra memory.
#
# Runtime: 43 ms, faster than 95.95%
# Memory Usage: 14.7 MB, less than 43.02%
class CleanThenCheck:
    def isPalindrome(self, s: str) -> bool:
        l = "".join(filter(str.isalnum, s)).lower()
        i, j = 0, len(l) - 1
        while i < j:
            if l[i] != l[j]:
                return False
            j -= 1
            i += 1
        return True


# Similar to the previous solution but substitute the while loop with
# a for loop.
#
# Time complexity: O(n) - One pass to clean up the input and another to
# check if the remaining characters form a palindrome.
# Space complexity: O(1) - Only pointers stored in memory though maybe
# join and filter may use extra memory.
#
# Runtime: 47 ms, faster than 91.78%
# Memory Usage: 14.7 MB, less than 43.02%
class ForLoop:
    def isPalindrome(self, s: str) -> bool:
        l = "".join(filter(str.isalnum, s)).lower()
        j = len(l) - 1
        for i in range(len(l) // 2):
            if l[i] != l[j]:
                return False
            j -= 1
        return True


# Solution using string.join and reversing the string
#
# Time complexity: O(n) - One pass to clean up the input and another to
# create the reversed string.
# Space complexity: O(n) - The reversed string uses extra memory.
#
# Runtime: 47 ms, faster than 91.78%
# Memory Usage: 14.8 MB, less than 36.86%
class CheckAgainstReverse:
    def isPalindrome(self, s: str) -> bool:
        l = "".join(filter(str.isalnum, s)).lower()
        return l == l[::-1]


# Solution using compiled regex and reversing the string
#
# Time complexity: O(n) - One pass to clean up the input and another to
# create the reversed string.
# Space complexity: O(n) - The reversed string uses extra memory.
#
# Runtime: 60 ms, faster than 68.44%
# Memory Usage: 15.3 MB, less than 23.03%
class UseRegex:
    def isPalindrome(self, s: str) -> bool:
        l = re.compile("[\W_]+").sub("", s).lower()
        return l == l[::-1]


# Similar to the first solution but avoid cleaning the string before
# we start checking characters, instead, for each pointer, check if the
# character under the pointer is alphanumeric, if it isn't, move the
# pointer forward.
#
# Time complexity: O(n) - One pass to clean up the input and another to
# check if the remaining characters form a palindrome.
# Space complexity: O(1) - Only pointers stored in memory though maybe
# join and filter may use extra memory.
#
# Runtime 125 ms Beats 11.87%
# Memory 14.8 Beats 44.73%
class TwoPointers:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            a = s[l].lower()
            b = s[r].lower()
            if a != b:
                return False
            l += 1
            r -= 1
        return True


def test():
    executors = [
        CleanThenCheck,
        ForLoop,
        CheckAgainstReverse,
        UseRegex,
        TwoPointers,
    ]
    tests = [
        [" ", True],
        [".,", True],
        ["0P", False],
        ["race a car", False],
        ["A man, a plan, a canal: Panama", True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1000):
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
