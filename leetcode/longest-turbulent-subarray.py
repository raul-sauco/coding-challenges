# 978. Longest Turbulent Subarray
# 🟠 Medium
#
# https://leetcode.com/problems/longest-turbulent-subarray/
#
# Tags: Array - Dynamic Programming - Sliding Window

import timeit
from typing import List


# Use a sliding window moving the right pointer forward while the sign
# is the opposite sign than on the previous two elements, when the
# condition fails, we adjust the left pointer to either, the current
# element, if the element is equal to the previous one, or the previous
# element if it is greater or smaller than the previous element, we
# also keep a variable with the last sign that we have seen that we use
# to check that the next one is the opposite sign.
#
# Time complexity: O(n) - We visit each element once and do O(1) work.
# Space complexity: O(1) - Constant extra space used.
#
# Runtime 493 ms Beats 83.81%
# Memory 17.9 MB Beats 72.75%
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return len(arr)
        # The pointer at which the current sequence starts.
        l, res = 0, 1
        # A flag that marks the sign we expect.
        greater = arr[0] < arr[1]
        for r in range(1, len(arr)):
            # Two equal elements break the sequence and do not start
            # a new one.
            if arr[r - 1] == arr[r]:
                l = r
                # Make sure there is a next element.
                if r < len(arr) - 1:
                    # The next sign is the one between next elements.
                    greater = arr[r] < arr[r + 1]
            # The wrong sign breaks the sequence but we can still use
            # the left pointer as the start of the next sequence.
            elif greater != (arr[r - 1] < arr[r]):
                l = r - 1
                # Expect the next sign to be the opposite.
                greater = arr[r - 1] > arr[r]
            # Correct opposite sign, increase the sequence and switch
            # switch the flag.
            else:
                res = max(res, 1 + r - l)
                greater = not greater
        return res


def test():
    executors = [Solution]
    tests = [
        [[100], 1],
        [[3, 3], 1],
        [[4, 8, 12, 16], 2],
        [[9, 4, 2, 1, 7, 8, 8, 1, 9], 3],
        [[9, 4, 2, 10, 7, 8, 8, 1, 9], 5],
        [[9, 4, 2, 1, 7, 8, 8, 1, 9, 7], 4],
        [[9, 4, 2, 1, 7, 8, 8, 1, 9, 7, 7], 4],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxTurbulenceSize(t[0])
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
