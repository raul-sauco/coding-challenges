# https://leetcode.com/problems/single-number/


from typing import List

# Solution using Xor
#
# Runtime: 255 ms, faster than 26.83% of Python3 online submissions for Single Number.
# Memory Usage: 16.7 MB, less than 50.38 % of Python3 online submissions for Single Number.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res


def test():
    tests = [
        [[2, 2, 1], 1],
        [[4, 1, 2, 1, 2], 4],
        [[1], 1],
    ]
    sol = Solution()
    for t in tests:
        assert sol.singleNumber(t[0]) == t[1]


test()
