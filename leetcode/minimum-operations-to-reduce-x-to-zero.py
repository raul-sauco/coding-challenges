# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        longest = -1
        target = sum(nums) - x
        left = 0
        right = 0
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            if current_sum == target:
                longest = max(longest, 1 + right - left)
            while current_sum >= target and left < len(nums):
                current_sum -= nums[left]
                left += 1
                if current_sum == target:
                    longest = max(longest, 1 + right - left)

        return -1 if longest == -1 else len(nums) - longest


tests = [
    [[1], 3, -1],
    [[1], 1, 1],
    [[5], 5, 1],
    [[1, 1, 4, 2, 3], 5, 2],
    [[5, 6, 7, 8, 9], 4, -1],
    [[5, 6, 7, 8, 9], 35, 5],
    [[5, 6, 7, 8, 9], 30, 4],
    [[3, 1, 1, 20, 1, 2, 1, 3], 27, 5],
    [[3, 2, 20, 1, 1, 3], 10, 5],
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 16, 15],
]


def test():
    sol = Solution()
    for t in tests:
        result = sol.minOperations(t[0], t[1])
        assert result == t[2], f'{result} != {t[2]}'


test()


def minOperationsNaive(self, nums: List[int], x: int) -> int:

    res = len(nums)+1
    left_sum = 0
    calculations = 0
    for end in range(len(nums), 0, -1):
        if (end < len(nums)):
            # Add the left element value to the sum
            left_sum += nums[end]
            if left_sum == x:
                # If the sum of the left elements to this point matches, we cannot get a better solution later
                steps = len(nums) - end
                res = min(res, steps)
                break
            if left_sum > x:
                # If the left sum is already greater than the number, we can't calculate a solution
                break

        # Now calculate sums starting from the right
        i = 0
        sum = left_sum  # Start with whatever value we have taken from the right, it will be 0 for the first iteration
        while i < end and sum < x:
            calculations += 1
            sum += nums[i]
            i += 1
            steps = i + (len(nums) - end)
            # If we have a match, compare the number of steps with the current best
            if sum == x:
                res = min(res, steps)
            elif sum > x:
                break

        # print(f'» Found a solution for [{nums}, {x}] in {calculations} steps')
        # return a solution, if found, or -1
    return res if res < len(nums)+1 else -1
