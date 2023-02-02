# Smallest Substring Containing
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/smallest-substring-containing
#
# Tags: String - Sliding Window

import timeit
from collections import Counter


# Use a sliding window approach and a counter to keep track of the
# characters and their frequencies that we have inside the current
# window. We iterate over all possible values of the right pointer, when
# we see a character that belongs to small string, we decrease the
# frequency, the number of instances of that character that we are
# short, by one, when the frequency goes from 1 to 0, it means we are
# not missing that character any longer. When we have all characters,
# we record the current window and compare it with the smallest window
# found until then. Once done that, we start shrinking the window from
# the left, when we remove any character in the small string, we add one
# to the number of these characters that we need, if that frequency goes
# from 0 to 1, we add that character to the missing set, as soon as we
# are missing a character, we stop decreasing the window and start
# increasing it.
#
# Time complexity: O(m+n) - We iterate over all characters in the small
# and big string.
# Space complexity: O(n) - We store the frequencies of characters in the
# small string in a counter that could have one entry per character.
class Solution:
    def smallestSubstringContaining(self, bigString, smallString):
        # Base case, empty small string.
        if not smallString:
            return ""
        # Store the frequencies that we need.
        freq = Counter(smallString)
        # Characters for which we are missing at least one.
        missing = set(smallString)
        # The length and start index of the shortest substring found so
        # far that contains all characters in small.
        best = (float("inf"), -1)
        # The index of the left boundary.
        l = 0
        for r in range(len(bigString)):
            cr = bigString[r]
            # If the character under the right pointer is not one of the
            # characters in small string, keep moving.
            if cr not in freq:
                continue
            # cr is one of the characters in small string.
            freq[cr] -= 1
            # Remove characters from the missing set only when the
            # count of missing ones is exactly zero.
            if freq[cr] == 0:
                missing.remove(cr)
            # If at this point the missing set is empty, the substring
            # between l and r contains all required characters, start
            # shrinking the sliding window until we are missing some
            # character again.
            while not missing:
                # If this substring is smaller than any of the previous
                # ones that contained the character set of small string,
                # update the shortest substring data.
                size = r - l + 1
                if size < best[0]:
                    best = (size, l)
                # Get the character under the left pointer and advance
                # the pointer after.
                cl = bigString[l]
                l += 1
                # Record that we are removing one instance of this
                # character if it belongs to small string.
                if cl not in freq:
                    continue
                freq[cl] += 1
                # When a frequency goes from zero to one, and only then,
                # we add that character to the missing set.
                if freq[cl] == 1:
                    missing.add(cl)

        return bigString[best[1] : best[1] + best[0]] if best[1] != -1 else ""


def test():
    executors = [Solution]
    tests = [
        ["abcd$ef$axb$c$", "$$abf", "f$axb$"],
        ["abcd$ef$axb$$", "$$abf$", "f$axb$$"],
        ["abcdefghijklmnopqrstuvwxyz", "aajjttwwxxzz", ""],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.smallestSubstringContaining(t[0], t[1])
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
