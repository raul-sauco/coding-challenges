# 2390. Removing Stars From a String
# 🟠 Medium
#
# https://leetcode.com/problems/removing-stars-from-a-string/
#
# Tags: String - Stack - Simulation

import timeit


# Use a stack to build the result, iterate over the characters in the
# input, when we see a '*', pop the last character from the stack, any
# other character, we push into the stack. Since Strings in Rust are
# mutable, we can use a String as our stack and return that directly.
#
# Time complexity: O(n) - We visit all characters in the input string
# and do O(1) work for each.
# Space complexity: O(n) - The stack grows in size linearly with the input.
#
# Runtime 207 ms Beats 98.50%
# Memory 15.5 MB Beats 77.42%
class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for c in s:
            if c == "*":
                res.pop()
            else:
                res.append(c)
        return "".join(res)


def test():
    executors = [Solution]
    tests = [
        ["erase*****", ""],
        ["leet**cod*e", "lecoe"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.removeStars(t[0])
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
