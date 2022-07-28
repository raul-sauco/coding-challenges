# 242. Valid Anagram
# 🟢 Easy
#
# https://leetcode.com/problems/valid-anagram/
#
# Tags: Hash Table - String - Sorting

import timeit
from collections import Counter, defaultdict

# 1e4 calls
# » Sorted              0.01574   seconds
# » DictionaryGet       0.02763   seconds
# » DefaultDictionary   0.03072   seconds
# » CollectionsCounter  0.03799   seconds
# » StringCount         0.04797   seconds

# Sort the strings and compare them. Anagrams will be the same string
# once sorted.
#
# Time complexity: O(n*log(n)) - For sorting.
# Space complexity: O(n) - Sorted returns a new string.
# We could reduce the space complexity to O(1) using to s.sort() to sort
# in-place and then compare the input, now sorted, strings.
#
# Runtime: 83 ms, faster than 34.87% of Python3 online submissions for
# Valid Anagram.
# Memory Usage: 15.1 MB, less than 11.43 % of Python3 online submissions
#  for Valid Anagram.
class Sorted:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# Solution using chars.get(c, 0) + 1
#
# Runtime: 78 ms, faster than 41.83% of Python3 online submissions for
# Valid Anagram.
# Memory Usage: 14.6 MB, less than 34.56 % of Python3 online submissions
#  for Valid Anagram.
class DictionaryGet:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        for w in t:
            if w not in chars:
                return False
            chars[w] -= 1
            if chars[w] == 0:
                del chars[w]
        return True


# Solution using defaultdict(int) and chars[0] += 1
#
# Runtime: 62 ms, faster than 68.39% of Python3 online submissions for
# Valid Anagram.
# Memory Usage: 14.3 MB, less than 96.95 % of Python3 online submissions
# for Valid Anagram.
class DefaultDictionary:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = defaultdict(int)
        for c in s:
            chars[c] += 1
        for w in t:
            if w not in chars:
                return False
            chars[w] -= 1
            if chars[w] == 0:
                del chars[w]
        return True


# Use collections.Counter, strings that have the same character
# frequency are anagrams.
#
# Runtime: 70 ms, faster than 54.35% of Python3 online submissions for
# Valid Anagram.
# Memory Usage: 14.5 MB, less than 34.56 % of Python3 online submissions
# for Valid Anagram.
class CollectionsCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Solution using string.count has a theoretical worst-case-scenario
# complexity of On^2 but it actually performs better on the LeetCode
# tests. I am not sure if this is due to the C implementation or the
# values that are being used on the tests, for example, if we fail with
# 'a' this test would run really fast.
#
# Time complexity: O(n^2)
# Space complexity: O(1)
#
# Runtime: 48 ms, faster than 91.87% of Python3 online submissions for
# Valid Anagram.
# Memory Usage: 14.4 MB, less than 96.95 % of Python3 online submissions
# for Valid Anagram.
class StringCount:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in "abcdefghijklmnopqrstuvwxyz":
            if s.count(c) != t.count(c):
                return False
        return True


def test():
    executors = [
        Sorted,
        DictionaryGet,
        DefaultDictionary,
        CollectionsCounter,
        StringCount,
    ]
    tests = [
        ["anagram", "nagaram", True],
        ["rat", "car", False],
        ["aacc", "cacc", False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isAnagram(t[0], t[1])
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
