# 1296. Divide Array in Sets of K Consecutive Numbers
# 🟠 Medium
#
# https://leetcode.com/problems/hand-of-straights/
#
# Tags: Array - Hash Table - Greedy - Sorting

import timeit
from collections import Counter
from typing import List

# Note: This question is the same as Leetcode 846. Hand of Straights.

# This problem is also similar to LeetCode 659. Split Array into
# Consecutive Subsequences, we can try a similar approach using a
# frequencies dictionary and greedily trying to build the sequences
# of length k.
#
# Time complexity: O(n*log(n)) - Sorting has the biggest complexity,
# then we visit each card a maximum of two times for O(n).
# Space complexity: O(n) - The frequencies dictionary.
#
# Runtime: 815 ms, faster than 27.94%
# Memory Usage: 31.4 MB, less than 59.35%
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # Sorting the input we make sure we visit smaller values first.
        nums.sort()
        # Store the frequencies of the elements we have available.
        available = Counter(nums)
        # Iterate over the sorted input and try to build a sequence of
        # length k.
        for num in nums:
            # Check if we have used all the elements of that value already.
            if available[num] <= 0:
                continue
            # We have, at least, one element of this value available,
            # try to build a sequence starting at this element.
            for i in range(k):
                val = num + i
                # If we are missing any of the elements to build this
                # sequence, we have failed already.
                if available[val] <= 0:
                    return False
                # Register the fact that we are using one element of
                # this value.
                available[val] -= 1
        # If we manage to place all elements in sequences, we succeeded.
        return True


def test():
    executors = [Solution]
    tests = [
        [[1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True],
        [[1, 2, 3, 4, 5], 4, False],
        [[1, 2, 3, 3, 4, 4, 5, 6], 4, True],
        [[3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3, True],
        [[1, 2, 3, 4], 3, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.isPossibleDivide(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
