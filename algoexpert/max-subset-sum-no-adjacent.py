# Max Subset Sum No Adjacent
# 🟠 Medium
#
# https://www.algoexpert.io/questions/max-subset-sum-no-adjacent
#
# Tags: Dynamic Programming

import timeit


# The max sum at each point will be the max between the previous max and
# the one before that plus the current value.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(n) - The dp array has the same size as the input.
class Solution:
    def maxSubsetSumNoAdjacent(self, array):
        # Base case, empty input.
        if not array:
            return 0
        # Base case, less than three values.
        if len(array) < 3:
            return max(array)
        dp = [0] * len(array)
        dp[0], dp[1] = array[0], max(array[0], array[1])
        for i in range(2, len(array)):
            dp[i] = max(dp[i - 2] + array[i], dp[i - 1])
        return dp[-1]


# Improve the previous solution by only storing two values instead of
# an array the same size as the input.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - We use constant extra space.
class SolutionO1:
    def maxSubsetSumNoAdjacent(self, array):
        # Base case, empty input.
        if not array:
            return 0
        # Base case, less than three values.
        if len(array) < 3:
            return max(array)
        # Substitute the dp array with the two previous values.
        a, b = array[0], max(array[0], array[1])
        for i in range(2, len(array)):
            a, b = b, max(a + array[i], b)
        return b


def test():
    executors = [
        Solution,
        SolutionO1,
    ]
    tests = [
        [[], 0],
        [[15], 15],
        [[4, 3, 5, 200, 5, 3], 207],
        [[75, 105, 120, 75, 90, 135], 330],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxSubsetSumNoAdjacent(t[0])
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
