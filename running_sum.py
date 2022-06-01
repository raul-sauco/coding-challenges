# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List

from helpers import BColors


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            nums[i] = sum
        return nums

    def runningSumInPlaceWithoutExtraVariable(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


def test():
    sol = Solution()
    assert sol.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert sol.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert sol.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    assert sol.runningSum([1, 1, 8, -90, 1]) == [1, 2, 10, -80, -79]
    assert sol.runningSum([]) == []
    print(f'\n{BColors.bold}{BColors.ok_green}» All tests passed!{BColors.end_dc}\n')


test()
