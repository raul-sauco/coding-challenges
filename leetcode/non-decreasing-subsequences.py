# 491. Non-decreasing Subsequences
# 🟠 Medium
#
# https://leetcode.com/problems/non-decreasing-subsequences/
#
# Tags: Array - Hash Table - Backtracking - Bit Manipulation

import timeit
from typing import List

# 100 calls.
# input => [1..15]
# » Backtracking        1.2301    seconds
# » SetComprehension    1.26346   seconds
# input => [15..1]
# » Backtracking        0.00254   seconds
# » SetComprehension    0.00113   seconds

# The classic backtracking solution to sub-sequence type problems. Start
# at the first element of the array and split into two branches, one
# that uses it and one that skips it, for each element after that, we
# chose to skip it and keep building the sequence and, if its value does
# not break the non-decreasing property of the sequence, we create
# another branch that uses the element.
#
# Time complexity: O(n*2^n) - The decision tree splits in two at each
# level and it has a max of n levels, for each of the 2^n possible
# sequences, we iterate over all its elements, a max of n, to convert
# them into a tuple hash them and add them to the set.
# Space complexity: O(n*2^n) - The number of subsequences that could be
# in the set.
#
# Runtime 226 ms Beats 80.94%
# Memory 22.3 MB Beats 40.47%
class Backtracking:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def bt(idx: int, cur: List[int]) -> None:
            if idx == len(nums):
                # If the subsequence is not empty.
                if len(cur) > 1:
                    res.add(tuple(cur))
                return
            # Keep building the sequence that skips this number.
            bt(idx + 1, cur)
            # If this number preserves the non-decreasing property.
            if not cur or cur[-1] <= nums[idx]:
                # Add this number and keep building the sequence.
                cur.append(nums[idx])
                bt(idx + 1, cur)
                # Backtrack.
                cur.pop()

        bt(0, [])
        return res


# A pretty neat solution by StefanPochmann, it is faster than the
# previous solution, probably because using a set comprehension makes
# the logic run in C. It does run slower for local tests where the input
# array is an increasing sequence of numbers from 1 to 15.
# https://leetcode.com/problems/non-decreasing-subsequences/solutions/97127/
#
# Time complexity: O(n*2^n)
# Space complexity: O(n*2^n)
#
# Runtime 199 ms Beats 100%
# Memory 20.8 MB Beats 98.13%
class SetComprehension:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subs = {()}
        for num in nums:
            subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]


def test():
    executors = [
        Backtracking,
        SetComprehension,
    ]
    tests = [
        [[4, 4, 3, 2, 1], [[4, 4]]],
        [
            [4, 6, 7, 7],
            [
                [4, 6],
                [4, 6, 7],
                [4, 6, 7, 7],
                [4, 7],
                [4, 7, 7],
                [6, 7],
                [6, 7, 7],
                [7, 7],
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = set(sol.findSubsequences(t[0]))
                # Leetcode accepts an iterable of tuples.
                exp = set(map(tuple, t[1]))
                # assert result == exp, (
                #     f"\033[93m» {result} <> {exp}\033[91m for"
                #     + f" test {col} using \033[1m{executor.__name__}"
                # )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
