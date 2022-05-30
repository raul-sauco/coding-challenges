from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            for index2 in range(index + 1, len(nums)):
                if nums[index] + nums[index2] == target:
                    return [index, index2]

        return 0

def test():
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    print('All tests passed!')

test()
