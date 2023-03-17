# 168. Excel Sheet Column Title
# 🟢 Easy
#
# https://leetcode.com/problems/excel-sheet-column-title/
#
# Tags: Math - String

import timeit


# What the problem is asking is to convert from base 10 to base 26.
#
# Time complexity: O(log26(n)) - The loop will run until the value is 0
# and on each iteration we divide by 26.
# Space complexity: O(log26(n)) - We will have one character in the
# result string for each iteration of the loop.
#
# Runtime 22 ms Beats 97.71%
# Memory 13.8 MB Beats 45.8%
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Initialize the result and a
        res, val, offset = [], columnNumber, ord("A")
        while val:
            # Compensate for the values being 1-indexed.
            val -= 1
            val, mod = divmod(val, 26)
            res.append(chr(mod + offset))
        return "".join(reversed(res))


def test():
    executors = [Solution]
    tests = [
        [1, "A"],
        [28, "AB"],
        [701, "ZY"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.convertToTitle(t[0])
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
