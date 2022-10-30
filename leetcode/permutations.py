# 46. Permutations
# 🟠 Medium
#
# https://leetcode.com/problems/permutations/
#
# Tags: Array - Backtracking

import itertools
import timeit
from typing import List


# Use an array of digits to store the current permutation that we are
# building and an array of the same length as the input to mark which
# digits have been used already. Define a backtrack function that adds
# one more digit, out of the available ones to the sequence and calls
# itself. After the call we backtrack to leave the state ready for the
# next call.
#
# Time complexity: O(n!) - Where n is the number of digits in the input.
# Space complexity: O(n) - If we don't take into account the result
# array and only consider the sequences as we build them, the array of
# flags for the elements already used and the depth of the call stack.
# If we want to consider the size of the output array, then O(n!).
#
# Runtime: 65 ms, faster than 72.39%
# Memory Usage: 14.2 MB, less than 23.67%
class BackTrack:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Mark indexes that have been used.
        used = [False] * len(nums)
        # The digits of the current permutation.
        digits = []

        def bt() -> None:
            # Base case, we have a full permutation.
            if len(digits) == len(nums):
                res.append(list(digits))
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    digits.append(nums[i])
                    bt()
                    digits.pop()
                    used[i] = False

        bt()
        return res


# The itertools module provides a method that does exactly what the
# problem asks, we can use it directly.
#
# Runtime: 63 ms, faster than 72.39%
# Memory Usage: 13.9 MB, less than 84.81%
class Itertools:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))
        # On LeetCode it passes as
        # return list(itertools.permutations(nums))


def test():
    executors = [
        BackTrack,
        Itertools,
    ]
    tests = [
        # [[1], [[1]]],
        # [[0, 1], [[0, 1], [1, 0]]],
        [
            [1, 2, 3],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.permute(t[0])
                result.sort()
                exp = t[1]
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
