# 1239. Maximum Length of a Concatenated String with Unique Characters
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
#
# Tags: Array - String - Backtracking - Bit Manipulation

import timeit
from typing import List, Set


# Cast all the input lists to sets removing any that have duplicate
# characters, since we will never be able to use them. Recursively
# explore the results of choosing to use, or not use, each of the
# resulting sets and return the length of the resulting group of
# characters keeping the best of them.
#
# Time complexity: O(1) - The recursive cost in O(2^n) where n is the
# length of the input array, but the problem guarantees that the input
# will be at most 16 sequences long. O(2^16) == O(1).
# Space complexity: O(1) - The call stack will have at most 16 calls,
# the set of used characters that we are passing will have, at most,
# 26 characters, the list of sets that we cast the input to will have
# at max 26*16 characters.
#
# Runtime: 86 ms, faster than 97.80%
# Memory Usage: 14.1 MB, less than 43.86%
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Cast the input lists into sets.
        sets = [set(chars) for chars in arr if len(set(chars)) == len(chars)]
        # Define a function that explores the recursive tree.
        # idx - is the index of the element of sets that we are exploring.
        # used - is a set of characters that we have decided to use.
        def dfs(idx: int, used: Set[str]) -> int:
            # If we have exhausted the input, return the current number
            # of characters used.
            if idx == len(sets):
                return len(used)
            # If using the set at the current index would not result in
            # duplicate characters, recursive call.
            if used & sets[idx]:
                using = 0
            else:
                # If we can use this set, add it and move to the next.
                using = dfs(idx + 1, used | sets[idx])
            # Return the best between using this chars and not.
            return max(dfs(idx + 1, used), using)

        # Initial call
        return dfs(0, set())


# Same as the previous solution but remove the comments and shorten
# the code inline some of the conditional checks.
class ShortCode:
    def maxLength(self, arr: List[str]) -> int:
        sets = [set(chars) for chars in arr if len(set(chars)) == len(chars)]

        def dfs(idx: int, used: Set[str]) -> int:
            return (
                max(
                    dfs(idx + 1, used),
                    dfs(idx + 1, used | sets[idx])
                    if not used & sets[idx]
                    else 0,
                )
                if idx < len(sets)
                else len(used)
            )

        return dfs(0, set())


def test():
    executors = [
        Solution,
        ShortCode,
    ]
    tests = [
        [["z"], 1],
        [["aa", "bb"], 0],
        [["un", "iq", "ue"], 4],
        [["cha", "r", "act", "ers"], 6],
        [["abcdefghijklmnopqrstuvwxyz"], 26],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxLength(t[0])
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
