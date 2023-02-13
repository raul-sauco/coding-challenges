# 217. Contains Duplicate
# 🟢 Easy
#
# https://leetcode.com/problems/contains-duplicate/
#
# Tags: Array - Hash Table - Sorting


import timeit
from typing import List


# Use a hash table to store values that we have seen, if we see a value
# that is already in the hash table, we have found a duplicate.
#
# Time complexity: O(n) - We could end up visiting each value, for each,
# we do O(1) work.
# Space complexity: O(n) - The hash set could grow to the size of the
# input.
#
# Runtime 514 ms Beats 73.16%
# Memory 26 MB Beats 71.69%
class HashSetCheck:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False


# Convert the input to a hash set, if the length remains the same, there
# are no duplicates.
#
# Time complexity: O(n) - We could end up visiting each value, for each,
# we do O(1) work.
# Space complexity: O(n) - The hash set could grow to the size of the
# input.
#
# Runtime 599 ms Beats 27.99%
# Memory 26.9 MB Beats 21.34%
class HashSetConversion:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not (len(nums) == len(set(nums)))


def test():
    executors = [
        HashSetCheck,
        HashSetConversion,
    ]
    tests = [
        [[1, 2, 3, 1], True],
        [[1, 2, 3, 4], False],
        [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.containsDuplicate(t[0])
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
