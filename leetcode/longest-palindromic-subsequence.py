# 516. Longest Palindromic Subsequence
# 🟠 Medium
#
# https://leetcode.com/problems/longest-palindromic-subsequence/
#
# Tags: String - Dynamic Programming

import timeit
from bisect import bisect_left
from collections import defaultdict
from functools import cache


# Use a 2D array to store the LPS between two indexes l and r that we
# have already computed, the base case is when l == r => 1 and l > r =>
# 0. For each pair l, r, we check base cases, then check the cache,
# otherwise compute the LPS, to do it, we check if the characters at l
# and r match, if they do, the result will be equal to the LPS at l+1,
# r-1 plus 2, if they don't match, the result will be the max LPS
# between not using the left or the right character.
#
# Time complexity: O(n^2) - We compute half of all possible values of
# (l, r) and the computations take amortized constant time.
# Space complexity: O(n^2) - The dp array can hold one key for each
# combination of (l, r).
#
# Runtime 836 ms Beats 97.34%
# Memory 71 MB Beats 25.78%
class Use2DArray:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def solve(l, r) -> int:
            if l == r:
                return 1
            if l > r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            # Are the characters a match?
            if s[l] == s[r]:
                dp[l][r] = 2 + solve(l + 1, r - 1)
            else:
                dp[l][r] = max(solve(l, r - 1), solve(l + 1, r))
            return dp[l][r]

        return solve(0, n - 1)


# Use a dictionary to store the LPS between two indexes l and r that we
# have already computed, the base case is when l == r => 1 and l > r =>
# 0. For each pair l, r, we check base cases, then check the cache,
# otherwise compute the LPS, to do it, we check if the characters at l
# and r match, if they do, the result will be equal to the LPS at l+1,
# r-1 plus 2, if they don't match, the result will be the max LPS
# between not using the left or the right character.
#
# Time complexity: O(n^2) - We compute half of all possible values of
# (l, r) and the computations take amortized constant time.
# Space complexity: O(n^2) - The dp dictionary can hold one key for each
# combination of (l, r).
#
# Runtime 1308 ms Beats 76.8%
# Memory 236.1 MB Beats 20.17%
class UseDict:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = {}

        def solve(l, r) -> int:
            if l == r:
                return 1
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            # Are the characters a match?
            if s[l] == s[r]:
                dp[(l, r)] = 2 + solve(l + 1, r - 1)
            else:
                dp[(l, r)] = max(solve(l, r - 1), solve(l + 1, r))
            return dp[(l, r)]

        return solve(0, n - 1)


# Similar to the previous solution but use the built-in @cache.
#
# Time complexity: O(n^2) - We compute half of all possible values of
# (l, r) and the computations take amortized constant time.
# Space complexity: O(n^2) - The dp array can hold one key for each
# combination of (l, r).
#
# Runtime 921 ms Beats 96%
# Memory 237.4 MB Beats 16.75%
class UseCache:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def solve(l, r) -> int:
            if l == r:
                return 1
            if l > r:
                return 0
            # Are the characters a match?
            if s[l] == s[r]:
                return 2 + solve(l + 1, r - 1)
            return max(solve(l, r - 1), solve(l + 1, r))

        return solve(0, len(s) - 1)


# Iterative bottom-up version, use an array and compute the values
# starting with the smaller substrings, use previous results to
# compute bigger gaps of (l, r).
#
# Time complexity: O(n^2) - We compute half of all possible values of
# (l, r) and the computations take amortized constant time.
# Space complexity: O(n) - We use 2 arrays of size n.
#
# Runtime 1029 ms Beats 86.51%
# Memory 13.9 MB Beats 97.69%
class DP:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp, tmp = [[0] * n for _ in range(2)]

        for i in reversed(range(n)):
            tmp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    tmp[j] = dp[j - 1] + 2
                else:
                    tmp[j] = max(dp[j], tmp[j - 1])
            dp = tmp[:]

        return dp[-1]


# Iterative bottom-up version, use an array and compute the values
# starting with the smaller substrings, use previous results to
# compute bigger gaps of (l, r).
#
# Time complexity: O(n^2) - We compute half of all possible values of
# (l, r) and the computations take amortized constant time.
# Space complexity: O(n) - We use 2 arrays of size n.
#
# Runtime 1029 ms Beats 86.51%
# Memory 13.9 MB Beats 97.69%
class DP:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp, tmp = [[0] * n for _ in range(2)]

        for i in reversed(range(n)):
            tmp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    tmp[j] = dp[j - 1] + 2
                else:
                    tmp[j] = max(dp[j], tmp[j - 1])
            dp = tmp[:]

        return dp[-1]


# Use the algorithm to compute the longest common subsequence between
# two strings and use it with the input and its reversed version as
# the parameters.
#
# Time complexity: O(n^2) - We iterate over all characters in s, for
# each, we may iterate over all characters of the reversed s.
# Space complexity: O(n) - The dictionary
#
# Runtime 1976 ms Beats 42.18%
# Memory 14 MB Beats 93.52%
class LCS:
    def longestPalindromeSubseq(self, s: str) -> int:
        # The size of the dp array is => O(LCS) max == O(min(m, n))
        dp = []
        # Create a dictionary of characters in text2 to the positions on
        # which they can be found.
        d = defaultdict(list)
        for i, c in enumerate(s[::-1]):
            d[c].append(i)
        # Iterate over the characters in text1 checking in which
        # position of the LCS they could be inserted.
        for c in s:
            if c in d:
                for i in reversed(d[c]):
                    # Find the position at which we could use this index
                    # in the dp array.
                    ins = bisect_left(dp, i)
                    # We could append this character to the current LCS.
                    if ins == len(dp):
                        dp.append(i)
                    # This character could be inserted before the
                    # current character at this position of the LCS,
                    # which makes it more likely to be able to append
                    # later.
                    else:
                        dp[ins] = i
        return len(dp)


def test():
    executors = [
        Use2DArray,
        UseDict,
        UseCache,
        DP,
        LCS,
    ]
    tests = [
        ["cbbd", 2],
        ["bbbab", 4],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.longestPalindromeSubseq(t[0])
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
