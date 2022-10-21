# 219. Contains Duplicate II
# 🟢 Easy
#
# https://leetcode.com/problems/contains-duplicate-ii/
#
# Tags: Array - Hash Table - Sliding Window

import timeit
from typing import List


# We can keep values that we have seen in a hash map with their index
# as a value, we iterate over the entire input checking if the index of
# the last time we saw the same value is within range.
#
# Time complexity: O(n) - We process each element once.
# Space complexity: O(n) - The hashmap can grow to the same size as the
# input.
#
# Runtime: 1361 ms, faster than 49.15%
# Memory Usage: 27.2 MB, less than 53.63%
class HashMapAndDiff:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # A dictionary of values pointing to the last index
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            # We can safely overwrite the last index of i because we
            # only care about the smallest difference.
            seen[num] = i
        return False


# If len(nums) is much greater than k, we can optimize but only keeping
# a sliding window of k values in the seen set.
#
# Time complexity: O(n) - We process each element once.
# Space complexity: O(k) - The hash set can grow to size k.
#
# Runtime: 707 ms, faster than 83.95%
# Memory Usage: 25.6 MB, less than 87.40%
class SlidingWindow:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Base case, with k == 0, we can't have duplicates.
        if not k:
            return False
        seen = set()
        l = r = 0
        while r < len(nums):
            # If this value is in the set, we are done.
            if nums[r] in seen:
                return True
            # Add the value under the right pointer, then shift it.
            seen.add(nums[r])
            r += 1
            # If the set has reached full capacity move the left pointer
            # and pop its value.
            if len(seen) > k:
                seen.remove(nums[l])
                l += 1
        return False


def test():
    executors = [
        HashMapAndDiff,
        SlidingWindow,
    ]
    tests = [
        [[1], 3, False],
        [[1, 1], 1, True],
        [[1, 1], 0, False],
        [[1, 0, 1, 1], 1, True],
        [[1, 2, 3, 1], 3, True],
        [[1, 2, 3, 1, 2, 3], 2, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.containsNearbyDuplicate(t[0], t[1])
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
