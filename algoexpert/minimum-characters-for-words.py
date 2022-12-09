# Minimum Characters For Words
# 🟠 Medium
#
# https://www.algoexpert.io/questions/minimum-characters-for-words
#
# Tags: String

import timeit
from collections import Counter


# This is a template that can be used as the starting point of a
# solution with minimal changes.
class Solution:
    def minimumCharactersForWords(self, words):
        if not words:
            return []
        counts = Counter(words[0])
        for word in words:
            counts |= Counter(word)
        res = []
        for char, count in counts.items():
            for _ in range(count):
                res.append(char)
        return res


def test():
    executors = [Solution]
    tests = [
        [["a", "abc", "ab", "boo"], ["a", "b", "c", "o", "o"]],
        [["cta", "cat", "tca", "tac", "a", "c", "t"], ["a", "c", "t"]],
        [
            ["this", "that", "did", "deed", "them!", "a"],
            ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minimumCharactersForWords(t[0])
                exp = t[1]
                result.sort()
                exp.sort()
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
