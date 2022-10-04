# 287. Find the Duplicate Number
# 🟠 Medium
#
# https://leetcode.com/problems/find-the-duplicate-number/
#
# Tags: Array - Two Pointers - Binary Search - Bit Manipulation

import timeit
from typing import List

# 10e4 calls
# » BitManipulation     0.04275   seconds
# » TortoiseAndHare     0.01008   seconds

# Use an integer as a bit mask of len(nums) bits, iterate over the input
# using the integers as indexes in the mask, for each, set its bit to 1
# when we find a bit that is already set, we have our duplicate number.
#
# Time complexity: O(n) - We visit each number once and perform O(1)
# operations.
# Space complexity: O(1) - We only store one integer in memory. The
# maximum size of the integer is ~12KB, this solution only works in
# Python because of the unlimited size of integers. In other languages,
# we could use several integers.
#
# Runtime: 1587 ms, faster than 19.73%
# Memory Usage: 27.9 MB, less than 91.11%
class BitManipulation:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize a mask of zeroes.
        mask = 0
        # Iterate over the input.
        for num in nums:
            idx = 1 << (num - 1)
            # Check if the bit is set already.
            if mask & idx:
                return num
            # Set the bit to 1
            mask |= idx


# This problem can also be solved using Floyd's cycle detection
# algorithm, there is a very good explanation on the problem's official
# solution, point 7. We run Floyd's algorithm to find the point were the
# tortoise and hare meet, at that point, we slow down the hare to the
# same speed as the tortoise and move the tortoise back to the start,
# when we move them forward again, the point at which meet will be the
# first node in the cycle.
#
# Time complexity: O(n) - The tortoise will visit a maximum of 2n nodes.
# Space complexity; O(1) - Two pointers stored.
#
# Runtime: 665 ms, faster than 92.16%
# Memory Usage: 27.9 MB, less than 57.85%
class TortoiseAndHare:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize the tortoise and hares in their respective
        # positions.
        tortoise = nums[nums[0]]
        hare = nums[nums[nums[0]]]
        # The first step is to find the point in the list where the
        # hare will meet the tortoise.
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
        # Once we find that point, move the tortoise back to the start.
        tortoise = nums[0]
        # Now slow down the hare, the distance between the hare and the
        # first node in the cycle and the tortoise and the first node
        # in the cycle is the same, the point at which they will meet
        # will be that node.
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        # Return the value of the first node in the cycle.
        return hare


def test():
    executors = [
        BitManipulation,
        TortoiseAndHare,
    ]
    tests = [
        [[1, 1], 1],
        [[1, 3, 4, 2, 2], 2],
        [[3, 1, 3, 4, 2], 3],
        [[37] + [x for x in range(1, 100001)], 37],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findDuplicate(t[0])
                exp = t[1]
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
