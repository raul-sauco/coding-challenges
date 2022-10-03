# 1578. Minimum Time to Make Rope Colorful
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
#
# Tags: Array - String - Dynamic Programming - Greedy

import timeit
from typing import List


# We can see that to solve the problem we need to find all sequences of
# the same color and, for each, eliminate all balloons except for one,
# we can use a greedy approach because we know that the most efficient
# solution will be to keep the balloon with the highest removal cost and
# keep the others. We iterate over the balloons keeping the color of the
# current sequence and the highest removal cost that we have seen in the
# current sequence in two variables, if the balloon we visit has the
# same color of the current sequence, we know that we need to remove
# either this balloon or the previous one we decided to keep, we
# choose to remove the one with the smaller cost and add that cost to
# the result. When we get to a balloon with a different color, we
# temporarily decide to keep it and store that color as the current
# sequence color and its cost as the highest cost.
#
# Time complexity: O(n) - We visit each element once and perform O(1)
# tasks.
# Space complexity: O(1) - We only store three variables. Constant space.
#
# Runtime: 1040 ms, faster than 98.87%
# Memory Usage: 25 MB, less than 52.92%
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Store the color of the current sequence.
        current_color = None
        # Store the highest value seen for the current sequence.
        current_highest = 0
        # Initialize the result.
        res = 0
        # Iterate over the balloons.
        for i in range(len(colors)):
            # If this is a new color, reinitialize the sequence.
            if current_color != colors[i]:
                current_highest = neededTime[i]
                current_color = colors[i]
            # Else, if we are inside a sequence.
            else:
                # Check which balloon in the sequence had a higher cost
                # and add the other to the time cost.
                if neededTime[i] > current_highest:
                    # If the current cost is higher, evict the previous
                    # highest cost and add it to the result.
                    res += current_highest
                    current_highest = neededTime[i]
                else:
                    # Otherwise, if they are equal or the current is
                    # lower, add that one to the cost.
                    res += neededTime[i]
        return res


def test():
    executors = [Solution]
    tests = [
        ["abc", [1, 2, 3], 0],
        ["aabaa", [1, 2, 3, 4, 1], 2],
        ["abaac", [1, 2, 3, 4, 5], 3],
        ["bbbaaa", [4, 9, 3, 8, 8, 9], 23],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minCost(t[0], t[1])
                exp = t[2]
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
