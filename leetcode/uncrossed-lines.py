# 1035. Uncrossed Lines
# 🟠 Medium
#
# https://leetcode.com/problems/uncrossed-lines/
#
# Tags: Array - Dynamic Programming

import timeit
from bisect import bisect_left
from collections import defaultdict
from functools import cache
from typing import List


# Top down dynamic programming solution, visit all elements in nums1,
# for each, find the furthest left element in nums2 that we could match
# it with and call the function recursively with two options, using and
# skipping that possible line. Return the max result between each of the
# options.
#
# Time complexity: O(m*n^2) - It looks like this solution could be
# O(2^n) because, at each step, we make a binary decision, and we have n
# steps, but the fact that we use dynamic programming to store computed
# result takes the complexity down to the number of possible call
# parameters.
# Space complexity: O(m*n^2) - The cache can hold a maximum of of one
# entry for each option of different call parameters.
#
# Runtime 1746 ms Beats 5.25%
# Memory 225.9 MB Beats 5.25%
class Memoized:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        d = defaultdict(list)
        for i, num in enumerate(nums2):
            d[num].append(i)

        # idx: the index of the element in nums1 that we are trying to
        # match. l: the index of the first element in nums2 that we are
        # allowed to use without crossing lines. lines: the number of
        # lines that we have drawn to the left.
        @cache
        def dfs(idx: int, l: int, lines: int) -> int:
            # Base case, we are out of idxs in nums1
            if idx == len(nums1):
                return lines
            skip = dfs(idx + 1, l, lines)
            # Find the leftmost index of nums1[idx] in nums2 that is
            # to the right of l.
            ins_idx = bisect_left(d[nums1[idx]], l)
            if ins_idx < len(d[nums1[idx]]):
                # We could link nums1[idx] with this index.
                i = d[nums1[idx]][ins_idx]
                use = dfs(idx + 1, i + 1, lines + 1)
                return max(skip, use)
            return skip

        return dfs(0, 0, 0)


# Bottom up dynamic programming solution, iterate over all combinations
# of indexes in both input arrays, the max cross lines for each two
# indices i,j we will always be able to have the same number of lines
# that we did before we added either of the characters at the end of
# the arrays, if the characters at the given indices match, we will also
# be able to have as many lines as we did having one less character less
# in each, plus one between the current two values.
#
# Time complexity: O(m*n) - We have two nested loops, the outer one
# iterates over m and the inner one over n elements.
# Space complexity: O(m*n) - We are using a m*n sized dp matrix.
#
# Runtime 192 ms Beats 67.19%
# Memory 16.7 MB Beats 33.86%
class DP:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                    + (1 if nums1[i - 1] == nums2[j - 1] else 0),
                )
        return dp[-1][-1]


# Space optimized DP solution, similar to the previous one but, since we
# at most access the previous row of n, we use an m-sized dp array
# instead of a m*n sized matrix.
#
# Time complexity: O(m*n) - We have two nested loops, the outer one
# iterates over m and the inner one over n elements.
# Space complexity: O(min(m,n)) - We are using a n-sized array with n
# the minimum between len(nums1) and len(nums2).
#
# Runtime 180 ms Beats 85.83%
# Memory 16.4 MB Beats 38.6%
class DPO1:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2) > len(nums1):
            return self.maxUncrossedLines(nums2, nums1)
        n = len(nums2)
        dp, tmp = [[0] * (n + 1) for _ in range(2)]
        for c in nums1:
            for j in range(1, n + 1):
                tmp[j] = max(
                    dp[j],
                    tmp[j - 1],
                    dp[j - 1] + (1 if nums2[j - 1] == c else 0),
                )
            dp = tmp[::]
        return dp[-1]


def test():
    executors = [
        Memoized,
        DP,
        DPO1,
    ]
    tests = [
        [[3, 2], [2, 2, 2, 3], 1],
        [[1, 2, 3], [4, 5, 6], 0],
        [[1, 4, 2], [1, 2, 4], 2],
        [[1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1], 2],
        [[2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxUncrossedLines(t[0], t[1])
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
