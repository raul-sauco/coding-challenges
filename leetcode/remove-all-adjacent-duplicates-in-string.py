# 1047. Remove All Adjacent Duplicates In String
# 🟢 Easy
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
#
# Tags: String - Stack

import timeit


# Iterate over the input string's characters pushing them into a stack,
# before pushing them, we compare the current character with the top of
# the stack, if they are the same, we pop the top of the stack and not
# push the current character.
#
# Time complexity: O(n) - We visit each character once to assess it and
# a maximum of 2 times to push it into, and pop it from the stack.
# Space complexity: O(n) - The stack could grow to the same size as the
# input.
#
# Runtime: 70 ms, faster than 97.15%
# Memory Usage: 14.7 MB, less than 86.70%
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


def test():
    executors = [Solution]
    tests = [
        ["abbaca", "ca"],
        ["azxxzy", "ay"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.removeDuplicates(t[0])
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
