# 1899. Merge Triplets to Form Target Triplet
# 🟠 Medium
#
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
#
# Tags: Array - Greedy

import timeit
from typing import List


# Iterate over the triplets determining if we can use them, which means
# that neither of the tree positions is greater than the target, if we
# can use that triplet, update that position on the target to true.
# and 3 pointers in memory.
#
# Time complexity: O(n) - We visit each triplet once.
# Space complexity: O(1) - Constant space.
#
# Runtime: 3140 ms, faster than 67.1%
# Memory Usage: 59.2 MB, less than 32.94%
class Solution:
    def mergeTriplets(
        self, triplets: List[List[int]], target: List[int]
    ) -> bool:
        # Keep a record of positions that we have matched.
        matched = (False, False, False)
        # Iterate over the triplets.
        for triplet in triplets:
            # Check if we can use this triplet.
            if all([triplet[i] <= target[i] for i in range(3)]):
                # Use it.
                matched = [
                    matched[i] or triplet[i] == target[i] for i in range(3)
                ]
                # If we have matched all positions, return True
                if all(matched):
                    return True
        # Return False if we could not construct the target triplet.
        return False


def test():
    executors = [Solution]
    tests = [
        [[[3, 4, 5], [4, 5, 6]], [3, 2, 5], False],
        [[[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5], True],
        [[[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5], True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.mergeTriplets(t[0], t[1])
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
