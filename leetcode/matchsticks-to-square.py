# https://leetcode.com/problems/matchsticks-to-square/

# Tags: Array - Dynamic Programming - Backtracking - Bit Manipulation - Bitmask

import timeit
from typing import List

# Requirements:
# - we need to form a square
# - we need to use all matchsticks
# - we cannot break matchsticks into smaller pieces
#
# Reasoning:
# - we need to arrange the matchsticks into four groups
# - each group needs to be exactly one fourth of the length of all matchsticks together
#
# This is the k=4 version of:
# Problem 698: Partition to K Equal Sum Subsets
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
#
# Both these problems belong to the Bin Packing Problem class (https://en.wikipedia.org/wiki/Bin_packing_problem)
# and cannot be solved in polynomial time. There is a good post here:
# https://leetcode.com/discuss/general-discussion/1125779/Dynamic-programming-on-subsets-with-examples-explained
#
# TODO the leetcode solution uses a bit mask to keep track of which matchsticks have been used, instead of
# keeping the length of the sides that have been computed.

# DFS memoized with some optimizations to fail as soon as possible when the algorithm detects that it is
# not possible to build a solution from the current state.
#
# Time complexity, O(n*2^n)
# We can have len(matchsticks) * 4 ^ (len(matchsticks) / (min-length-matchstick))
# Space complexity O(n+2^n) we can have a call stack as deep as one branch of the
#
# Runtime: 9609 ms, faster than 5.05% of Python3 online submissions for Matchsticks to Square.
# Memory Usage: 366.3 MB, less than 5.04% of Python3 online submissions for Matchsticks to Square.
class MemoizedRecursive:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)

        # each side of the square needs to be a quarter of the perimeter
        target, remainder = divmod(perimeter, 4)

        # If the division by four is not an integer, we cannot solve the problem
        if len(matchsticks) < 4 or remainder != 0:
            return False

        # Store partial results in a memo
        memo = {}

        # Exploring bigger elements first speed cases when the result is negative
        matchsticks.sort(reverse=True)

        # Take a pointer to the list element that we need to process now and the length of the sides of the
        # square that we have built up to the moment and return whether we can build a square starting at
        # this state
        def dfs(idx: int, lengths: List[int]) -> bool:

            # We can index states based on the current element we are looking at and the length of the sides
            # independently of which side they are
            lengths.sort(reverse=True)
            key = tuple([idx] + lengths)

            if key in memo:
                return memo[key]

            # Iterate over the four possibilities that we have at the moment
            for side in range(4):
                updated_lengths = lengths.copy()
                updated_lengths[side] += matchsticks[idx]

                # If this side is already longer than the target, there is no need to continue
                if updated_lengths[side] > target:
                    continue

                # Check if we still have matchsticks we can use
                if idx + 1 < len(matchsticks):
                    # Recursive call, if any of the calls returns true, we can return true
                    if dfs(idx + 1, updated_lengths):
                        memo[key] = True
                        return True
                elif updated_lengths == [target for _ in range(4)]:
                    memo[key] = True
                    return True

            # If all the recursive calls return false, we cannot construct a square from this state
            memo[key] = False
            return False

        # Initial call
        return dfs(0, [0 for _ in range(4)])


def test():
    executors = [MemoizedRecursive]
    tests = [
        [[5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3], True],
        [[2, 2, 2], False],
        [[1, 2, 2, 2], False],
        [[1, 1, 2, 2, 2], True],
        [[3, 3, 3, 3, 4], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.makesquare(t[0])
                expected = t[1]
                assert (
                    result == expected
                ), f"\033[93m» {result} <> {expected}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
