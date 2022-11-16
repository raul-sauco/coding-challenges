# 115. Distinct Subsequences
# 🔴 Hard
#
# https://leetcode.com/problems/distinct-subsequences/
#
# Tags: String - Dynamic Programming

import timeit
from functools import cache

# The brute force solution simply chooses to use or skip each character
# in s until the string that is being built is of length t, then returns
# whether the string constructed is a match or not.
#
# Time complexity: O(2^n) - Where n is the length of s.
# Space complexity: O(n) - Where n is the length of s, the call stack
# can grow to height n.


# We can improve the previous solution caching intermediate results to
# avoid repeating the same calculations and by only moving forward when
# the characters under both indexes are a match, otherwise only move
# forward the s pointer trying to find a match for the character in t.
#
# Time complexity: O(m*n) - The potential number of combinations of the
# internal function parameters.
# Space complexity: O(m*n) - The number of call results that could be
# cached equals all the different parameters with which the function
# could be called.
#
# Runtime: 105 ms, faster than 97.19%
# Memory Usage: 19.6 MB, less than 76.97%
class Memoized:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dfs(si: int, ti: int) -> int:
            # Base case, the string already has the same length as t.
            if ti == len(t):
                return 1
            # If we don't have enough characters left, this branch fails.
            if len(s) - si < len(t) - ti:
                return 0
            # Otherwise explore the two branches if the character would
            # be a match.
            if t[ti] == s[si]:
                return dfs(si + 1, ti) + dfs(si + 1, ti + 1)
            # If the characters don't match update the pointer in s.
            return dfs(si + 1, ti)

        return dfs(0, 0)


# The dynamic programming solution stores the ways to build up to
# index j on t using the first i characters of s.
#
# Time complexity: O(m*n) - We iterate over each index of t, in reality
# over an average of half the indexes of t, but it does not change the
# overall time complexity, for each index of s.
# Space complexity: O(m*n) - We store a value for each combination of
# m and n.
#
# Runtime: 423 ms, faster than 89.23%
# Memory Usage: 70.3 MB, less than 68.42%
class DP:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        if M < N:
            return 0
        dp = [[1] + [0] * N for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, 1 + min(i, N)):
                # We know that we can build up to t[j] in, at least, as
                # many ways as we could build up to t[j-1]
                dp[i][j] = dp[i - 1][j]
                # If the characters under the indexes match, we can add
                # the number of ways we could build up to t[j-1] using
                # s[i-1] characters.
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]


# The space optimized version of the previous solution, we only store
# the previous row of dp instead of the entire 2D matrix.
#
# Time complexity: O(m*n) - We iterate over each index of t, in reality
# over an average of half the indexes of t, but it does not change the
# overall time complexity, for each index of s.
# Space complexity: O(n) - We store a value for each n in two arrays.
#
# Runtime: 271 ms, faster than 92.11%
# Memory Usage: 14.1 MB, less than 95.31%
class DPOn:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        if M < N:
            return 0
        dp = [1] + [0] * (N)
        for i in range(1, M + 1):
            current = [1] + [0] * (N)
            for j in range(1, min(i + 1, N + 1)):
                current[j] = dp[j]
                if s[i - 1] == t[j - 1]:
                    current[j] += dp[j - 1]
            dp = current
        return dp[-1]


def test():
    executors = [
        Memoized,
        DP,
        DPOn,
    ]
    tests = [
        ["rabbbit", "rabbit", 3],
        ["babgbag", "bag", 5],
        [
            "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbba"
            + "eabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe",
            "bddabdcae",
            10582116,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numDistinct(t[0], t[1])
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
