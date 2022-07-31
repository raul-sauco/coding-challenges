# 307. Range Sum Query - Mutable
# 🟠 Medium
#
# https://leetcode.com/problems/range-sum-query-mutable/
#
# Tags: Array - Design - Binary Indexed Tree - Segment Tree


import timeit
from typing import List


# The requirements of this problem are pretty much exactly what a
# binary indexed tree, also called Fenwick Tree, is designed for.
#
# Time complexity: O(n*log(n)) to create the tree, we insert every item,
# O(log(n)) to update and obtain sumRanges.
# Space complexity: O(n) - The Fenwick tree has the same size as the
# input.
#
# Runtime: 4247 ms, faster than 34.07% of Python3 online submissions for
# Range Sum Query - Mutable.
# Memory Usage: 30.7 MB, less than 94.76% of Python3 online submissions
# for Range Sum Query - Mutable.
class FenwickTree:
    def __init__(self, nums: List[int]):
        # Initialize a list of length nums + 1 with all 0s.
        self.vals = [0] * (len(nums) + 1)
        # Insert all the values in the original input list into the tree.
        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, index: int, val: int) -> None:
        # Indexes in the bit are shifted by 1
        i = index + 1
        # We want to add/subtract from the current existing value.
        # We need to isolate the value at that index first.
        old_val = self.sumToIdx(index) - self.sumToIdx(index - 1)
        val -= old_val
        # Traverse all the ancestors adding val
        while i < len(self.vals):

            # Add val to current node of BI Tree
            self.vals[i] += val

            # Update index to that of parent in update View
            i += i & (-i)

    # Define a function that sums between two given ranges.
    def sumRange(self, left: int, right: int) -> int:
        total = self.sumToIdx(right)
        if left > 0:
            return total - self.sumToIdx(left - 1)
        return total

    # Define a function that sums to the given index.
    def sumToIdx(self, idx: int) -> int:
        sum = 0
        i = idx + 1
        while i > 0:
            sum += self.vals[i]
            i -= i & (-i)
        return sum


# TODO add the Segment Tree solution.


def test():
    executors = [FenwickTree]
    tests = [[]]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for idx, t in enumerate(tests):

                # Test 1
                sol = executor([1, 3, 5])
                # Sum range
                result = sol.sumRange(0, 2)
                exp = 9
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {idx} using \033[1m{executor.__name__}"
                )
                # Update
                sol.update(1, 2)
                # Sum range
                result = sol.sumRange(0, 2)
                exp = 8
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {idx} using \033[1m{executor.__name__}"
                )

                # Test 2
                sol = executor([9, -8])
                sol.update(0, 3)
                # Sum range
                result = sol.sumRange(1, 1)
                exp = -8
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {idx} using \033[1m{executor.__name__}"
                )
                # Sum range
                result = sol.sumRange(0, 1)
                exp = -5
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {idx} using \033[1m{executor.__name__}"
                )
                # Update
                sol.update(1, -3)
                # Sum range
                result = sol.sumRange(0, 1)
                exp = 0
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {idx} using \033[1m{executor.__name__}"
                )

        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
