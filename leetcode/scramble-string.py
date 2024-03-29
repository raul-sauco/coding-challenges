# 87. Scramble String
# 🔴 Hard
#
# https://leetcode.com/problems/scramble-string/
#
# Tags: String - Dynamic Programming - Divide and Conquer

import timeit
from collections import defaultdict
from functools import cache


# Iterate over the input strings' characters, if the strings are a full
# match, return true, if the character frequencies vary, return false,
# if neither of the conditions is true, we can try all the possible ways
# to split s1 in two, and try the result keeping both halves in place
# and swapping them, against s2, we can call isScramble recursively
# with the resulting substrings, if any of the options matches, s2 is
# a scrambled version of s1.
#
# Time complexity: O(n^4) - For each value i 0..n, where n is the length
# of the input strings, we need to try 4 variations of the substrings
# generated by splitting using i, 2 swapping and 2 not swapping.
# Space complexity: O(n^2) - Each call on the call stack will have its
# own copy of the substrings and the stack have a height of n.
# Since n <= 30, we may want to simplify both time and space as O(1) but
# the runtime changes significantly with the size of the input.
#
# Runtime 71 ms Beats 47.7%
# Memory 15.7 MB Beats 24.38%
class Memoization:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        # Check for a full match.
        is_full_match = True
        # Checking for frequency mismatches helps discard branches that
        # will not result in a match faster.
        freq = defaultdict(int)
        for i in range(n):
            if s1[i] != s2[i]:
                is_full_match = False
            freq[s1[i]] += 1
            freq[s2[i]] -= 1
            if not freq[s1[i]]:
                freq.pop(s1[i])
            if not freq[s2[i]]:
                freq.pop(s2[i])
        if is_full_match:
            return True
        # If the frequencies are not a match this cannot be a match.
        if freq:
            return False
        # Otherwise try different indexes at which we can split.
        for i in range(1, n):
            # Useful to see how we can split the strings.
            # print(f"no-swap: s1: {s1[:i]}/{s1[i:]}, s2: {s2[:i]}/{s2[i:]}")
            # print(f"swap: s1: {s1[:i]}/{s1[i:]}, s2: {s2[n-i:]}/{s2[:n-i]}")
            # We can split here and both swap or don't.
            if (
                self.isScramble(s1[:i], s2[:i])
                and self.isScramble(s1[i:], s2[i:])
            ) or (
                self.isScramble(s1[:i], s2[n - i :])
                and self.isScramble(s1[i:], s2[: n - i])
            ):
                return True
        # None of the splits match.
        return False


# We can shorten the previous solution by letting each branch run to its
# exhaustion. The solution is shorter but less efficient.
class Shorter:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n == 0 or (n == 1 and s1 == s2):
            return True
        for i in range(1, n):
            # We can split here and both swap or don't.
            if (
                self.isScramble(s1[:i], s2[:i])
                and self.isScramble(s1[i:], s2[i:])
            ) or (
                self.isScramble(s1[:i], s2[n - i :])
                and self.isScramble(s1[i:], s2[: n - i])
            ):
                return True
        # None of the splits match.
        return False


# TODO: Add the DP solution, looks really cool! PS: wait to forget it first :-)


def test():
    executors = [
        Memoization,
        Shorter,
    ]
    tests = [
        ["a", "a", True],
        ["great", "great", True],
        ["great", "rgeat", True],
        ["great", "eatgr", True],
        ["great", "tearg", True],
        ["great", "rtgra", False],
        ["abcde", "caebd", False],
        ["abcdefghijklmnopqrstuvwxyz", "wxyzstuvqrnopmhijklefgdcba", True],
        ["eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd", False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isScramble(t[0], t[1])
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
