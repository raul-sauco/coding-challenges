# 2444. Count Subarrays With Fixed Bounds
# 🔴 Hard
#
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
#
# Tags: Array - Queue - Sliding Window - Monotonic Queue

import timeit
from typing import List


# The most brute force solution picks every combination of start and end
# indexes and iterates over all the elements between the indexes to
# check if the array has fixed bounds.
#
# Time complexity: O(n^3) - Three nested loops.
# Space complexity: O(1) - Constant extra memory.
class BruteForce:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res, n = 0, len(nums)
        for l in range(n):
            for r in range(l, n):
                # Iterate over the array l..r and check if each element
                # is within bounds and if there is at least one min and
                # one max values.
                found_min = found_max = False
                for num in nums[l : r + 1]:
                    # As soon as we find a value out of bounds we break.
                    if not minK <= num <= maxK:
                        break
                    if num == minK:
                        found_min = True
                    if num == maxK:
                        found_max = True
                else:
                    if found_min and found_max:
                        res += 1
        return res


# The key observation to make is that out of bounds elements cannot
# belong to any subarray, we can split the input into subarrays that
# could be subarrays with fixed bounds. If we keep track of the indexes
# of the last time that we saw an out of bounds value, a max and a min
# values, we can compute the number of subarrays in O(1) from any index.
#
# Time complexity: O(n) - We iterate over the elements one time and do
# constant time work for each.
# Space complexity: O(1) - The algorithm uses constant extra memory.
#
# Runtime 871 ms Beats 83.60%
# Memory 28.5 MB Beats 69.75%
class SlidingWindow:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Initialize the last max, min and out of bounds values seen.
        last_max = last_min = last_oob = -1
        # Initialize the result.
        res = 0
        for i, num in enumerate(nums):
            # Update the last seen values with the current value.
            if not minK <= num <= maxK:
                last_oob = i
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i
            # How many valid arrays can we build that end at index i?
            # - We need to include one max and one min, the furthest
            #   right we can go is the furthest left between the last
            #   max and min: min(last_min, last_max)
            # - We cannot include any out of bounds values, the furthest
            #   left we can go in last_oob + 1
            # - We can pick any index between these values, that is
            #   min(last_min, last_max) - last_oob if that is a positive
            #   value, or 0 if the last out bounds is further left than
            #   one or both of last_max or last_min.
            res += max(0, min(last_min, last_max) - last_oob)
        return res


def test():
    executors = [
        BruteForce,
        SlidingWindow,
    ]
    tests = [
        [[1, 1, 1, 1], 1, 1, 10],
        [[1, 3, 5, 2, 7, 5], 1, 5, 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.countSubarrays(t[0], t[1], t[2])
                exp = t[3]
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
