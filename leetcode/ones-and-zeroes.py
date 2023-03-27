# 474. Ones and Zeroes
# 🟠 Medium
#
# https://leetcode.com/problems/ones-and-zeroes/
#
# Tags: Array - String - Dynamic Programming

import timeit
from typing import List


# We can use dynamic programming, this problem is similar to the classic
# coin change problem, we can keep a dp object where the entries
# dp(i,j)= x represent the maximum number of substrings that we can use
# while keeping a maximum of i zeroes and j ones. For each substring in
# the input array of substrings, we iterate over all the keys, a maximum
# of 1e4, checking if we could add the number of zeroes and ones to the
# current dictionary entry without going over the limits m and n.
#
# Time complexity: O(m*n*s) - Where s is the length of strs. We iterate
# over all strings s and, for each, we iterate all the existing keys in
# the dp dictionary. m and n are limited to 100, we could simplify to
# O(s*1e4) ≈ O(s) but, in the context of the problem is a big enough
# that I think it is more accurate to not simplify. We could go even
# further and, since len(strs) <= 600, and that is also a small value,
# O(100*100*600) ≈ O(1)
# Space complexity: O(m*n) - The dp dictionary.
#
# Runtime 1856 ms Beats 95.59%
# Memory 14.1 MB Beats 81.5%
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # A dictionary where each entry keyed by (i, j) represents the
        # maximum subarray length using i zeroes and j ones.
        dp = {(0, 0): 0}
        res = 0
        # Iterate over the strings.
        for s in strs:
            # Compute the number of ones and zeroes.
            ones, zeroes = 0, 0
            for c in s:
                if c == "0":
                    zeroes += 1
                else:
                    ones += 1
            # Try to add this values to each previous dp entry iterating
            # in reverse over the existing keys.
            for i, j in list(sorted(dp.keys(), reverse=True)):
                z, o = zeroes + i, ones + j
                # If adding this substring adds in going over, skip.
                if z > m or o > n:
                    continue
                key = (z, o)
                if key in dp:
                    dp[key] = max(dp[key], dp[(i, j)] + 1)
                else:
                    dp[key] = dp[(i, j)] + 1
                res = max(res, dp[key])
        return res


def test():
    executors = [Solution]
    tests = [
        [["10", "0", "1"], 1, 1, 2],
        [["10", "0001", "111001", "1", "0"], 4, 3, 3],
        [["10", "0001", "111001", "1", "0"], 5, 3, 4],
        [["10", "0001", "111001", "1", "0"], 50, 50, 5],
        [
            [
                "0",
                "1101",
                "01",
                "00111",
                "1",
                "10010",
                "0",
                "0",
                "00",
                "1",
                "11",
                "0011",
            ],
            63,
            36,
            12,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findMaxForm(t[0], t[1], t[2])
                exp = t[3]
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
