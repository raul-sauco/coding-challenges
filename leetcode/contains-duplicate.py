# https://leetcode.com/problems/contains-duplicate/


from typing import List

# Runtime: 514 ms, faster than 73.16% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26 MB, less than 71.69 % of Python3 online submissions for Contains Duplicate.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False

    # Cool faster solution
    # return not(len(nums) == len(set(nums)))


def test():
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 1]) == True
    assert sol.containsDuplicate([1, 2, 3, 4]) == False
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True


test()
