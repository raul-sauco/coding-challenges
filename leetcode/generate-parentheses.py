# 22. Generate Parentheses
# 🟠 Medium
#
# https://leetcode.com/problems/generate-parentheses/
#
# Tags: String - Dynamic Programming - Backtracking

import timeit
from typing import List


# Iterate over the number of parentheses to generate, at each level,
# take 1 or 2 branches depending which ones are available, opening a
# parentheses, closing it or both.
#
# Time complexity: O(2^n) - Where n is the number of parentheses to
# generate.
# Space complexity: O(n) - The number of parentheses that will be
# generated.
#
# Runtime: 41 ms, faster than 86.12%
# Memory Usage: 14.2 MB, less than 76.89%
class BackTrack:
    def generateParenthesis(self, n: int) -> List[str]:
        # Store the result in a list.
        res = []
        # Define a function that generates the next parentheses.
        def next(remaining: int, current: List[str], open: int):
            # Base case, no remaining parentheses to generate and all the
            # parentheses are closed.
            if not open and not remaining:
                res.append("".join(current))
            # If we need to generate more parentheses, one of the
            # branches will be adding an opening parentheses.
            if remaining:
                current.append("(")
                next(remaining - 1, current, open + 1)
                # Backtrack
                current.pop()
            # If we have unclosed parentheses, one of the branches will
            # be to close one of them.
            if open:
                current.append(")")
                next(remaining, current, open - 1)
                # Backtrack
                current.pop()

        # Initial call
        next(n, [], 0)
        return res


def test():
    executors = [BackTrack]
    tests = [
        [1, ["()"]],
        [3, ["((()))", "(()())", "(())()", "()(())", "()()()"]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.generateParenthesis(t[0])
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
