# 1539. Kth Missing Positive Number
# 🟢 Easy
#
# https://leetcode.com/problems/kth-missing-positive-number/
#
# Tags: Array - Binary Search

import bisect
import timeit
from typing import Callable, Generic, List, Sequence, TypeVar


class BruteForce:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, expected, missing = 0, 1, 0
        while missing < k - 1:
            if i < len(arr) and arr[i] == expected:
                i += 1
                expected += 1
            else:
                missing += 1
                expected += 1
        return expected


# Use binary search to find the index right before the index where the
# kth missing value would be if found. Use the combination of index and
# value to compute how many missing values there are before a given
# element.
#
# Time complexity: O(log(n)) - Binary search over the elements in arr.
# Space complexity: O(1) - Constant extra memory used.
#
# Runtime 48 ms Beats 88.93%
# Memory 14 MB Beats 44.89%
class BinarySearch:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Base case, the kth missing element is to the left of the
        # first element in the array.
        if k < arr[0]:
            return k
        # Left pointer and right non-inclusive right pointer.
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            # The number of integers missing up to arr[mid] is:
            # missing_left = arr[mid] - mid - 1
            if arr[mid] - mid - 1 < k:
                l = mid + 1
            else:
                r = mid
        # arr[l] is the biggest value in the array smaller than
        # the kth missing positive integer. Compute kth
        return k + l


# Looking for a solution to use bisect, I came to this:
# https://stackoverflow.com/a/39501468/2557030
# It uses the same logic as the previous solution but uses bisect to
# find the "insertion point" instead of manually doing it, I expected
# this solution to run faster but it didn't and it used more more
# memory, which makes sense because it uses an extra nested class.
#
# Time complexity: O(log(n)) - Binary search over the elements in arr.
# Space complexity: O(1) - Constant extra memory used.
#
# Runtime 48 ms Beats 88.93%
# Memory 14.4 MB Beats 13.3%
class BuiltInBinarySearch:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Base case, the kth missing element is to the left of the
        # first element in the array.
        if k < arr[0]:
            return k
        # Inner class that can access arr.
        class KeyWrapper:
            def __getitem__(self, i):
                return arr[i] - i - 1

            def __len__(self):
                return len(arr)

        return k + bisect.bisect_left(KeyWrapper(), k)


def test():
    executors = [
        BruteForce,
        BinarySearch,
        BuiltInBinarySearch,
    ]
    tests = [
        [[142], 145, 146],
        [[1, 2, 3, 4], 2, 6],
        [[2, 3, 4, 7, 11], 5, 9],
        [[100_000], 100_009, 100_010],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findKthPositive(t[0], t[1])
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
