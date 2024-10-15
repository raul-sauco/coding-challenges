# 1964. Find the Longest Valid Obstacle Course at Each Position
# 🔴 Hard
#
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
#
# Tags: Array - Binary Search - Divide and Conquer - Binary Indexed Tree
# - Segment Tree - Merge Sort - Ordered Set

import timeit
from bisect import bisect_right
from typing import List


# Use dynamic programming, each subproblem can be seen as "the longest
# non-decreasing subsequence" but, if we use something similar to the
# LIS solution, it will run in O(n^2*log(n)), we can instead see that,
# for each index, we only need to find the longest sequence to the left
# where the last element is less than, or equal to the current element,
# because then we can append the current element. We could do this in
# O(n), resulting in O(n^2) overall time complexity, iterating over all
# the previous results but that can be optimized if we use an extra
# structure where we keep these previous results sorted and can binary
# search the insertion point.
#
# Time complexity: O(n*log(n)) - We iterate over all the elements, for
# each, we do a binary search over the previous results that could be up
# to n.
# Space complexity: O(n) - The dp array uses n extra memory.
#
# Runtime 1025 ms Beats 31%
# Memory 34.65 MB Beats 37%
class Solution:
    def longestObstacleCourseAtEachPosition(
        self, obstacles: List[int]
    ) -> List[int]:
        # dp[i] holds the smallest value that we have seen as the last
        # element of a sequence of length i. It is guaranteed to be
        # non-decreasing.
        res, dp = [], [float("inf")] * (len(obstacles) + 1)
        for o in obstacles:
            idx = bisect_right(dp, o)
            res.append(idx + 1)
            dp[idx] = o
        return res


def test():
    executors = [Solution]
    tests = [
        [[8], [1]],
        [[8, 1], [1, 1]],
        [[2, 2, 1], [1, 2, 1]],
        [[8, 1, 8], [1, 1, 2]],
        [[1, 2, 3, 2], [1, 2, 3, 3]],
        [[3, 1, 5, 6, 4, 2], [1, 1, 2, 3, 2, 2]],
        [[5, 1, 5, 5, 1, 3, 4, 5, 1, 4], [1, 1, 2, 3, 2, 3, 4, 5, 3, 5]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.longestObstacleCourseAtEachPosition(t[0])
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
