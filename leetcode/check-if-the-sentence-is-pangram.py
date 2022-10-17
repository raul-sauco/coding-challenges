# 1832. Check if the Sentence Is Pangram
# 🟢 Easy
#
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/
#
# Tags: Hash Table - String

import string
import timeit
from collections import Counter

# 10e4 calls
# » SetLength2          0.01077   seconds
# » SentenceSet         0.01606   seconds
# » CounterLength       0.02726   seconds
# » SetLength           0.03021   seconds

# Make a set out of the sentence, iterate over the characters in ascii
# lowercase checking if each of them is in sentence.
#
# Time complexity: O(n) - We need to visit each character in sentence to
# add it to the set.
# Space complexity: O(1) - The set maximum size is fixed to 26.
#
# Runtime: 40 ms, faster than 83.13%
# Memory Usage: 13.8 MB, less than 54.81%
class SentenceSet:
    def checkIfPangram(self, sentence: str) -> bool:
        have = set(sentence)
        for char in string.ascii_lowercase:
            if not char in have:
                return False
        return True


# Start iterating over sentence adding its characters to a set until we
# either arrive to the end of sentence or the set has size 26.
#
# Time complexity: O(n) - We could iterate over the entire input, but
# there is the probability that we would stop earlier, as soon as all
# the characters were found.
# Space complexity: O(1) - The set may only grow to size 26.
#
# Runtime: 30 ms, faster than 96.35%
# Memory Usage: 13.8 MB, less than 54.81%
class SetLength:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for c in sentence:
            seen.add(c)
            if len(seen) == 26:
                return True
        return False


# We can optimize the previous solution by eliminating any loops and
# checking the length of a set generated casting the input.
#
# Time complexity: O(n) - We could iterate over the entire input, but
# there is the probability that we would stop earlier, as soon as all
# the characters were found.
# Space complexity: O(1) - The set may only grow to size 26.
#
# Runtime: 33 ms, faster than 93.51%
# Memory Usage: 13.9 MB, less than 54.81%
class SetLength2:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


# Same logic as the previous solution but it seems like using a counter
# has more overhead.
#
# Time complexity: O(n) - We could iterate over the entire input, but
# there is the probability that we would stop earlier, as soon as all
# the characters were found.
# Space complexity: O(1) - The set may only grow to size 26.
#
# Runtime: 62 ms, faster than 33.73%
# Memory Usage: 13.9 MB, less than 54.81%
class CounterLength:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(Counter(sentence)) == 26


def test():
    executors = [
        SetLength2,
        SentenceSet,
        CounterLength,
        SetLength,
    ]
    tests = [
        ["", False],
        ["leetcode", False],
        ["thequickbrownfoxjumpsoverthelazydog", True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.checkIfPangram(t[0])
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
