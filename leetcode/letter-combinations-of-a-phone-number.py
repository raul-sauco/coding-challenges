# 17. Letter Combinations of a Phone Number
# 🟠 Medium
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#
# Tags: Hash Table - String - Backtracking

import timeit
from typing import List


# Runtime: 60 ms, faster than 31.39%
# Memory Usage: 13.8 MB, less than 79.23%
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Base case, return an empty list.
        if not digits:
            return []
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # Define a recursive function that adds the next letter to the
        # existing letters.
        def addNextLetter(i, current: List[str]) -> List[str]:
            # Base case, no more chars to add.
            if i == len(digits):
                return ["".join(current)]
            res = []
            for char in d[digits[i]]:
                # Add this char.
                current.append(char)
                # Recursive call
                res += addNextLetter(i + 1, current)
                # Backtrack
                current.pop()
            return res

        # Initial call
        return addNextLetter(0, [])


def test():
    executors = [Solution]
    tests = [
        ["", []],
        ["2", ["a", "b", "c"]],
        ["23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.letterCombinations(t[0])
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
