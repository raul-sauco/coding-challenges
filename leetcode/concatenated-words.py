# 472. Concatenated Words
# 🔴 Hard
#
# https://leetcode.com/problems/concatenated-words/
#
# Tags: Array - String - Dynamic Programming - Depth-First Search - Trie

import timeit
from collections import defaultdict
from typing import List


# We can create a dictionary of words keyed by their lengths, then we
# iterate over the input words, for any word that is long enough to be
# a concatenation of other words, we try to build by checking all the
# slices that are of a length that has an existing word, if the slice
# is found in the dictionary, we continue building, if we get to the
# end of the word, we have found that all its substrings are smaller
# words in the input.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input. We have to read all the characters to create the initial
# dictionary, then we sort the keys in O(k*log(k)) where k is the number
# of unique word lengths in the input and it is guaranteed to be less
# than n, then we iterate over all words taking slices and checking if
# the slices can be found in the dictionary, this is also O(n).
# Space complexity: O(n) - The dictionary holds all the characters in
# the input words.
#
# Runtime 338 ms Beats 93.87%
# Memory 21.4 MB Beats 64.2%
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # A dictionary of word lengths to words with that length. O(n)
        d = defaultdict(set)
        shortest_two = [31, 31]
        for w in words:
            l = len(w)
            d[l].add(w)
            if l < shortest_two[1]:
                shortest_two[1] = l
                if shortest_two[1] < shortest_two[0]:
                    shortest_two = shortest_two[::-1]
        # The minimum length a word needs to have to be considered.
        min_length_concat = sum(shortest_two)
        # The word lengths found in the input array.
        word_lengths = sorted(d.keys())
        res = set()

        def dfs(word: str, idx: int) -> None:
            # Base case, we have built the given word using other words
            # in the input.
            if idx == len(word):
                res.add(word)
                return
            # Find all the words that we could concatenate at this point
            # instead of trying all the words, use the length to slice
            # the target word and check if it exists in the set of the
            # given length.
            for length in word_lengths:
                # Do not bother using lengths that are too long to
                # concatenate with any others.
                if len(word) - word_lengths[0] < length:
                    break
                wanted = word[idx : idx + length]
                # If the substring is a word in the input and we have
                # not used yet in the current concatenation, use it.
                if wanted in d[length]:
                    dfs(word, idx + length)

        for w in words:
            # Skip words that are too short.
            if len(w) < min_length_concat:
                continue
            dfs(w, 0)
        return res


def test():
    executors = [Solution]
    tests = [
        [["cat", "dog", "catdog"], ["catdog"]],
        [
            [
                "cat",
                "cats",
                "catsdogcats",
                "dog",
                "dogcatsdog",
                "hippopotamuses",
                "rat",
                "ratcatdogcat",
            ],
            ["catsdogcats", "dogcatsdog", "ratcatdogcat"],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findAllConcatenatedWordsInADict(t[0])
                exp = set(t[1])
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
