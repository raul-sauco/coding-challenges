# https://leetcode.com/problems/range-sum-query-immutable/

# Tags: Array - Design - Prefix Sum

import timeit
from itertools import accumulate
from typing import List


# Create an array of sums. When a range sum is requested, fetch it from Sum(right - left)
#
# Time complexity: O(n) to create the prefix sum array, O(1) to calculate the range sums on sumRange() calls.
# Space complexity: O(n) for the prefix sum array
#
# Runtime: 95 ms, faster than 83.82% of Python3 online submissions for Range Sum Query - Immutable.
# Memory Usage: 17.7 MB, less than 31.84% of Python3 online submissions for Range Sum Query - Immutable.
class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - (self.sums[left - 1] if left > 0 else 0)


# Similar idea, same complexity but it runs slower because the list is iterated over twice, one to prepend the 0
# and another one to calculate the prefix sum.
#
# Runtime: 147 ms, faster than 50.84% of Python3 online submissions for Range Sum Query - Immutable.
# Memory Usage: 17.7 MB, less than 31.84% of Python3 online submissions for Range Sum Query - Immutable.
class ZeroPadded:
    def __init__(self, nums: List[int]):
        self.sums = list(accumulate([0] + nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
def test():
    executors = [NumArray, ZeroPadded]
    tests = [
        [
            [-2, 0, 3, -5, 2, -1],
            {
                1: [0, 2],
                -1: [2, 5],
                -3: [0, 5],
                -1: [5, 5],
            },
        ],
        [
            [2],
            {
                2: [0, 0],
            },
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1e5"))):
            for i, t in enumerate(tests):
                sol = executor(t[0])
                for sum in t[1]:
                    result = sol.sumRange(*t[1][sum])
                    exp = sum
                    assert (
                        result == exp
                    ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
