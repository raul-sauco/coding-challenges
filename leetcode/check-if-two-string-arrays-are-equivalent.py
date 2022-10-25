# 1662. Check If Two String Arrays are Equivalent
# 🟢 Easy
#
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
#
# Tags: Array - String

import timeit
from collections.abc import Generator
from itertools import chain, zip_longest
from typing import List


# Convert the arrays to strings using join() then compare them.
#
# Time complexity: O(m+n) - The sum of the length of each string.
# Space complexity: O(m+n) - The strings that we cast the arrays to.
#
# Runtime: 61 ms, faster than 46.31%
# Memory Usage: 13.9 MB, less than 75.82%
class Naive:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


# We can improve on the previous solution by defining a generator
# function that produces the characters of a given List[str] in order.
#
# Time complexity: O(min(m, n)) - The algorithm will run at most the
# length of the shorter input counting characters.
# Space complexity: O(1) - No extra space is used, the generator does
# not store all values in memory but only uses a constant amount of
# memory.
#
# Runtime: 62 ms, faster than 43.12%
# Memory Usage: 13.9 MB, less than 33.11%
class UseGenerator:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Define a helper function to help iterate over the inputs.
        def getChars(arr: List[str]) -> Generator[str, None]:
            for chars in arr:
                for char in chars:
                    yield char
            # Mark the end of the stream.
            yield None

        return all(a == b for a, b in zip(getChars(word1), getChars(word2)))


# We can improve even further using one of the functions in the
# itertools package instead of defining our own.
#
# Time complexity: O(max(m, n)) - The algorithm will run at most the
# length of the longest input counting characters.
# Space complexity: O(1) - No extra space is used, the generator does
# not store all values in memory but only uses a constant amount of
# memory.
#
# Runtime: 57 ms, faster than 58.20%
# Memory Usage: 13.9 MB, less than 33.11%
class BuiltInFn:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return all(
            a == b
            for a, b in zip_longest(
                chain.from_iterable(word1), chain.from_iterable(word2)
            )
        )


def test():
    executors = [
        Naive,
        UseGenerator,
        BuiltInFn,
    ]
    tests = [
        [["ab", "c"], ["a", "bc"], True],
        [["a", "cb"], ["a", "c"], False],
        [["a", "cb"], ["ab", "c"], False],
        [["abc", "d", "defg"], ["abcddefg"], True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.arrayStringsAreEqual(t[0], t[1])
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
