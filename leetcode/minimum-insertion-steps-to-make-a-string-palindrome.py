# 1312. Minimum Insertion Steps to Make a String Palindrome
# 🔴 Hard
#
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
#
# Tags: String - Dynamic Programming

import timeit
from bisect import bisect_left


# Compute the longest palindromic subsequence in the input string, the
# result is the length of the string minus the LPS because these are
# characters that we can use as they are.
#
# Time complexity: O(n^2) - O(n) to build the dictionary, then we
# iterate over the n characters of s, for each, we may end up iterating
# over all the indexes on s.
# Space complexity: O(n) - The dictionary and the dp array.
#
# Runtime 89 ms Beats 100%
# Memory 13.8 MB Beats 99.80%
class Solution:
    # Copied from `./longest-common-subsequence.py`
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp, a = [], ord("a")
        d = [[] for _ in range(26)]
        for i, c in enumerate(text2):
            d[ord(c) - a].append(i)
        for c in text1:
            idx = ord(c) - a
            if d[idx]:
                for i in reversed(d[idx]):
                    ins = bisect_left(dp, i)
                    if ins == len(dp):
                        dp.append(i)
                    else:
                        dp[ins] = i
        return len(dp)

    def minInsertions(self, s: str) -> int:
        return len(s) - self.longestCommonSubsequence(s, s[::-1])


def test():
    executors = [Solution]
    tests = [
        ["zzazz", 0],
        ["mbadm", 2],
        ["leetcode", 5],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minInsertions(t[0])
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
