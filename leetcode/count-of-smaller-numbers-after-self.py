# 315. Count of Smaller Numbers After Self
# 🔴 Hard
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
#
# Tags: Array - Binary Search - Divide and Conquer - Binary Indexed Tree - Segment Tree - Merge Sort - Ordered Set

import timeit
from typing import List


# We can start by the naive brute-force solution, visit each number in nums in order and check how many
# elements after nums are smaller than it. O(n2) - it will fail with Time Limit Exceeded.
#
# Time complexity: O(n^2).
# Space complexity: O(1) - if we don't take into account the input and output arrays.
class Naive:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            for val in nums[i + 1 :]:
                if val < num:
                    res[i] += 1
        return res


# A specialized binary indexed tree where the update method only increments by 1.
# There is an example of a standard binary indexed tree with comments in `utils/binary_indexed_tree.py`
class BITree:
    def __init__(self, n: int):
        self.sums = [0] * (n + 1)

    def update(self, idx: int) -> None:
        idx += 1
        while idx < len(self.sums):
            self.sums[idx] += 1
            idx += idx & -idx

    def sum(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res += self.sums[idx]
            idx -= idx & -idx
        return res


# Use a binary indexed tree to keep count, for each value in the input array, of how many elements equal or smaller
# we have already seen. Then start iterating from the back of the input array, for each position, update the result
# array and add the current value to the binary indexed tree.
#
# Time complexity: O(n*log(n)) - We visit each element on the input array and, for each, update the tree O(log(n)).
# Space complexity: O(n) - The binary indexed tree is stored in memory as an array of size len(nums) + 1.
#
# Runtime: 4187 ms, faster than 54.52% of Python3 online submissions for Count of Smaller Numbers After Self.
# Memory Usage: 34.8 MB, less than 51.30% of Python3 online submissions for Count of Smaller Numbers After Self.
class BITSolution:
    def countSmaller(self, nums):

        # Create a dictionary of all unique values in the input array as keys pointing to their
        # position if they were an ordered set with the smallest at 0 and the biggest at len(n) - 1.
        dict = {value: idx for idx, value in enumerate(sorted(set(nums)))}

        # Initialize the binary indexed tree, and the results array, to all 0s
        bi_tree, res = BITree(len(dict)), [0] * len(nums)

        # Start at the back of nums and iterate over every position
        for i in range(len(nums) - 1, -1, -1):

            # Update the result set with the current sum of frequencies in the tree at that point.
            # The tree contains, for each value, the sum of elements smaller than the current one.
            res[i] = bi_tree.sum(dict[nums[i]])

            # Update the sums on the binary indexed tree. This is a special use case in which we always increment
            # by 1 and we are using the dictionary to translate between values and indexes.
            # The result is that increasing the value at the index pointed to by the dictionary, we increase the
            # numbers equal or less than this value that we have seen up to that moment.
            # Since we are iterating from the back, we can use that information to check how many values less than
            # the current one we have seen and update the result array.
            bi_tree.update(dict[nums[i]])

        return res


# TODO look into the segment tree solution.
# https://www.topcoder.com/thrive/articles/Range%20Minimum%20Query%20and%20Lowest%20Common%20Ancestor
class SegmentTreeSol:
    def countSmaller(self, nums: List[int]) -> List[int]:
        pass


# TODO look into the merge sort solution.
class MergeSortSol:
    def countSmaller(self, nums: List[int]) -> List[int]:
        pass


def test():
    executors = [
        # Naive,
        BITSolution,
    ]
    tests = [
        [
            [3, 10, 0, 7, 1, -13, 6, -5, 16, 7, 3, -9],
            [5, 9, 3, 6, 3, 0, 3, 1, 3, 2, 1, 0],
        ],
        [[5, 2, 6, 1], [2, 1, 1, 0]],
        [[-1], [0]],
        [[-1, -1], [0, 0]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.countSmaller(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
