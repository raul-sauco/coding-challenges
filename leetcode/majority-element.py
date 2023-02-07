# 169. Majority Element
# 🟢 Easy
#
# https://leetcode.com/problems/majority-element/
#
# Tags: Array - Hash Table - Divide and Conquer - Sorting - Counting

import timeit
from collections import defaultdict
from typing import List


# The naive solution uses a hashmap to keep a count of the number of
# times that we have seen a given number, when that count becomes more
# than half the length of the input array, we return that value.
#
# Time complexity: O(n) - We visit each element once and do O(1) work.
# Space complexity: O(n) - We can end up with almost n/2 entries in the
# dictionary of frequencies.
#
# Runtime 178 ms Beats 48.64%
# Memory 15.6 MB Beats 27.36%
class Naive:
    def majorityElement(self, nums: List[int]) -> int:
        boundary = len(nums) // 2
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
            if freq[num] > boundary:
                return num
        raise Exception("This should never run")


# For the follow-up we can use the Boyer-Moore majority vote algorithm
# https://en.wikipedia.org/wiki/Boyer–Moore_majority_vote_algorithm
#
# Time complexity: O(n) - We visit each element once and do O(1) work.
# Space complexity: O(1) - We only store two pointers.
#
# Runtime 158 ms Beats 95.23%
# Memory 15.4 MB Beats 99.25%
class BoyerMoore:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


def test():
    executors = [
        Naive,
        BoyerMoore,
    ]
    tests = [
        [[3, 2, 3], 3],
        [[2, 2, 1, 1, 1, 2, 2], 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.majorityElement(t[0])
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
