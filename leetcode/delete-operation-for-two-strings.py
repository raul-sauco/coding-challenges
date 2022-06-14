# https://leetcode.com/problems/delete-operation-for-two-strings/
from bisect import bisect_left
from collections import defaultdict


class Solution:
    # Fast but hard to understand
    def minDistance(self, word1: str, word2: str) -> int:
        # We can use the same logic as 1143. Longest Common Subsequence ./longest-common-subsequence.py
        dp = []
        d = defaultdict(list)
        for i, c in enumerate(word2):
            d[c].append(i)
        for c in word1:
            if c in d:
                for i in reversed(d[c]):
                    ins = bisect_left(dp, i)
                    if ins == len(dp):
                        dp.append(i)
                    else:
                        dp[ins] = i
        # We need to remove all the characters that are not common
        return len(word1) + len(word2) - 2 * len(dp)

    # Easy to understand version found here
    # https://leetcode.com/problems/delete-operation-for-two-strings/discuss/1195726/C%2B%2BPythonJava-Short-and-Easy-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP
    def minDistanceEasyRead(self, w1: str, w2: str) -> int:
        dp = [[1000]*(len(w2)+1) for i in range(len(w1)+1)]
        for i in range(len(w1) + 1):
            for j in range(len(w2) + 1):
                dp[i][j] = i + j if i == 0 or j == 0 else dp[i - 1][j - 1] if w1[i -
                                                                                 1] == w2[j - 1] else 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


def test():
    tests = [
        ['sea', 'eat', 2],
        ['leetcode', 'etco', 4],
        ['xyz', 'abcde', 8],
        ['', '', 0],
    ]
    sol = Solution()
    for t in tests:
        result = sol.minDistance(t[0], t[1])
        assert result == t[2], f'{result} != {t[2]}'


test()
