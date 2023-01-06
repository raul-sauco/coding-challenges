# One Edit
# 🟠 Medium
#
# https://www.algoexpert.io/questions/one-edit
#
# Tags: String - Two Pointers

import timeit


# Determine which string is longer, if any, and start iterating over all
# the indexes in both of them at the same time, if we find a character
# that is not the same in both strings, we consume one edit and keep
# checking the characters after the edit.
#
# Time complexity: O(n) - Where n is the length of either string, if
# the lengths differ by more than 1 the algorithm will stop in O(1).
# Space complexity: O(1) - Only constant extra memory is used.
class Solution:
    def oneEdit(self, stringOne, stringTwo):
        short, long = stringOne, stringTwo
        if len(short) > len(long):
            short, long = long, short
        # The difference between the strings is too much.
        if len(long) - len(short) > 1:
            return False
        i = j = 0
        # The remaining number of edits.
        edits = 1
        while i < len(short) and j < len(long):
            if short[i] == long[j]:
                i += 1
            # The characters at the current indexes do not match.
            else:
                # We don't have any edits left.
                if not edits:
                    return False
                # We have edits, consume one.
                edits -= 1
                # The strings are the same length, replace this character.
                if len(short) == len(long):
                    i += 1
            # Always move the pointer in the longer string.
            j += 1
        return True


def test():
    executors = [Solution]
    tests = [
        ["a", "a", True],
        ["ab", "a", True],
        ["ab", "c", False],
        ["abcde", "acde", True],
        ["abccde", "abcde", True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.oneEdit(t[0], t[1])
                exp = t[2]
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
