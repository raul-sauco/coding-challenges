# https://leetcode.com/problems/jump-game/

import timeit
from typing import List

# Intuition: Mark the end of the array as our point to reach (goal) and start checking the
# positions before it.
# For each position, if we can reach the current goal from there i + nums[i] >= goal
# mark that position as the new goal and check if we can reach it from any of the previous positions.
#
# Runtime: 477 ms, faster than 97.37% of Python3 online submissions for Jump Game.
# Memory Usage: 15.4 MB, less than 18.06 % of Python3 online submissions for Jump Game.


class Linear:
    def canJump(self, nums: List[int]) -> bool:
        # Initial goal, reaching the last position of the array.
        goal = len(nums) - 1
        # Iterate over all the positions except the last one
        for i in range(len(nums) - 2, -1, -1):
            # If from the current position we can reach the current goal
            if i + nums[i] >= goal:
                # Reaching this position becomes our current goal
                goal = i
        # If our last goal is to reach the start position, we can jump to the end
        return goal == 0


# Similar to the brute force algorithm but memorize positions that we have explored but do not lead
# to a solution.
# There is no need to memoize positions that return True because the True value propagates and
# terminates execution, returning True, as soon as the first one is found.
#
# Runtime: 8078 ms, faster than 5.00% of Python3 online submissions for Jump Game.
# Memory Usage: 27.8 MB, less than 5.11 % of Python3 online submissions for Jump Game.
class Memoization:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def explore(n: int):
            if n in memo:
                return memo[n]
            if nums[n] + n >= len(nums)-1:
                return True
            for i in range(nums[n], 0, -1):
                if explore(n+i):
                    return True
            memo[n] = False
            return False
        return explore(0)


# Start at n=0 and explore the furthest position you can reach.
# Recursively explore the furthest position you can reach from there.
# If at any point you can reach the end of the array or further, return True
# Once all the possibilities have been explored, return False
# Worst case would be O(n^2) if all n values are small and they fail towards the end.
class BruteForce:
    def canJump(self, nums: List[int]) -> bool:
        def explore(n: int):
            if nums[n] + n >= len(nums)-1:
                return True
            for i in range(nums[n], 0, -1):
                if explore(n+i):
                    return True
            return False
        return explore(0)


# Reasoning; for each element i, including i = len(nums)-1, we can jump there if there is any element
# at position j with val = i-j
#
# The worst case scenario for this solution is when num[i] for larger is are large values.
# In LeetCode it fails with Time Limit Exceeded.
class BackwardTabulation:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(len(nums)-2, -1, -1):
            # If we can reach the last element of the current array from this position
            if i+nums[i] >= len(nums)-1:
                if self.canJump(nums[:i+1]):
                    return True
        return False

# The worst case scenario would be having large values for num[i]
# In that case the solution does not pass on LeetCode, instead it fails with Time Limit Exceeded.


class Tabulation:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [False for _ in range(len(nums))]
        can_reach[0] = True
        for i in range(len(nums)):
            # If we can reach this position
            if can_reach[i]:
                for j in range(nums[i]):
                    landing = i + j + 1
                    if landing < len(can_reach) - 1:
                        # Mark all the positions we can jump to ahead of this one as reachable
                        can_reach[landing] = True
                    elif landing == len(can_reach) - 1:
                        # Quick return if we are marking the last element as True
                        return True
        return can_reach[len(nums) - 1]


def test():
    executor = [
        {'executor': Linear, 'title': 'Linear', },
        {'executor': Memoization, 'title': 'Memoization', },
        {'executor': BruteForce, 'title': 'BruteForce', },
        {'executor': BackwardTabulation, 'title': 'BackwardTabulation', },
        {'executor': Tabulation, 'title': 'Tabulation', },
    ]
    tests = [
        [[10, 3, 1, 1, 4], True],
        [[2, 3, 1, 1, 4], True],
        [[3, 2, 1, 0, 4], False],
        [[0], True],
        [[1, 0], True],
        [[0, 1], False],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e5'))):
            for t in tests:
                sol = e['executor']()
                result = sol.canJump([*t[0]])
                expected = t[1]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
