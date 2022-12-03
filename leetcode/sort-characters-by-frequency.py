# 451. Sort Characters By Frequency
# 🟠 Medium
#
# https://leetcode.com/problems/sort-characters-by-frequency/
#
# Tags: Hash Table - String - Sorting - Heap (Priority Queue)
# Bucket Sort - Counting

import timeit
from collections import Counter


# Count the frequency of each character, then the most_common method to
# get a list of tuples ordered by most common character first, use that
# list to build the output.
#
# Time complexity: O(k*log(k)+n) - Where k is the number of unique
# character frequencies and n is the number of characters in the input
# string. All characters need to be read from the input and wrote to the
# input in O(n), the frequencies need to be sorted in O(k*log(k)).
# Space complexity: O(k) - A counter with as many elements as unique
# frequencies there are in the input. Max 62 keys.
#
# Runtime: 73 ms, faster than 73.11%
# Memory Usage: 15.2 MB, less than 98.50%
class UseCounter:
    def frequencySort(self, s: str) -> str:
        return "".join(c * freq for c, freq in Counter(s).most_common())


# Use bucket sort to improve the time complexity, create an array of
# buckets where we place characters indexed by their frequency in the
# input string. Even the theoretical complexity of this solution is
# better, the previous one outperforms it because the key space is
# smaller. When we use a counter keyed by character, we have at most
# 26 + 26 + 10 = 62 keys, when we key by frequencies, the buckets array
# may be of length 10^5. O(k*log(k)) with k <= 62 outperforms O(n) with
# n <= 10^5 for big values of n.
#
# Time complexity: O(n) - We iterate over the entire length of the array
# three times.
# Space complexity: O(n) - The buckets array has the same length as the
# input. The counter can also be of the same size as the input for small
# inputs <= 62 with all unique characters.
#
# Runtime: 202 ms, faster than 7.89%
# Memory Usage: 23.8 MB, less than 7.96%
class BucketSort:
    def frequencySort(self, s: str) -> str:
        buckets = [[] for _ in range(len(s) + 1)]
        for key, value in Counter(s).items():
            buckets[value].append(key)
        return "".join(
            [i * c for i in reversed(range(len(buckets))) for c in buckets[i]]
        )


def test():
    executors = [
        UseCounter,
        BucketSort,
    ]
    tests = [
        ["eeeee", ("eeeee")],
        ["tree", ("eetr", "eert")],
        ["Aabb", ("bbAa", "bbaA")],
        ["cccaaa", ("aaaccc", "cccaaa")],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.frequencySort(t[0])
                exp = t[1]
                assert result in exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
