# 171. Excel Sheet Column Number
# 🟢 Easy
#
# https://leetcode.com/problems/excel-sheet-column-number/
#
# Tags: Math - String

import timeit


# Convert from base 26 to base 10, pop characters from the end of the
# input and convert them to the equivalent base 10 value adding it to
# the result.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input.
# Space complexity: O(n) - Where n is the number of characters in the
# input.
#
# Runtime 41 ms Beats 23.24%
# Memory 13.9 MB Beats 46.44%
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        chars, power, res = list(columnTitle), 1, 0
        while chars:
            res += (ord(chars.pop()) - ord("A") + 1) * power
            power *= 26
        return res


# Use an iterator, optionally wrapped in list comprehension, and the
# sum function to improve performance using c code to perform the
# operations.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input.
# Space complexity: O(n) - Where n is the number of characters in the
# input.
#
# Runtime 38 ms Beats 41.76%
# Memory 13.7 MB Beats 92.93%
class Solution2:
    def titleToNumber(self, columnTitle: str) -> int:
        # The version using an iterator has better memory usage but
        # worst time.
        # Runtime 38 ms Beats 41.76%
        # Memory 13.7 MB Beats 92.93%
        # return sum(
        #     (ord(c) - ord("A") + 1) * 26**i
        #     for i, c in enumerate(reversed(list(columnTitle)))
        # )
        # The version using list comprehension has worst memory usage
        # but better time.
        # Runtime 31 ms Beats 83.76%
        # Memory 13.8 MB Beats 46.44%
        return sum(
            [
                (ord(c) - ord("A") + 1) * 26**i
                for i, c in enumerate(reversed(list(columnTitle)))
            ]
        )


def test():
    executors = [
        Solution,
        Solution2,
    ]
    tests = [
        ["A", 1],
        ["AB", 28],
        ["ZY", 701],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.titleToNumber(t[0])
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
