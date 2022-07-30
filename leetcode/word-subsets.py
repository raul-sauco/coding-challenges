# 916. Word Subsets
# 🟠 Medium
#
# https://leetcode.com/problems/word-subsets/
#
# Tags: Array - Hash Table - String

import timeit
from collections import Counter
from functools import reduce
from operator import or_
from typing import List


# Looking at the description, it seems like the best complexity we can
# try to achieve is O(n) since we will need to visit at least once, each
# character of the input.
# One observation that helps us, is that the length of the input words
# is restricted and, while there could be a high number of words, they
# are pretty short.
#
# 1 <= words1.length, words2.length <= 104
# 1 <= words1[i].length, words2[i].length <= 10
#
# We can take all the subsequences in words2 and build a dictionary of
# frequencies needed to be a universal word. Then check all words in
# word1 against that dictionary.
#
# Time complexity: O(n) - We visit each character in the input a
# constant number of times.
# Space complexity: O(1) - If we don't consider the input and output
# lists, we are only keeping the frequencies dictionary in memory, it
# has a max length of 10.
#
# Runtime: 1712 ms, faster than 26.01% of Python3 online submissions for
# Word Subsets.
# Memory Usage: 18.5 MB, less than 87.67% of Python3 online submissions
# for Word Subsets.
class CounterAndAll:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Build a dictionary of frequencies needed to be universal.
        # O(n) - n: combined number of characters in words2
        freq = Counter(words2[0])
        for word in words2[1:]:
            # Union of frequencies, preserves the maximum values for
            # each key in both counters.
            freq = freq | Counter(word)

        # Store the results in a list.
        res = []

        # Since the input words have a max length of 10, if we need more
        # than 10 characters to be a universal words, none of the input
        # words will match, return an empty set.
        if sum(freq.values()) > 10:
            return res

        # Iterate over the words in words1 checking them against the
        # frequencies dictionary.
        # O(1) - len(word1) <= 10
        for word in words1:
            wc = Counter(word)
            # For word to be a superset of all words in word2, it needs
            # to have the same of higher frequency for each entry in
            # the frequencies dictionary.
            # O(1) - len(freq) <= 10
            if all(wc[x] >= freq[x] for x in freq):
                res.append(word)

        return res


# Similar logic to the previous solution but using some Python magic.
# In this example, using built-in functions does not seem to improve
# performance.
#
# Runtime: 2493 ms, faster than 5.01% of Python3 online submissions for
# Word Subsets.
# Memory Usage: 18.6 MB, less than 54.67% of Python3 online submissions
# for Word Subsets.
class BuiltInFns:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Substitute the for loop and | operator for reduce and or_
        freq = reduce(or_, (Counter(w) for w in words2))
        # Substitute the if check and all() call for list comprehension
        # with an internal check.
        return [word for word in words1 if freq & Counter(word) == freq]


def test():
    executors = [CounterAndAll, BuiltInFns]
    tests = [
        [
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["eoo", "eo", "a", "b", "c", "k", "g"],
            [],
        ],
        [
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["eoo", "eo", "a", "b", "c", "k"],
            ["facebook"],
        ],
        [
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["e", "o"],
            ["facebook", "google", "leetcode"],
        ],
        [
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["l", "e"],
            ["apple", "google", "leetcode"],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.wordSubsets(t[0], t[1])
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
