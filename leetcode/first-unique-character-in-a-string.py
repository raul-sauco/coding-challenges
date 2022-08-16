# 387. First Unique Character in a String
# 🟢 Easy
#
# https://leetcode.com/problems/first-unique-character-in-a-string/
#
# Tags: Hash Table - String - Queue - Counting

import timeit
from collections import Counter


# One pass to count character frequencies and one pass to find the
# first character that is unique in the string.
#
# Time complexity: O(n) - Two passes == O(2n) => O(n).
# Space complexity: O(1) - The counter has a max size of 26.
#
# Runtime: 160 ms, faster than 59.19%
# Memory Usage: 14.1 MB, less than 59.01%
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # One pass to count the character frequencies.
        freq = Counter(s)
        # Second pass to return the index of the first character with
        # frequency == 1.
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i
        # If no character had a frequency of 1, return -1
        return -1


# This solution runs faster because the work is being done by C code
# instead of a Python loop. If the code performing the work was both C
# or Python, it should be slower than the previous one.
#
# Time complexity: O(n)
# Space complexity: O(1) - For the set, max of 26 characters.
#
# Runtime: 70 ms, faster than 98.50%
# Memory Usage: 14.1 MB, less than 59.01%
class ListComprehension:
    def firstUniqChar(self, s: str) -> int:
        return min(
            [s.index(char) for char in set(s) if s.count(char) == 1] or [-1]
        )


def test():
    executors = [Solution]
    tests = [
        ["leetcode", 0],
        ["loveleetcode", 2],
        ["aabb", -1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.firstUniqChar(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
