# 131. Palindrome Partitioning
# 🟠 Medium
#
# https://leetcode.com/problems/palindrome-partitioning/
#
# Tags: String - Dynamic Programming - Backtracking

import timeit
from typing import List

# Classic backtracking solution, for each index, we try all string
# prefixes to see if they are a palindrome, if they are, we use them to
# build one of the solutions (one of the ways to partition the input
# string) and keep building starting at the first unused index.
#
# Time complexity: O(n*2^n) - The decision tree splits in 2 at each
# level, and there are n levels where n is the number of characters in
# the input string. At each call, we iterate over all characters in
# the substring, which could also be n, to check if the substring is
# a palindrome.
# Space complexity: O(n) - The height of the call stack, if we take into
# consideration the result, then n^2 which is the possible number of
# palindromes.
#
# Runtime 658 ms Beats 85.74%
# Memory 30.3 MB Beats 47.4%
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, current = [], []
        # The first index that we need to look into.
        def bt(idx: int) -> None:
            if idx == len(s):
                res.append(current[:])
            # Try to form palindromes of all lengths starting at the
            # given index.
            for i in range(idx, len(s)):
                # Try to form a palindrome with i + 1 characters.
                sub = s[idx : i + 1]
                # If this substring is not a palindrome, ignore it.
                if sub == sub[::-1]:
                    current.append(sub)
                    bt(i + 1)
                    current.pop()

        bt(0)
        return res


def test():
    executors = [Solution]
    tests = [
        ["a", [["a"]]],
        ["aab", [["a", "a", "b"], ["aa", "b"]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.partition(t[0])
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
