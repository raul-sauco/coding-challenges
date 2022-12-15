# 1143. Longest Common Subsequence
# 🟠 Medium
#
# https://leetcode.com/problems/longest-common-subsequence/
#
# Tags: String - Dynamic Programming

import timeit
from bisect import bisect_left
from collections import defaultdict

# 1e3 calls
# » DP                  0.11152   seconds
# » DPO1                0.08118   seconds
# » UseIndexes          0.03673   seconds

# Use dynamic programming, visit all the indexes of both strings, for
# each, the LCS equals the LCS of the previous indexes plus one if the
# characters match, or the best of removing one of the characters if
# the characters at the current indexes do not match.
#
# Time complexity: O(m*n) - Where m and n are the lengths of the input
# strings.
# Space complexity: O(m*n) - We use a matrix of m*n positions.
#
# Runtime: 418 ms, faster than 90.90%
# Memory Usage: 21.8 MB, less than 92.4%
class DP:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                # If the characters at this position match, we can use
                # the previous match to build a longer LCS.
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                # The characters don't match, the LCS is the best we
                # can build without the last character of each string.
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]


# Improve the dynamic programming solution's memory complexity by only
# storing the last row of data and choosing the shorter string to be
# the row.
#
# Time complexity: O(m*n) - Where m and n are the lengths of the input
# strings.
# Space complexity: O(min(m, n)) - Where use an array of the same
# length as the shorter input string.
#
# Runtime: 285 ms, faster than 99.79%
# Memory Usage: 13.8 MB, less than 98.85%
class DPO1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            return self.longestCommonSubsequence(text2, text1)
        N = len(text2)
        dp = [0] * (N + 1)
        for c in text1:
            row = [0] * (N + 1)
            for j in range(N):
                # Characters match, we can use them to extend the
                # previous LCS.
                if c == text2[j]:
                    row[j + 1] = dp[j] + 1
                # Characters don't match, the LCS for this indexes is
                # the best of the LCS before adding one of them.
                else:
                    row[j + 1] = max(row[j], dp[j + 1])
            dp = row
        return dp[-1]


# Neat solution that was on the faster end of the submissions, it
# creates a hashmap of chars to indexes at which they have been seen,
# then uses the hashmap to quickly determine if they can be used to
# build a longer sequence.
#
# Time complexity: O(m*n) - O(n) to build the dictionary, then we
# iterate over the m characters of text1 and, for each, may end up
# iterating over all the indexes on text2, if that was the only
# character found there. Even though the theoretical complexity is high,
# the actual runtime is very good because the input strings tend to
# have low frequencies of different characters instead of high
# frequencies of few characters.
# Space complexity: O(m+n) - The dictionary and the dp array.
#
# Runtime: 58 ms, faster than 100%
# Memory Usage: 13.8 MB, less than 98.85%
class UseIndexes:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # The size of the dp array is => O(LCS) max == O(min(m, n))
        dp = []
        # Create a dictionary of characters in text2 to the positions on
        # which they can be found.
        d = defaultdict(list)
        for i, c in enumerate(text2):
            d[c].append(i)
        # Iterate over the characters in text1 checking in which
        # position of the LCS they could be inserted.
        for c in text1:
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
        DP,
        DPO1,
        UseIndexes,
    ]
    tests = [
        ["", "aoeu", 0],
        ["abc", "abc", 3],
        ["mbc", "abc", 2],
        ["abc", "def", 0],
        ["acccd", "bcc", 2],
        ["abcde", "ace", 3],
        ["xxxxxxxxxxx", "", 0],
        ["abcba", "abcbcba", 5],
        ["xxxxxxxxxxx", "y", 0],
        ["oxcpqrsvwf", "shmtulqrypy", 2],
        ["xxxxxxxxxxx", "yyyyyyyyyyx", 1],
        ["xxxxxxxxxxx", "xxxxxxxxxxx", 11],
        ["xxxxxxxxxxx", "xyyxyyxyxxyxxyxyyyx", 9],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1000):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.longestCommonSubsequence(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
