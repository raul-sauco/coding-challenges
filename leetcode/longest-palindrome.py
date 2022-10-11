# 409. Longest Palindrome
# 🟢 Easy
#
# https://leetcode.com/problems/longest-palindrome/
#
# Tags: Hash Table - String - Greedy

import timeit
from collections import Counter, defaultdict


# Iterate over the characters storing them in a dictionary as we go,
# every time we find a pair, we add 2 to the result, only once, if we
# have an uneven number of characters, we add an extra 1 for the
# character in the middle of the palindrome.
#
# Time complexity: O(n)
# Space complexity: O(n) - For the dictionary.
#
# Runtime: 80 ms, faster than 5.54%
# Memory Usage: 13.8 MB, less than 97.88%
class Loop:
    def longestPalindrome(self, s: str) -> int:
        seen = defaultdict(int)
        # Flag to store whether we have any character in uneven numbers.
        seen_uneven = 0
        length = 0
        for c in s:
            seen[c] += 1
        for c in seen:
            # If any of the characters is in an uneven number,
            # we can build an uneven palindrome.
            if not seen_uneven and seen[c] % 2 == 1:
                seen_uneven = 1
            # Add 2 per each pair found, discarding other single
            # characters.
            length += seen[c] // 2 * 2
        return length + seen_uneven


# Use a counter to obtain character frequencies, then iterate over them
# adding 2 for each pair and 1, once, for a single character if found.
#
# Time complexity: O(n)
# Space complexity: O(n) - For the counter.
#
# Runtime: 62 ms, faster than 22.27%
# Memory Usage: 13.9 MB, less than 21.85%
class ColCounter:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        for char_count in Counter(s).values():
            length += char_count // 2
        length *= 2
        if length < len(s):
            return length + 1
        return length


# Nice idiomatic way to do the same as the previous solutions. Count
# character frequencies, then subtract the number of odd frequencies
# minus one.
#
# Time complexity: O(n)
# Space complexity: O(n) - For the counter.
#
# Runtime: 30 ms, faster than 97.72%
# Memory Usage: 13.8 MB, less than 66.77%
class CountOdds:
    def longestPalindrome(self, s: str) -> int:
        odds = sum(v & 1 for v in Counter(s).values())
        return len(s) - odds + bool(odds)


def test():
    executors = [
        Loop,
        CountOdds,
        ColCounter,
    ]
    tests = [
        ["a", 1],
        ["bb", 2],
        ["abccccdd", 7],
        ["abbccccdd", 9],
        ["aAbbccccdd", 9],
        ["aAAbbccccdd", 11],
        ["aaAAbbccccdd", 12],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.longestPalindrome(t[0])
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
