# 1639. Number of Ways to Form a Target String Given a Dictionary
# 🔴 Hard
#
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
#
# Tags: Array - String - Dynamic Programming

import timeit
from collections import Counter, defaultdict
from functools import cache
from typing import List


# Precompute the frequencies of characters at a given index of words,
# then we can explore the recursion tree, at each index, we can choose
# to pick a character from the current column, which we can do in as
# many ways as instances of the character at target[i] there are, or
# skip this column.
#
# Time complexity: O(m*n + m*t) - We build a dictionary with character
# frequencies found at each index, to build it, we visit each character
# in the input array words in O(m*n), then we call the dfs function that
# can be called a maximum of m*t times where m is len(words[0]) and t
# is len(target).
# Space complexity: O(m*t) - The number of entries that we can store
# in the cache is m*t.
#
# Runtime 2344 ms Beats 54.48%
# Memory 242.6 MB Beats 28.79%
class Memoization:
    def numWays(self, words: List[str], target: str) -> int:
        # M is the word length, N is the number of words.
        m = len(words[0])
        # Create a dictionary of indexes to the characters that can be
        # found at that index. O(m*n)
        chars_at_index = [defaultdict(int) for _ in range(m)]
        # Iterate over all the words.
        for word in words:
            for i, c in enumerate(word):
                chars_at_index[i][c] += 1

        @cache
        def dfs(w_idx, t_idx) -> int:
            # Check if we have completed the word.
            if t_idx == len(target):
                return 1
            # Check if we have run out of indexes to pick from.
            if w_idx == m:
                return 0
            # We can use any of the characters at this w_idx or skip
            # the index.
            pick = chars_at_index[w_idx][target[t_idx]] * dfs(
                w_idx + 1, t_idx + 1
            )
            skip = dfs(w_idx + 1, t_idx)
            return (pick + skip) % 1_000_000_007

        return dfs(0, 0)


# Bottom-up DP version of the previous solution, the transition remains
# the same, pick a character from the current column in freq ways, or
# skip it.
#
# Time complexity: O(m*n + m*t) - We build an array with character
# frequencies found at each index, to build it, we visit each character
# in the input array words in O(m*n), then we have a nested m*t loop.
# Space complexity: O(m*t) - The size of the dp array.
#
# Runtime 3015 ms Beats 28.79%
# Memory 39 MB Beats 73.93%
class DP:
    def numWays(self, words: List[str], target: str) -> int:
        # M is the word length, N is the number of words, T the length
        # of target.
        m, t, mod = len(words[0]), len(target), 1_000_000_007
        # Create a dictionary of indexes to the characters that can be
        # found at that index. O(m*n)
        freq = [[0] * m for _ in range(26)]
        # Iterate over all the words.
        for word in words:
            for i, c in enumerate(word):
                freq[ord(c) - 97][i] += 1
        dp = [[0] * (m + 1) for _ in range(t + 1)]
        # One way to have 0 characters using 0 columns.
        dp[0][0] = 1
        for i in range(t + 1):
            for j in range(m):
                if i < t:
                    dp[i + 1][j + 1] += freq[ord(target[i]) - 97][j] * dp[i][j]
                    dp[i + 1][j + 1] %= mod
                dp[i][j + 1] += dp[i][j]
                dp[i][j + 1] %= mod
                # Doing the mod at each step impacts performance but
                # brings memory usage from 290 MB to 39 MB.
        return dp[-1][-1]


# Space optimized version of the previous solution, we only need to
# store the last column of results. We can also only store the
# character frequencies for the column that we are about to process.
#
# Time complexity: O(m*n + m*t) - We build an array with character
# frequencies found at each index, to build it, we visit each character
# in the input array words in O(m*n), then we have a nested m*t loop.
# Space complexity: O(t) - The size of the dp array. The freq counter
# has a max size of 26.
#
# Runtime 1493 ms Beats 78.21%
# Memory 20.4 MB Beats 94.16%
class DPO1:
    def numWays(self, words: List[str], target: str) -> int:
        m, t = len(words[0]), len(target)
        dp = [1] + [0] * t
        for i in range(m):
            # Compute the frequencies of characters at this index.
            freq = Counter(word[i] for word in words)
            for j in reversed(range(t)):
                dp[j + 1] = (
                    dp[j + 1] + dp[j] * freq[target[j]]
                ) % 1_000_000_007
        return dp[-1]


def test():
    executors = [
        Memoization,
        DP,
        DPO1,
    ]
    tests = [
        [["cbba", "baab"], "bcb", 0],
        [["abba", "baab"], "bcb", 0],
        [["abba", "baab"], "bab", 4],
        [["acca", "bbbb", "caca"], "aba", 6],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numWays(t[0], t[1])
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
