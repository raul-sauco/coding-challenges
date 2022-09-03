# 1. Two Sum
# 🟢 Easy
#
# https://leetcode.com/problems/two-sum/
#
# Tags: Array - Hash Table

import timeit
from typing import List

# 100 calls with n <= 1000
# » Naive               2.27413   seconds
# » HashMapSolution     0.00751   seconds

# Create a hashmap that stores numbers that we have seen already as keys
# and their indices as values, then iterate over the numbers in the
# input, for each number, check if the set contains a number that we can
# add to this one to add up to the target, if found, return their indices,
# the description guarantees that each test case will have at most one
# solution.
#
# Time complexity; O(n) - We visit each element of the input once, for
# each, we check if another element is in the set at O(1) cost.
# Space complexity: O(n) - The set can grow to size n.
#
# Runtime: 104 ms, faster than 52.66%
# Memory Usage: 15.1 MB, less than 49.66%
class HashMapSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store values seen in a hashmap to access in O(1).
        seen = {}
        # Iterate over the input.
        for idx in range(len(nums)):
            # We are looking for a value that we can add to nums[i] to
            # sum up to target.
            match = target - nums[idx]
            # If we have seen that value already.
            if match in seen:
                # Return the indices of the two numbers.
                return [seen[match], idx]
            # If this wasn't a match, add the value => index pair to the
            # seen dictionary.
            seen[nums[idx]] = idx
        # Not strictly necessary because having one answer is guaranteed.
        return -1


# The naive solution iterates over the input array and for each item, it
# checks the result of adding it to all values to its right.
#
# Time complexity: O(n^2) - For each value, we visit all the remaining
# values.
# Space complexity: O(1) - Constant space.
#
# Runtime: 4718 ms, faster than 22.90%
# Memory Usage: 14.7 MB, less than 99.57%
class Naive:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate over all the input O(n).
        for i in range(len(nums)):
            # The nested loop also iterates over the entire input
            # O(n-1)..O(n-2)..O(n-3) => O(n)
            for j in range(i + 1, len(nums)):
                # Compare the sum of each two pairs with the target.
                if nums[i] + nums[j] == target:
                    # If the sum matches, return the indices.
                    return [i, j]
        # Not strictly necessary because having one answer is guaranteed.
        return -1


def test():
    executors = [
        Naive,
        HashMapSolution,
    ]
    tests = [
        [[2, 7, 11, 15], 9, [0, 1]],
        [[3, 2, 4], 6, [1, 2]],
        [[3, 3], 6, [0, 1]],
        [[x for x in range(1000)], 1997, [998, 999]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.twoSum(t[0], t[1])
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
