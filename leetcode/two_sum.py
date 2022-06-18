from typing import List

# Solution using a hashmap has a O(n) for time and space.
# Runtime: 104 ms, faster than 52.66% of Python3 online submissions for Two Sum.
# Memory Usage: 15.1 MB, less than 49.66 % of Python3 online submissions for Two Sum.

# Solution iterating through each item of the array has a complexity O(n^2) because it runs
# through the entire array through each item on it.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in s:
                return [s[c], i]
            s[nums[i]] = i

        # O(n^2) because it runs through the entire array through each item on it
        # for index in range(len(nums)):
        #     for index2 in range(index + 1, len(nums)):
        #         if nums[index] + nums[index2] == target:
        #             return [index, index2]

        # return 0

def test():
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    print('All tests passed!')

test()
