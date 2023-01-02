# 520. Detect Capital
# 🟢 Easy
#
# https://leetcode.com/problems/detect-capital/
#
# Tags: String

import re
import timeit


# Runtime 32 ms Beats 88.30%
# Memory 14.2 MB Beats 8.93%
class Iterative:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        # If the first two characters are uppercase, everything else
        # also needs to be. If they aren't everything after the first
        # character needs to be lowercase.
        is_uppercase_word = word[0].isupper() and word[1].isupper()
        return all([c.isupper() == is_uppercase_word for c in word[1:]])


# Runtime 27 ms Beats 97.37%
# Memory 14.2 MB Beats 56.30%
class UseRegex:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)


def test():
    executors = [
        Iterative,
        UseRegex,
    ]
    tests = [
        ["a", True],
        ["A", True],
        ["ab", True],
        ["Ab", True],
        ["AB", True],
        ["aB", False],
        ["USA", True],
        ["Flag", True],
        ["FlaG", False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.detectCapitalUse(t[0])
                exp = t[1]
                # The regex solution returns a match object.
                assert bool(result) == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
