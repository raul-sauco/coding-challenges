# First Non-Repeating Character
# 🟢 Easy
#
# https://www.algoexpert.io/questions/first-non-repeating-character
#
# Tags: String - Hash Map

import timeit
from collections import Counter


class Solution:
    def firstNonRepeatingCharacter(self, string: str) -> int:
        # Write your code here.
        freq = Counter(string)
        for i, c in enumerate(string):
            if freq[c] == 1:
                return i
        # There are not non-repeating characters.
        return -1


def test():
    executors = [Solution]
    tests = [
        ["abcdcaf", 1],
        ["faadabcbbebdf", 6],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.firstNonRepeatingCharacter(t[0])
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
