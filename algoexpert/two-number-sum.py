# Two Number Sum
# 🟢 Easy
#
# https://www.algoexpert.io/questions/two-number-sum
#
# Tags: Array - Hash Set

import timeit
from typing import List


# Classic two sum problem, the most common solution is to use a set to
# check if each number complementary has been seen in O(1).
#
# Time complexity: O(n) - We iterate once over the input and do O(1)
# operations for each element.
# Space complexity: O(n) - The set could grow to the same size as the
# input.
class HashSet:
    def twoNumberSum(self, array: List[int], targetSum: int) -> List[int]:
        # A set of integer values that we have seen.
        seen = set()
        for num in array:
            if targetSum - num in seen:
                return [targetSum - num, num]
            else:
                seen.add(num)
        # If the sum cannot be obtained with two numbers, return an
        # empty list.
        return []


# A different solution that sacrifices time to gain a better space
# complexity, first sort the array, then use two pointers to try to
# compute the target using a small and a large value.
#
# Time complexity: O(n*log(n)) - The sorting step has the highest
# time complexity, the two pointer section that visits the elements is
# O(n).
# Space complexity: O(1) - The algorithm does not use any extra memory.
class TwoPointers:
    def twoNumberSum(self, array: List[int], targetSum: int) -> List[int]:
        array.sort()
        l, r = 0, len(array) - 1
        while l < r:
            s = array[l] + array[r]
            # If the sum is smaller than the target, we need a bigger
            # sum, move the left pointer right.
            if s < targetSum:
                l += 1
            # If the sum is larger than the target, we need a smaller
            # sum, move the right pointer left.
            elif s > targetSum:
                r -= 1
            else:
                return [array[l], array[r]]
        return []


def test():
    executors = [
        HashSet,
        TwoPointers,
    ]
    tests = [
        [[11], 11, []],
        [[3, 5, -4, 8, 11, 1, -1, 6], 10, [11, -1]],
        [[-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164, []],
        [[-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163, [210, -47]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sorted(sol.twoNumberSum(t[0], t[1]))
                exp = sorted(t[2])
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
