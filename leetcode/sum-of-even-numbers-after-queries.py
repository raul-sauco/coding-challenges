# 985. Sum of Even Numbers After Queries
# 🟠 Medium
#
# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
#
# Tags: Array - Simulation

import timeit
from typing import List


# The brute force solution would perform the operations and calculate
# the sum of evens at each step, without trying to save any of the
# computed values to avoid recalculating them.
#
# Time complexity: O(n*q) - We iterate over all the queries q and, for
# each, iterate over the entire nums array of n values.
# Space complexity: O(n) - If we don't consider the input or output
# arrays and avoid using a temporary array, instead mutating the input,
# we can improve it to O(1).
#
# This solution would fail with Time Limit Exceeded.
class BruteForce:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        # The result array will have the same size as the queries.
        res = [0] * len(queries)
        # Make a copy of the input to avoid mutating it.
        temp = nums.copy()
        # Iterate over the queries computing the sum of even numbers
        # after the operation is done. O(n)
        for i in range(len(queries)):
            # Extract the value and the affected index from the query.
            val, idx = queries[i]
            # Execute the operation.
            temp[idx] += val
            # Compute the sum of evens. O(n)
            res[i] = sum([x for x in temp if x % 2 == 0])
        return res


# Use dynamic programming to store intermediate results. Iterate over
# the queries and, for each query, perform O(1) operations.
#
# Time complexity: O(n+q) - We iterate once over the input array nums to
# calculate the sum of evens in O(n), then we iterate over the queries
# array in O(q) and, for each query, perform O(1) operations.
# Space complexity: O(1) - If we don't consider the input or output
# arrays, notice that we need to mutate the input array to obtain that
# complexity, if we wanted to avoid doing so, we would need to make a
# copy, like in the previous solution, and the complexity would be O(n).
#
# Runtime: 539 ms, faster than 91.58%
# Memory Usage: 20.4 MB, less than 75.51%
class DP:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        # The result array will have the same size as the queries.
        res = [0] * len(queries)
        # Iterate over the queries computing the sum of even numbers
        # after the operation is done. O(n) Use enumerate to extract the
        # value and the affected index from the query. This is
        # equivalent to using only the index to iterate and then having:
        # val, idx = queries[i]
        for i, (val, idx) in enumerate(queries):
            # If this is the first operation compute the sum of evens.
            if i == 0:
                # Execute the operation.
                nums[idx] += val
                # Compute the sum of evens. O(n)
                res[i] = sum([x for x in nums if x % 2 == 0])
                continue
            # If this is not the first operation, use the previously
            # computed results to speed up calculation.
            res[i] = res[i - 1]
            # If the previous value was an even number, we are loosing
            # its value.
            if nums[idx] % 2 == 0:
                res[i] -= nums[idx]
            # Execute the operation.
            nums[idx] += val
            # If the new value is even, we are gaining its value.
            if nums[idx] % 2 == 0:
                res[i] += nums[idx]
        return res


def test():
    executors = [
        BruteForce,
        DP,
    ]
    tests = [
        [[1], [[4, 0]], [0]],
        [[1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]], [8, 6, 2, 4]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1000):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.sumEvenAfterQueries([*t[0]], t[1])
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
