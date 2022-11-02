# 967. Numbers With Same Consecutive Differences
# 🟠 Medium
#
# https://leetcode.com/problems/problem-name/
#
# Tags: Backtracking - Breadth-First Search

import timeit
from collections import deque
from typing import List


# Treat each digit as a level of BFS, on each level, visit each element
# and add to the next level 0, 1 or 2 combinations of that element with
# a new digit with differences +k and -k appended to it.
#
# When When 1 <= k <=4:
# Time complexity: O(2^n) - On each level we may end up with twice the
# number of elements that we had in the previous level.
# Space complexity: O(2^n) - The deque may grow to that size, even if we
# don't take into account the input and output, the deque is not
# the real output because we are casting to list.
#
# # When When k == 0 or k > 4:
# Time complexity: O(n) - Each level will only have one element, because
# no matter the value of the last digit, there will be only one valid
# digit that we can add to it.
# Space complexity: O(n) - Any level can have a maximum of 9 elements,
# in fact, the number of elements will tend to decrease with bigger
# values of n and k.
#
# Runtime: 31 ms, faster than 99.67%
# Memory Usage: 14.2 MB, less than 73.75%
class IterativeBFS:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # Base case, length 0.
        if n == 0:
            return []
        # There cannot be any leading 0s, root level is 1..9
        level = [x for x in range(1, 10)]
        # Base case, length 1.
        if n == 1:
            return level
        # If we are going to have multiple levels, use a deque.
        level = deque(level)
        # We have 1 digit, add the rest up to n.
        for _ in range(2, n + 1):
            # For each element in the previous level.
            for _ in range(len(level)):
                el = level.popleft()
                # Get the last digit.
                last_digit = el % 10
                # Compute once the product of element * 10.
                prod = el * 10
                # Check if the digit - k results in a valid digit.
                down = last_digit - k
                if down >= 0:
                    # Append that number to the next level.
                    level.append(prod + down)
                # Check if the digit + k results in a valid digit.
                # Also check that k is not 0, when k is 0 we just need
                # to append the same digit and we did that already.
                up = last_digit + k
                if k and up <= 9:
                    level.append(prod + up)
        # The last level computed contains all the combinations of size n.
        return list(level)


# Use Set comprehension to shorten the code in the previous solution.
# Time and space complexity remain the same.
#
# Runtime: 71 ms, faster than 41.53%
# Memory Usage: 14.1 MB, less than 94.35%
class ItBFSetComp:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # First level is 1..9
        level = range(1, 10)
        # As many levels as digits (n) counting the first level we
        # already filled. Iterate over the levels.
        for _ in range(n - 1):
            # For each element in the current level, try to append
            # the two digits that have an absolute difference k with the
            # last digit if they are valid.
            level = {
                prev * 10 + new_digit
                for prev in level
                for new_digit in [prev % 10 + k, prev % 10 - k]
                if 0 <= new_digit <= 9
            }
        # Cast the set to list.
        return list(level)


def test():
    executors = [
        IterativeBFS,
        ItBFSetComp,
    ]
    tests = [
        [4, 8, [1919, 8080, 9191]],
        [3, 7, [181, 292, 707, 818, 929]],
        [1, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]],
        [2, 0, [11, 22, 33, 44, 55, 66, 77, 88, 99]],
        [
            2,
            1,
            [
                10,
                12,
                21,
                23,
                32,
                34,
                43,
                45,
                54,
                56,
                65,
                67,
                76,
                78,
                87,
                89,
                98,
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numsSameConsecDiff(t[0], t[1])
                # Sorting is needed because the set comprehension
                # solution does not preserve order.
                result.sort()
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
