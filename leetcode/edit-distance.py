# 72. Edit Distance
# 🔴 Hard
#
# https://leetcode.com/problems/edit-distance/
#
# Tags: Array - Dynamic Programming

import timeit


# We can compute the edit distance of each substring of w1 from 0 to j
# and each substring of w2 from 0 to i based on whether the characters
# at w1[j] and w2[i] match. If they match, the edit distance will be the
# same as for the substrings w1[j-1], w2[i-1] because we won't need to
# edit the new character, if they don't match, the edit distance will be
# the best between [w1[j-1], w2[i-1]], [w1[j], w2[i-1]] and [w1[j-1],
# w2[i]] because we know that we can edit any of them to become w1[0..j],
# w2[0..i] with one edit, either remove, add or replace.
#
# Time complexity: O(m*n) - We compute dp for each combination of
# possible prefixes of the two input strings.
# Space complexity: O(m) - The dp array has the length of word1 + 1.
#
# Runtime 116 ms Beats 86.95%
# Memory 13.9 MB Beats 94.10%
class DP:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [i for i in range(m + 1)]
        for i in range(n):
            temp = [i + 1] + [0] * (m)
            for j in range(m):
                temp[j + 1] = (
                    dp[j]
                    if word1[j] == word2[i]
                    else min(temp[j], dp[j + 1], dp[j]) + 1
                )
            dp = temp
        return dp[-1]


# Similar to the previous version but uses an m*n matrix to store
# intermediate results.
#
# Runtime 151 ms Beats 77.81%
# Memory 17.6 MB Beats 55.49%
class DPMxN:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize a dp matrix of size m*n.
        m, n = len(word1), len(word2)
        dp = [[""] * (m + 1) for _ in range(n + 1)]
        dp[0] = [i for i in range(m + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for i in range(n):
            for j in range(m):
                if word1[j] == word2[i]:
                    #  min(dp[i + 1][j], dp[i][j + 1], dp[i][j])
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = (
                        min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
                    )
        return dp[-1][-1]


def test():
    executors = [
        DP,
        DPMxN,
    ]
    tests = [
        ["", "", 0],
        ["a", "a", 0],
        ["a", "b", 1],
        ["horse", "ros", 3],
        ["aaaaa", "abaa", 2],
        ["intention", "execution", 5],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minDistance(t[0], t[1])
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
