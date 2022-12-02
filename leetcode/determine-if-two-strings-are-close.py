# 1657. Determine if Two Strings Are Close
# 🟠 Medium
#
# https://leetcode.com/problems/determine-if-two-strings-are-close/
#
# Tags: Hash Table - Sting - Sorting

import timeit
from collections import Counter


# The strings need to have the same unique characters, the same number
# of characters, length, and the same frequencies of groups of the same
# character. We don't need to check the input length, but speeds up by
# discarding in O(1) inputs where the strings have different lengths.
#
# Time complexity: O(n*log(n)) - Sorting the counter values has the
# highest complexity.
# Space complexity: O(n) - The counters could have the same size as the
# input strings.
#
# Runtime: 135 ms, faster than 99.60%
# Memory Usage: 15.4 MB, less than 16.80%
class Sorting:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return (
            len(word1) == len(word2)
            and set(word1) == set(word2)
            and sorted(Counter(word1).values())
            == sorted(Counter(word2).values())
        )


# Similar solution but, instead of sorting the character frequencies to
# compare them, we count them.
#
# Time complexity: O(n) - All the operations happen in linear time.
# Space complexity: O(n) - The counters could have the same size as the
# input strings.
#
# Runtime: 123 ms, faster than 99.60%
# Memory Usage: 15.1 MB, less than 80%
class Counting:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return (
            len(word1) == len(word2)
            and set(word1) == set(word2)
            and Counter(Counter(word1).values())
            == Counter(Counter(word2).values())
        )


def test():
    executors = [
        Sorting,
        Counting,
    ]
    tests = [
        ["a", "aa", False],
        ["abc", "bca", True],
        ["cabbba", "abbccc", True],
        ["abbzzca", "babzzcz", False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.closeStrings(t[0], t[1])
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
