# 347. Top K Frequent Elements
# 🟠 Medium
#
# https://leetcode.com/problems/top-k-frequent-elements/
#
# Tags: Array - Hash Table - Divide and Conquer - Sorting
#  - Heap (Priority Queue) - Bucket Sort - Counting - Quickselect

import timeit
from collections import Counter, defaultdict
from typing import List


# Use the built-in Python Counter to count the elements and its
# `most_common(n)` method to get the k most frequent.
#
# Time complexity: O(n*log(n)) - Sorting the dictionary by value.
# Space complexity: O(n) - The size of the dictionary.
#
# Runtime 95 ms Beats 95.19%
# Memory Usage 18.4 Beats 99.66%
class UseCounter:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in Counter(nums).most_common(k)]


# Use bucket sorting, first get the frequency of items in the input,
# then create an array of buckets and place each unique value in the
# array indexed by its frequency. To create the result, iterate in
# reverse over the array indexes and pop elements until the result has
# grown to have k elements.
#
# Time complexity: O(n) - Sorting the dictionary by value.
# Space complexity: O(n) - The size of the dictionary.
#
# Runtime 104 ms Beats 71.15%
# Memory Usage 18.7 Beats 42.44%
class BucketSort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element, same as Counter(nums).
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        # A bucket that holds elements indexed by their frequency.
        bucket = []
        for num, count in freq.items():
            # Expand bucket if needed.
            while count + 1 > len(bucket):
                bucket.append(None)
            # If empty add a list at the index.
            if not bucket[count]:
                bucket[count] = []
            # Append the value indexed by its frequency.
            bucket[count].append(num)
        # Create a result of size k.
        res, idx = [], len(bucket) - 1
        while len(res) < k:
            if bucket[idx]:
                res.append(bucket[idx].pop())
            else:
                idx -= 1
        return res


def test():
    executors = [
        UseCounter,
        BucketSort,
    ]
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
