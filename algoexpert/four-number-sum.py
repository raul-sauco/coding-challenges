# Four Number Sum
# 🔴 Hard
#
# https://www.algoexpert.io/questions/four-number-sum
#
# Tags: Array - Sorting

import timeit
from collections import defaultdict


# The brute force solution explores all options using nested loops.
#
# Time complexity: O(n^4) - Four levels deep nested loops.
# Space complexity: O(1) - Constant space is used.
class BruteForce:
    def fourNumberSum(self, array, targetSum):
        res = []
        for i in range(len(array) - 3):
            for j in range(i + 1, len(array) - 2):
                for k in range(j + 1, len(array) - 1):
                    for m in range(k + 1, len(array)):
                        vals = [array[i], array[j], array[k], array[m]]
                        if sum(vals) == targetSum:
                            res.append(vals)
        return res


# Use a hashmap of pair sums to find target quadruplets in O(n^2) time.
#
# Time complexity: O(n^2) - Nested loops with constant time operations
# in the inner loop.
# Space complexity: O(n^2) - The hashmap will hold the sum of all pairs.
class Solution:
    def fourNumberSum(self, array, targetSum):
        # Use a hashmap of pair sums to the pairs that add up to them.
        # Use a set to store quadruplets to eliminate duplicates. The OJ
        # accepts a set of tuples as the result.
        sums, res = defaultdict(set), set()
        # Iterate over all pairs in O(n^2).
        for i in range(len(array) - 1):
            for j in range(i + 1, len(array)):
                vals = (array[i], array[j])
                s = array[i] + array[j]
                if targetSum - s in sums:
                    for pair in sums[targetSum - s]:
                        if array[i] not in pair and array[j] not in pair:
                            res.add(
                                tuple(
                                    sorted(
                                        [pair[0], pair[1], array[i], array[j]]
                                    )
                                )
                            )
                sums[s].add(vals)
        return res


def test():
    executors = [
        BruteForce,
        Solution,
    ]
    tests = [
        [[1, 2, 3, 4, 5, 6, 7], 10, [[1, 2, 3, 4]]],
        [[7, 6, 4, -1, 1, 2], 16, [[7, 6, 4, -1], [7, 6, 1, 2]]],
        [
            [5, -5, -2, 2, 3, -3],
            0,
            [[-5, -3, 3, 5], [-5, -2, 2, 5], [-3, -2, 2, 3]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.fourNumberSum(t[0], t[1])
                # The result could be in any order.
                result = sorted(map(sorted, result))
                exp = sorted(map(sorted, t[2]))
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
