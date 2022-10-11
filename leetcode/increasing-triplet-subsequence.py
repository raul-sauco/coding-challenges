# 334. Increasing Triplet Subsequence
# 🟠 Medium
#
# https://leetcode.com/problems/increasing-triplet-subsequence/
#
# Tags: Array - Greedy

import timeit
from typing import List


# Iterate over the input keeping track of the lowest single digit and
# the lowest subsequence of two digits seen, if we see a value greater
# than the second digit in the sequence, we can return true. If we see
# a value lesser than the best single digit, we can update it, if we
# see a value greater than it but smaller than the second digit in the
# best sequence of two, we can use it, and the smallest digit, to update
# the best sequence.
#
# Time complexity: O(n) - We visit each number in the input once and
# perform O(1) operations.
# Space complexity: O(1) - We keep two values in memory, an int and a
# tuple of two ints. Constant space.
#
# Runtime: 881 ms, faster than 66.1%
# Memory Usage: 24.6 MB, less than 80.42%
class Greedy:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Keep the lowest number seen.
        one = float("inf")
        # Keep the best sequence of 2 seen.
        twos = [float("inf"), float("inf")]
        for num in nums:
            # If the number is bigger than our biggest sequence of 2,
            # we found a match.
            if num > twos[1]:
                return True
            if num <= one:
                one = num
                # If we still have not found a sequence, may as well
                # take the smaller value.
                if twos[1] == float("inf"):
                    twos[0] = one
            elif num < twos[1]:
                twos[1] = num
                # If we are going to update 2, may update 1 as well
                if twos[0] > one:
                    twos[0] = one
        return False


def test():
    executors = [Greedy]
    tests = [
        [[20, 100, 10, 12, 5, 13], True],
        [[1, 2, 3], True],
        [[1, 2, 3, 4, 5], True],
        [[5, 4, 3, 2, 1], False],
        [[2, 1, 5, 0, 4, 6], True],
        [[2, 1, 5, 4, 0, 6], True],
        [[-4, 4, 6], True],
        [[-4, 4, -6], False],
        [[-4, -4, 6], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.increasingTriplet(t[0])
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
