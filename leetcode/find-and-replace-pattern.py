# 890. Find and Replace Pattern
# 🟠 Medium
#
# https://leetcode.com/problems/find-and-replace-pattern/
#
# Tags: Array - Hash Table - String

import timeit
from typing import List


# We need to visit each character of each string to check if they match
# the pattern, it seems like the best we can do is O(n) where n is the
# number of characters in the input.
#
# Time complexity: O(n) - With n the combined number of characters in
# the input strings, we may end up visiting each character in each one.
# Space complexity: O(n) - The result set could grow to the same size
# as the input.
#
# Runtime: 59 ms, faster than 32.35% of Python3 online submissions for
# Find and Replace Pattern.
# Memory Usage: 13.9 MB, less than 28.72% of Python3 online submissions
# for Find and Replace Pattern.
class TwoMaps:
    def findAndReplacePattern(
        self, words: List[str], pattern: str
    ) -> List[str]:
        # Create an empty list, we cannot initialize it because we do
        # not know the size of the output at this point.
        res = []
        # Map each character in the pattern with the first position we
        # see it at and store the mappings in a dictionary.
        pd = {}
        for i, c in enumerate(pattern):
            if c not in pd:
                pd[c] = i
        # Iterate over the input words checking that they match the
        # pattern.
        for word in words:
            # If the problem did not guarantee that all input words have
            # the same length as the pattern, we could quickly filter
            # words in O(1) checking their length against the pattern's
            # and skipping any words that differ.
            # if len(word) != len(pattern):
            #     continue

            # Mapping of the current word's characters to the pattern
            wd = {}
            # Flag wether the character matches.
            match = True
            # Visit each character in word matching its characters with
            # its index the first time we see it. Then check if the
            # indexes match the pattern's dictionary indexes.
            for i, c in enumerate(word):
                if c not in wd:
                    wd[c] = i
                # Check that the pattern and word characters match the
                # first index where we saw them.
                if pd[pattern[i]] != wd[c]:
                    match = False
                    break

            # Append matched words to the result set.
            if match:
                res.append(word)

        return res


# We can improve on the solution above using some built-in functions to
# execute the same logic.
#
# Time complexity: O(n) - With n the combined number of characters in
# the input strings, we may end up visiting each character in each one.
# Space complexity: O(n) - The memory usage could grow to the same size
# as the input.
#
# Running the LeetCode tests does not give the expected result, this
# code performs worst than the previous one, it is probably due to the
# values used for testing. My guess is that a high percentage of the
# test words are not a match, in that case, the previous solution should
# perform better because it will fail as soon as a character not match,
# without checking the rest of the word. This solution will process
# each character in each word before deciding that it is not a match,
# that is probably compensating the extra performance that we are
# getting from the C code.
#
# Runtime: 66 ms, faster than 16.78% of Python3 online submissions for
# Find and Replace Pattern.
# Memory Usage: 13.9 MB, less than 28.72% of Python3 online submissions
# for Find and Replace Pattern.
class TwoMapsZip:
    def findAndReplacePattern(
        self, words: List[str], pattern: str
    ) -> List[str]:
        # Define a function to check if our words match the patters.
        def match(word):
            # Use dictionaries and setdefault to match the characters in
            # the word to the ones in the pattern.
            wd, pd = {}, {}
            # Return wether each character of word could be substituted
            # with the corresponding character in pattern to give the
            # same result.
            return all(
                (wd.setdefault(a, b), pd.setdefault(b, a)) == (b, a)
                for a, b in zip(word, pattern)
            )

        # Use the filter iterator to return words that match.
        return list(filter(match, words))


def test():
    executors = [TwoMaps, TwoMapsZip]
    tests = [
        [["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb", ["mee", "aqq"]],
        [["a", "b", "c"], "a", ["a", "b", "c"]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findAndReplacePattern(t[0], t[1])
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
