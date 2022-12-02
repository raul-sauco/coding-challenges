# 1704. Determine if String Halves Are Alike
# 🟢 Easy
#
# https://leetcode.com/problems/determine-if-string-halves-are-alike/
#
# Tags: String - Counting

import timeit

# Count the number of vowels in each half of the string, return wether
# the count is the same.
#
# Time complexity: O(n) - We visit all elements in the input and perform
# O(1) operations.
# Space complexity: O(1) - We only use constant space.
#
# Runtime: 22 ms, faster than 99.90%
# Memory Usage: 13.9 MB, less than 33.40%
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l, r, balance, vowels = 0, len(s) - 1, 0, "aeiouAEIOU"
        while l < r:
            if s[l] in vowels:
                balance += 1
            if s[r] in vowels:
                balance -= 1
            l += 1
            r -= 1
        return balance == 0


def test():
    executors = [Solution]
    tests = [
        ["book", True],
        ["textbook", False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.halvesAreAlike(t[0])
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
