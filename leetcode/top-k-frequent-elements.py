# 347. Top K Frequent Elements
# 🟠 Medium
#
# https://leetcode.com/problems/top-k-frequent-elements/
#
# Tags: Array - Hash Table - Divide and Conquer - Sorting
#  - Heap (Priority Queue) - Bucket Sort - Counting - Quickselect

import timeit
from collections import Counter
from typing import List


# Use the built-in Python Counter to count the elements and its
# `most_common(n)` method to get the k most frequent.
#
# Time complexity: O(n*log(n)) - Sorting the dictionary by value.
# Space complexity: O(n) - The size of the dictionary.
#
# Runtime 95 ms Beats 95.19%
# Memory Usage 18.4 Beats 99.66%
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in Counter(nums).most_common(k)]


def test():
    executors = [Solution]
    tests = [
        [[1], 1, [1]],
        [[3, 0, 1, 0], 1, [0]],
        [[1, 1, 1, 2, 2, 3], 2, [1, 2]],
        [[1, 1, 1, 2, 2, 2, 2, 3], 3, [2, 1, 3]],
        [[1, 4, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 3], 3, [3, 2, 1]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.topKFrequent(t[0], t[1])
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
