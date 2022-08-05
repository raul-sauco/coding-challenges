# 39. Combination Sum
# 🟠 Medium
#
# https://leetcode.com/problems/combination-sum/
#
# Tags: Array - Backtracking

import timeit
from typing import List


# A brute-force approach will start by picking all numbers and, for each
# iteration, it would combine them with all the numbers again until
# we either came to a solution or the current result became bigger than
# target. Since that would result in permutations of the same values, we
# need to find another approach.
# Instead we can start picking values off the candidates array and for
# each, choose to use it [0..target // value] times. Then pass that
# decision down the decision tree.
# When we get to a result, go over the target, or we exhaust the
# candidates, we stop exploring that branch.
#
# Time complexity: O(2^t) - For each iteration, we have m possible
# choices with m being the remaining target // the current value. To
# calculate the complexity, we can also see it as a decision tree where
# for each decision, we can either take or not the current value. Since
# the value could be 1, we could take it target number of times until it
# ends up adding up to target.
# Space complexity: O(2^t) - The call stack.
#
# Runtime: 100 ms, faster than 77.71%
# Memory Usage: 14.1 MB, less than 72.82%
class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        # Store the results in a list, initially we don't know the size.
        results = []
        # Define a function that explores the next value in candidates.
        def dp(current: List[int], idx: int, ct: int) -> None:
            # Pick the leftmost number, we can use it
            # [0, 1, 2, target // n] times, then calculate the rest of
            # the result based on calling dp without this number and
            # adjusting the target.
            for n in range(ct // candidates[idx] + 1):
                val = n * candidates[idx]
                # If adding this value n number of times to the current
                # result would result in the target, add this result to
                # the list of results.
                if val == ct:
                    results.append(current + ([candidates[idx]] * n))
                # If adding this value n number of times still falls
                # short of the current target, and we have more
                # candidates, keep searching.
                elif val < ct and idx < len(candidates) - 1:
                    dp(current + ([candidates[idx]] * n), idx + 1, ct - val)

        # Initial call.
        dp([], 0, target)
        return results


def test():
    executors = [Solution]
    tests = [
        [[2], 1, []],
        [[2], 2, [[2]]],
        [[2, 3, 6, 7], 7, [[2, 2, 3], [7]]],
        [[7, 3, 6, 2], 7, [[3, 2, 2], [7]]],
        [[2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1e3"))):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.combinationSum(t[0], t[1])
                result.sort()
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
