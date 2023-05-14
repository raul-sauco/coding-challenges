# 1799. Maximize Score After N Operations
# 🔴 Hard
#
# https://leetcode.com/problems/maximize-score-after-n-operations/
#
# Tags: Array - Math - Dynamic Programming - Backtracking - Bit Manipulation
# - Number Theory - Bitmask

import timeit
from functools import cache
from heapq import heapify, heappop
from math import gcd
from typing import List


# Memoized solution, try all combinations of pairs in each position, use
# a bitmask of the numbers that we have already used to avoid computing
# the result more than once when we start with the same state.
#
# Time complexity: O((2^n)*n^2) - Where n is the length of nums, we have
# 2^n bitmasks, for each bitmask, we check n^2 pairs of indexes to find
# the highest score that can be obtained.
# Space complexity: O(n*(2^n)) - The parameters of the function that we
# are memoizing.
#
# Runtime 1922 ms Beats 82.91%
# Memory 25.8 MB Beats 16.46%
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i, mask):
            if i > n // 2:
                return 0
            res = 0
            for j in range(n):
                if (1 << j) & mask:
                    continue
                for k in range(j + 1, n):
                    if (1 << k) & mask:
                        continue
                    res = max(
                        res,
                        i * gcd(nums[j], nums[k])
                        + dfs(i + 1, mask | ((1 << j) | (1 << k))),
                    )
            return res

        return dfs(1, 0)


# This solution is not correct because the logic only works when the
# maximum gcd that we pick is unique.
#
# TODO: It would be interesting merging this logic into the DP solution,
# for each call to the internal dfs function, first check if there
# there exists a unique pair that gives us the maximum GCD, if it does,
# pick that one, otherwise, check all possibilities.
# That could be extended to exploring only the pairs that give use the
# maximum GCD at each call level, instead of all possible pairs.
#
# Time complexity: O() -
# Space complexity: O() -
#
# Runtime  ms Beats %
# Memory  MB Beats %
class Solution2:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2
        # Construct a max heap with the gcd of all pairs of values.
        d = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                d.append((-gcd(nums[i], nums[j]), i, j))
        heapify(d)
        res = 0
        used = [False] * len(nums)
        idx = n
        while idx:
            g, i, j = heappop(d)
            if used[i] or used[j]:
                continue
            res -= idx * g
            used[i] = True
            used[j] = True
            idx -= 1
        return res


def test():
    executors = [
        Solution,
        # Solution2,
    ]
    tests = [
        [[1, 2], 1],
        [[3, 4, 6, 8], 11],
        [[1, 2, 3, 4, 5, 6], 14],
        [
            [
                109497,
                983516,
                698308,
                409009,
                310455,
                528595,
                524079,
                18036,
                341150,
                641864,
                913962,
                421869,
                943382,
                295019,
            ],
            527,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxScore(t[0])
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
