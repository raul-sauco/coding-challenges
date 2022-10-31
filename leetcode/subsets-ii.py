# 90. Subsets II
# 🟠 Medium
#
# https://leetcode.com/problems/subsets-ii/
#
# Tags: Array - Backtracking - Bit Manipulation

import timeit
from collections import Counter
from typing import List

# 10e3 calls.
# » UseCounter          0.01731   seconds
# » BitFlags            0.03567   seconds
# » BitFlagsCompression 0.03502   seconds

# Count the number of unique digits, for each one, add it 0 to count
# times to the current result set.
#
# Time complexity: O(2^n) - The number of different subsets that we may
# need to generate.
# Space complexity: O(n) - Where n is the number of unique keys in the
# input. All data structures and the call stack will have that size. If
# we want to count the output array res, then O(2^n).
#
# Runtime: 59 ms, faster than 73.76%
# Memory Usage: 14.2 MB, less than 49.95%
class UseCounter:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        res = []
        # A list of the keys in the counter dictionary, this is also the
        # unique values on the input.
        keys = list(c.keys())

        def bt(i: int, s: List[int]) -> None:
            if i == len(keys):
                res.append(list(s))
                return
            num = keys[i]
            # Add 0..count times this number and call bt()
            for count in range(c[num] + 1):
                # Add this many instances of num.
                for _ in range(count):
                    s.append(num)
                bt(i + 1, s)
                for _ in range(count):
                    s.pop()

        bt(0, [])
        return res


# Use a binary string to mark the indexes of numbers that we have added
# to the set already. Sort the input to avoid having permutations and
# use a set of tuples to remove duplicate sets. An example of generated
# binary strings for n == 3 is:
#
# 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111
#
# Time complexity: O(2^n) - Trivial to see because we are looping over
# that range.
# Space complexity: O(2^n) - The number of unique sets if all values in
# the input were unique.
#
# Runtime: 95 ms, faster than 11.4%
# Memory Usage: 14.2 MB, less than 49.95%
class BitFlags:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort nums to avoid having different permutations.
        nums.sort()
        n = len(nums)
        res = set()
        # Use this range and slicing to avoid dealing with leading 0s
        # in the bitmask.
        for i in range(2**n, 2 ** (n + 1)):
            # Create the subset using the bitmask for this index.
            res.add(tuple(nums[j] for j in range(n) if bin(i)[3:][j] == "1"))
        return list(map(list, res))
        # On LeetCode there is no need to cast.
        # return res


# Similar logic but use set comprehension to build the result.
#
# Time complexity: O(2^n) - Trivial to see because we are looping over
# that range.
# Space complexity: O(2^n) - The number of unique sets if all values in
# the input were unique.
#
# Runtime: 62 ms, faster than 70.78%
# Memory Usage: 14.1 MB, less than 93.82%
class BitFlagsCompression:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort nums to avoid having different permutations.
        nums.sort()
        n = len(nums)
        return list(
            map(
                list,
                {
                    tuple(nums[j] for j in range(n) if bin(i)[3:][j] == "1")
                    for i in range(2**n, 2 ** (n + 1))
                },
            )
        )
        # On LeetCode there is no need to cast.
        # return {
        #     tuple(nums[j] for j in range(n) if bin(i)[3:][j] == "1")
        #     for i in range(2**n, 2 ** (n + 1))
        # }


def test():
    executors = [
        UseCounter,
        BitFlags,
        BitFlagsCompression,
    ]
    tests = [
        [[0], [[], [0]]],
        [[1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]],
        [
            [4, 4, 4, 1, 4],
            [
                [],
                [1],
                [1, 4],
                [1, 4, 4],
                [1, 4, 4, 4],
                [1, 4, 4, 4, 4],
                [4],
                [4, 4],
                [4, 4, 4],
                [4, 4, 4, 4],
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.subsetsWithDup(t[0])
                # Need to sort each item and the whole list.
                result = list(sorted(map(sorted, result)))
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
