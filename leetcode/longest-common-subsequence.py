# https://leetcode.com/problems/longest-common-subsequence/

from bisect import bisect_left
from collections import defaultdict


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [0 for _ in range(len(text1) + 1)]  # Store all i-1 values
        for a in text2:
            prev = 0
            for i, b in enumerate(text1):
                current = memo[i+1]  # Store (i-1,j-1)
                # DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise
                if a == b:
                    memo[i+1] = prev + 1       # DP[i - 1][j - 1] + 1
                else:
                    # max(DP[i - 1][j], DP[i][j - 1])
                    memo[i+1] = max(memo[i+1], memo[i])
                prev = current

        return memo[-1]

    # Neat solution that was on the faster end of the submissions
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        d = defaultdict(list)
        for i, c in enumerate(text2):
            d[c].append(i)
        for c in text1:
            if c in d:
                for i in reversed(d[c]):
                    ins = bisect_left(dp, i)
                    if ins == len(dp):
                        dp.append(i)
                    else:
                        dp[ins] = i
        return len(dp)

        #   ''ABCDEAAAAA
        # ''0 00000
        # B 0 01111
        # A 0 11
        # A
        # C
        # E


def test():
    sol = Solution()
    tests = [
        ["abcde", "ace", 3],
        ["abc", "abc", 3],
        ["mbc", "abc", 2],
        ["abc", "def", 0],
        ["oxcpqrsvwf", "shmtulqrypy", 2],
        ["acccd", "bcc", 2],
        ["xxxxxxxxxxx", "xxxxxxxxxxx", 11],
        ["xxxxxxxxxxx", "yyyyyyyyyyx", 1],
        ["xxxxxxxxxxx", "y", 0],
        ["xxxxxxxxxxx", "", 0],
        ["", "aoeu", 0],
        ["abcba", "abcbcba", 5],
    ]
    for t in tests:
        result = sol.longestCommonSubsequence(t[0], t[1])
        assert t[2] == result, f'{result} != {t[2]}'


test()
