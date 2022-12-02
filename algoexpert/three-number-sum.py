# Three Number Sum
# 🟠 Medium
#
# https://www.algoexpert.io/questions/three-number-sum
#
# Tags: Array, Two Pointer, Sorting

import timeit


# Find all combinations of three numbers in the input that add up to the
# target sum by fixing one number at a time and using two pointers to
# find combinations of other two numbers that make up to the sum.
#
# Time complexity: O(n^2) - For each value in the array, we explore all
# combinations of other two values in linear time.
# Space complexity: O(1) - If we don't count the output or input arrays.
class Solution:
    def threeNumberSum(self, array, targetSum):
        array.sort()
        res = []
        # Fix the leftmost element, then use two pointers to find all
        # combinations of other two values that add to the target sum.
        for i in range(len(array) - 2):
            l, r = i + 1, len(array) - 1
            while l < r:
                val = array[i] + array[l] + array[r]
                if val == targetSum:
                    res.append((array[i], array[l], array[r]))
                    l += 1
                    r -= 1
                elif val < targetSum:
                    l += 1
                else:
                    r -= 1
        return res


def test():
    executors = [
        Solution,
    ]
    tests = [
        [[8, 10, -2, 49, 14], 57, [(-2, 10, 49)]],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 29, [(5, 9, 15), (6, 8, 15)]],
        [[12, 3, 1, 2, -6, 5, -8, 6], 0, [(-8, 2, 6), (-8, 3, 5), (-6, 1, 5)]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.threeNumberSum(t[0], t[1])
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
