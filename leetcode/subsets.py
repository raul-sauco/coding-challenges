# 78. Subsets
# 🟠 Medium
#
# https://leetcode.com/problems/subsets/
#
# Tags: Array - Backtracking - Bit Manipulation

import timeit
from typing import List


# Iterate over all elements of the input, for each element, generate all
# subsets that contain it and the ones that don't.
#
# Time complexity: O(n * 2^n) - For each element, we have two options,
# take it or not, when we take it, we copy the result set in O(n) to
# pass it to one of the branches.
# Space complexity: O(2^n) - The result list will have 2^n elements.
#
# Runtime: 43 ms, faster than 76.59%
# Memory Usage: 14.2 MB, less than 35.80%
class Recursive:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Define an array to hold the results.
        res = []
        # Define a recursive function that explores a given branch of
        # the recursion.
        def bt(idx: int, res: List[int]) -> List[List[int]]:
            # For each index, return the result of picking and not
            # picking this element.
            # Check for the base case when this is the last element.
            if idx == len(nums) - 1:
                return [res, res + [nums[idx]]]
            # If we are not at the last index, keep exploring.
            return bt(idx + 1, res) + bt(idx + 1, res + [nums[idx]])

        # Initial call
        return bt(0, [])


# We can implement the same solution without recursion by iterating
# over the list and copying all the existing subsets adding the current
# item that we are visiting.
#
# Time complexity: O(n * 2^n) - For each element, we have two options,
# take it or not, when we take it, we copy all the existing subsets and
# add this element to them before adding them to the previous result.
# Space complexity: O(2^n) - The result list will have 2^n elements.
#
# Runtime: 36 ms, faster than 92.06%
# Memory Usage: 14 MB, less than 82.71%
class Iterative:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Define an array to hold the results.
        res = [[]]
        # Iterate over the input, for each number, duplicate all
        # existing entries in the result set adding the current number.
        for num in nums:
            res += [curr + [num] for curr in res]
        return res


# Another approach is to generate all possible bitmasks of the same
# length as the number of elements in the input, then iterate over them
# using their bit values to determine which elements to add to the
# current subset. If a given bit i is 0, the subset does not contain the
# element i, if it is 1, it does.
#
# Time complexity: O(n * 2^n) - We iterate over all possible bitmasks of
# length n, for each we append a result to the result set, which is
# amortized O(1)
# Space complexity: O(2^n) - The result list will have 2^n elements.
#
# Runtime: 72 ms, faster than 10.69%
# Memory Usage: 14.2 MB, less than 35.80%
class BinarySorted:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        # Use this range and slicing to avoid dealing with leading 0s
        # in the bitmask.
        for i in range(2**n, 2 ** (n + 1)):
            # Create the subset using the bitmask for this index.
            res.append([nums[j] for j in range(n) if bin(i)[3:][j] == "1"])
        return res


def test():
    executors = [
        Recursive,
        Iterative,
        BinarySorted,
    ]
    tests = [
        [[1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]],
        [[0], [[], [0]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.subsets(t[0])
                exp = t[1]
                result.sort()
                exp.sort()
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
