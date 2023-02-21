# 540. Single Element in a Sorted Array
# 🟠 Medium
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/
#
# Tags: Array - Binary Search

import timeit
from typing import List


# Use a modified version of binary search that checks the neighbors of
# the value under mid to determine whether to discard the right of left
# half of the remaining array at each step. We can use the fact that, on
# the sequence before the single value, the pointers for the duplicates
# will be (even, odd) while after the single value they will be
# (odd, even). When both values right and left of the mid are different,
# we have found the single value and we can return it.
#
# Time complexity: O(n*log(n)) - At each step we stop considering half
# of the current search space.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 182 ms Beats 55.3%
# Memory 23.7 MB Beats 39.30%
class BinarySearch:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Base case, only one value or non-duplicate at the beginning
        # of the input array.
        if len(nums) == 1 or nums[0] != nums[1]:
            return nums[0]
        # Base case, the non-duplicate value is at end of the input array.
        if nums[-2] != nums[-1]:
            return nums[-1]
        # Left pointer will always be to the left of the non-duplicate
        # value, should be an uneven index and nums[l-1] == nums[l]. The
        # right pointer will always be to the right of the non-duplicate
        # value, it should always be in an uneven index and it should
        # always comply with nums[r] == nums[r+1].
        l, r = 1, len(nums) - 2
        while True:
            mid = (r + l) // 2
            # mid points to the non-duplicate.
            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                return nums[mid]
            # nums[mid] is not the single value.
            # If mid is an odd value
            if mid % 2:
                # If the value before it is the same, adjust the left
                # pointer, otherwise, the right pointer.
                if nums[mid - 1] == nums[mid]:
                    l = mid
                else:
                    r = mid
            # mid is an even value pointer.
            else:
                # If the value after is the same, adjust the left
                # pointer to that value.
                if nums[mid] == nums[mid + 1]:
                    l = mid + 1
                # Otherwise, move the right pointer to the value before.
                else:
                    r = mid - 1


# Brilliant solution by StefanPochmann:
# https://leetcode.com/problems/single-element-in-a-sorted-array/solutions/100732/
#
# Uses the fact that: (even ^ 1 == even + 1) and (odd ^ 1 == odd - 1) to
# simplify the code of the previous solution while using similar logic.
#
# Time complexity: O(n*log(n)) - At each step we stop considering half
# of the current search space.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 173 ms Beats 83.3%
# Memory 23.6 MB Beats 86.81%
class BinarySearchXor:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == nums[mid ^ 1]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


def test():
    executors = [
        BinarySearch,
        BinarySearchXor,
    ]
    tests = [
        [[4], 4],
        [[-1, -1, 4], 4],
        [[3, 3, 7, 7, 10, 11, 11], 10],
        [[3, 3, 7, 7, 10, 10, 11], 11],
        [[1, 1, 2, 3, 3, 4, 4, 8, 8], 2],
        [[1, 2, 2, 3, 3, 4, 4, 8, 8], 1],
        [[-1, -1, 0, 2, 2, 4, 4, 8, 8], 0],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.singleNonDuplicate(t[0])
                exp = t[1]
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
