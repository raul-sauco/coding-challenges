# https://leetcode.com/problems/interleaving-string/

import timeit
from functools import lru_cache
from typing import List


# Explore each possible branch using a dictionary to store suffixes that have been already computed.
#
# Runtime: 92 ms, faster than 18.94% of Python3 online submissions for Interleaving String.
# Memory Usage: 16.4 MB, less than 5.51% of Python3 online submissions for Interleaving String.
class DictMemoized:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # Base cases
        if s1 == "" and s2 == "" and s3 == "":
            return True
        if len(s1) + len(s2) != len(s3):
            return False

        # The key for this combination of inputs
        key = s1 + "#" + s2 + "#" + s3

        # Memo section
        if not hasattr(self, "memo"):
            self.memo = {}
        elif key in self.memo:
            return self.memo[key]

        # Recursive call
        if s1 != "" and s1[0] == s3[0]:
            if self.isInterleave(s1[1:], s2, s3[1:]):
                self.memo[key] = True
                return True
            else:
                self.memo[key] = False
        if s2 != "" and s2[0] == s3[0]:
            if self.isInterleave(s1, s2[1:], s3[1:]):
                self.memo[key] = True
                return True
            else:
                self.memo[key] = False
        # If neither of the current first characters match the first character of the interleave, we cannot construct it
        self.memo[key] = False
        return False


# Same as above, but use lru_cache and a nested recursive function
class CacheMemoized:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            choose_s1, choose_s2 = False, False
            if i < len(s1) and s1[i] == s3[i + j]:
                choose_s1 = dfs(i + 1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                choose_s2 = dfs(i, j + 1)

            return choose_s1 or choose_s2

        return dfs(0, 0)


# Use tabulation.
#
# Runtime: 122 ms, faster than 5.93% of Python3 online submissions for Interleaving String.
# Memory Usage: 14.1 MB, less than 73.34% of Python3 online submissions for Interleaving String.
class Tabulation2D:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # Base conditions
        if len(s1) + len(s2) != len(s3):
            return False

        # Initialize matrix
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True  # Three empty strings

        # Compute the result
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]


# Optimize tabulation storing only one row instead of matrix
class Tabulation1D:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if n > m:
            m, n = n, m
            s1, s2 = s2, s1
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                choose_s1, choose_s2 = False, False
                if s1[i - 1] == s3[i + j - 1]:
                    choose_s1 = dp[j]
                if s2[j - 1] == s3[i + j - 1]:
                    choose_s2 = dp[j - 1]
                dp[j] = choose_s1 or choose_s2

        return dp[-1]


def test():
    executors = [Tabulation1D, Tabulation2D, DictMemoized, CacheMemoized]
    tests = [
        ["aabcc", "dbbca", "aadbbcbcac", True],
        ["aabcc", "dbbca", "aadbbbaccc", False],
        ["", "", "", True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for t in tests:
                sol = executor()
                result = sol.isInterleave(t[0], t[1], t[2])
                expected = t[3]
                assert result == expected, f"{result} != {expected}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds"))


test()
