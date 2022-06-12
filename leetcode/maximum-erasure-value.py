# https://leetcode.com/problems/maximum-erasure-value/
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = {}
        sum = 0
        left = 0
        max_sum = 0
        for right in range(len(nums)):
            if nums[right] in seen:
                # Move the left pointer to the left of the last seen position removing the values from the sum
                while left <= seen[nums[right]]:
                    sum -= nums[left]
                    left += 1

            # Always add the new, or updated, seen position and the value to the sum
            seen[nums[right]] = right
            sum += nums[right]
            max_sum = max(max_sum, sum)

        return max_sum


tests = [
    [[4, 2, 4, 5, 6], 17],
    [[5, 2, 1, 2, 5, 2, 1, 2, 5], 8],
    [[1], 1],
    [[10000, 1, 10000, 1, 1, 1, 1, 1, 1], 10001]
]


def test():
    sol = Solution()
    for t in tests:
        result = sol.maximumUniqueSubarray(t[0])
        assert result == t[1], f'{result} != {t[1]}'


test()
