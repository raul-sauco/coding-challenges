# https://leetcode.com/problems/merge-sorted-array/

from typing import List
from helpers import BColors


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # If n is 0, there is nothing to do
        if n > 0:
            # If m == 0
            if m == 0:
                for i in range(n):
                    nums1[i] = nums2[i]
            else:
                index1, index2 = 0, 0
                remaining1 = m
                # Iterate over the elements in nums1
                while index1 < m + n and index2 < n:
                    print(f'» Checking {index1}:{index2}')
                    # If the current value in nums2 is less than the current value in nums1
                    # or we have used all the valid values in nums1
                    if nums2[index2] < nums1[index1] or remaining1 == 0:
                        print(
                            f'» {nums1[index1]} > {nums2[index2]}; inserting at {index1}')
                        # Insert from n2 at current position
                        nums1[index1:index1] = [nums2[index2]]
                        del nums1[-1]
                        # Update the indexes
                        index1 += 1
                        index2 += 1
                    else:
                        print(
                            f'» {nums1[index1]} <= {nums2[index2]}; skipping')
                        # Move to the next element
                        index1 += 1
                        remaining1 -= 1
                    print(f'» {nums1}')

    # This is a better solution! Starting from the tail
    def mergeFromTail(self, nums1, m, nums2, n):
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1

    # And this is a really cool solution using built-in functionality
    def mergeVeryShort(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()


def test():
    sol = Solution()
    nums1, m, nums2, n, expected = [1, 2, 3, 0, 0, 0], 3, [
        2, 5, 6], 3, [1, 2, 2, 3, 5, 6]
    sol.merge(nums1, m, nums2, n)
    assert nums1 == expected, f'{nums1} differs from {expected}'

    nums1, m, nums2, n, expected = [1], 1, [], 0, [1]
    sol.merge(nums1, m, nums2, n)
    assert nums1 == expected, f'{nums1} differs from {expected}'

    nums1, m, nums2, n, expected = [0], 0, [1], 1, [1]
    sol.merge(nums1, m, nums2, n)
    assert nums1 == expected, f'{nums1} differs from {expected}'

    nums1, m, nums2, n, expected = [2, 0], 1, [1], 1, [1, 2]
    sol.merge(nums1, m, nums2, n)
    assert nums1 == expected, f'{nums1} differs from {expected}'

    nums1, m, nums2, n, expected = [-1, 0, 0, 3, 3, 3, 0,
                                    0, 0], 6, [1, 2, 2], 3, [-1, 0, 0, 1, 2, 2, 3, 3, 3]
    sol.merge(nums1, m, nums2, n)
    assert nums1 == expected, f'{nums1} differs from {expected}'

    print(f'\n{BColors.bold}{BColors.ok_green}» All tests passed!{BColors.end_dc}\n')


test()


def testFromTail():
    sol = Solution()
    nums1, m, nums2, n, expected = [1, 2, 3, 0, 0, 0], 3, [
        2, 5, 6], 3, [1, 2, 2, 3, 5, 6]
    sol.mergeFromTail(nums1, m, nums2, n)
    assert nums1 == expected, f'{nums1} differs from {expected}'

    nums1, m, nums2, n, expected = [1], 1, [], 0, [1]
    sol.mergeFromTail(nums1, m, nums2, n)
    assert nums1 == expected, f'{nums1} differs from {expected}'

    nums1, m, nums2, n, expected = [0], 0, [1], 1, [1]
    sol.mergeFromTail(nums1, m, nums2, n)
    assert nums1 == expected, f'{nums1} differs from {expected}'

    nums1, m, nums2, n, expected = [2, 0], 1, [1], 1, [1, 2]
    sol.mergeFromTail(nums1, m, nums2, n)
    assert nums1 == expected, f'{nums1} differs from {expected}'

    nums1, m, nums2, n, expected = [-1, 0, 0, 3, 3, 3, 0,
                                    0, 0], 6, [1, 2, 2], 3, [-1, 0, 0, 1, 2, 2, 3, 3, 3]
    sol.mergeFromTail(nums1, m, nums2, n)
    assert nums1 == expected, f'{nums1} differs from {expected}'

    print(f'\n{BColors.bold}{BColors.ok_green}» All tests passed!{BColors.end_dc}\n')


testFromTail()
