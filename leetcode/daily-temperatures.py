# 739. Daily Temperatures
# 🟠 Medium
#
# https://leetcode.com/problems/daily-temperatures/
#
# Tags: Array - Stack - Monotonic Stack

import timeit
from typing import List


# Use a monotonic non-increasing stack to store temperatures seen for
# which we haven't found a higher temperature yet. Iterate over the
# input checking the current temperature against the ones stored in the
# stack, we pop all the lower temperatures and save the difference
# between indexes in the result array.
#
# Time complexity: O(n) - We process each temperature a max of 2 times.
# Space complexity: O(n) - The monotonic stack could grow to the same
# size as the input.
#
# This code failed with TLE but it seems to be a bug with the time
# limit in leetcode.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Use a monotonic stack to keep the warmest recorded temperatures.
        stack = []
        # Use an array of the same length as the input to store the results.
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                # We found a warmer temperature, write the number of days we
                # waited.
                res[idx] = i - idx
            # There are no lower temperatures in the array now, add this one.
            stack.append(i)
        return res


def test():
    executors = [Solution]
    tests = [
        [[30], [0]],
        [[30, 60, 90], [1, 1, 0]],
        [[30, 40, 50, 60], [1, 1, 1, 0]],
        [[73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]],
        [
            [73, 74, 75, 71, 69, 72, 73, 73, 73, 76, 73, 73, 73, 72, 100],
            [1, 1, 7, 2, 1, 1, 3, 2, 1, 5, 4, 3, 2, 1, 0],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.dailyTemperatures(t[0])
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
