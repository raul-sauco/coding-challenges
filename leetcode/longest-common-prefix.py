# 14. Longest Common Prefix
# 🟢 Easy
#
# https://leetcode.com/problems/longest-common-prefix/
#
# Tags: String

import timeit
from typing import List


# Iterate over the words checking how many characters match the longest
# prefix so far.
#
# Time complexity: O(n*m) - We could visit every string n in O(n) and,
# depending on the contents, could end up visiting each character in
# each of them m at O(n).
# Space complexity: O(m) - Prefix could grow to the size of m, for
# example if we only have one word.
#
# Runtime: 39 ms, faster than 85.87%
# Memory Usage: 14 MB, less than 49.70%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Strings has, at least, one word, if it is the only one, the
        # whole word will be the longest prefix.
        prefix = strs[0]
        # Iterate over the rest of the strings
        for string in strs[1:]:
            # Base cases, if any string is empty, or the prefix is
            # empty, return an empty prefix.
            if string == "" or prefix == "":
                return ""
            # Iterate over the length of the shortest of the two
            # checking which characters match.
            idx = 0
            limit = min(len(prefix), len(string))
            while idx < limit:
                # If the characters don't match, stop checking.
                if prefix[idx] == string[idx]:
                    idx += 1
                else:
                    break
            # Slice the prefix if the current match is shorter
            if idx < len(prefix):
                prefix = prefix[:idx]
        return prefix


def test():
    executors = [Solution]
    tests = [
        [["ab", "a"], "a"],
        [["flower", "flow", "flight"], "fl"],
        [["flower", "flow", "flight"], "fl"],
        [["dog", "racecar", "car"], ""],
        [["dogeared"], "dogeared"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.longestCommonPrefix(t[0])
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
