# 2306. Naming a Company
# 🔴 Hard
#
# https://leetcode.com/problems/naming-a-company/
#
# Tags: Array - Hash Table - String - Bit Manipulation - Enumeration

import string
import timeit
from typing import List


# The naive solution does literally what the problem tells it to do, it
# iterates over every pair of words, switches their first characters and
# checks to see if any of the resulting words is already in the input.
#
# Time complexity: O(n^2) - We check every pair of words, for each, we
# swap their characters and hash them, but word length is limited to 10
# characters, so O(1) work.
# Space complexity: O(n) - The set that we use to check if a word is
# part of the input has the same size as the input.
#
# This solution fails with TLE.
class Naive:
    def distinctNames(self, ideas: List[str]) -> int:
        # Naive approach with O(n^2) time complexity.
        not_allowed = set(ideas)
        count, n = 0, len(ideas)
        for i in range(n):
            for j in range(i + 1, n):
                w1 = ideas[i][0] + ideas[j][1:]
                w2 = ideas[j][0] + ideas[i][1:]
                if w1 not in not_allowed and w2 not in not_allowed:
                    count += 2
        return count


# This solution is based in two observations, words with the same first
# letters can never be combined amongst themselves, because they would
# not change and therefore are guaranteed to be in the input, we can
# put all words with the same characters into sets. Then we iterate over
# each pair of sets, check how many word suffixes are common between
# both sets, because they will also result in an existing word, and
# compute the number of ways to combine suffixes that are not common
# between themselves.
#
# Time complexity: O(n) - We visit each word to build the dictionary,
# then iterate over the characters that we use as keys for the
# dictionary using a nested loop at O(26^2)≈O(1). Inside each of the 26^2
# loops we compute the intersection of sets, which overall can be at most
# O(n) work because that is the number of words in the combined sets,
# and do some math with the length of the sets and their intersection
# at O(1).
# Space complexity: O(n) - The dictionary contains all characters in the
# input.
#
# Runtime 548 ms Beats 96.77%
# Memory 28.5 MB Beats 58.6%
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # The keys that we will use for the dictionary and to iterate
        # over our keys later.
        chars = string.ascii_lowercase
        # Words with the same first character can never be combined.
        d = {c: set() for c in chars}
        for idea in ideas:
            d[idea[0]].add(idea[1:])

        # The count of words we can form.
        count = 0
        for i in range(len(chars) - 1):
            # Skip empty keys
            w1 = d[chars[i]]
            if not w1:
                continue
            for j in range(i + 1, len(chars)):
                w2 = d[chars[j]]
                # Count the number of suffixes common to both sets.
                common = len(w1 & w2)
                # Add the number of combinations that we can do.
                count += 2 * (len(w1) - common) * (len(w2) - common)
        return count


def test():
    executors = [
        Naive,
        Solution,
    ]
    tests = [
        [["lack", "back"], 0],
        [["coffee", "donuts", "time", "toffee"], 6],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.distinctNames(t[0])
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
