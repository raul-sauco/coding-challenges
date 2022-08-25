# 383. Ransom Note
# 🟢 Easy
#
# https://leetcode.com/problems/ransom-note/
#
# Tags: Hash Table - String - Counting

import timeit
from collections import Counter


# Count the character frequencies in the magazine, iterate over the
# characters in the ransom note, subtracting the character from the
# available pool. Make sure that all characters in the ransom note are
# available.
#
# Time complexity: O(n) - Where n is the number of characters in both
# inputs.
# Space complexity: O(n) - Where n is the number of characters in both
# inputs.
#
# Runtime: 73 ms, faster than 73.69%
# Memory Usage: 14.1 MB, less than 53.79%
class Iterative:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Get a count of characters in the magazine.
        available = Counter(magazine)
        # Iterate over the characters in he ransom note making sure that
        # the character is still available.
        for c in ransomNote:
            # Make sure the character is still available.
            if c not in available or not available[c]:
                return False
            # "use" one of this character.
            available[c] -= 1
        # If all the characters were available, we can compose the
        # ransom note.
        return True


# Use two counters, subtract the frequencies on the magazine from the
# frequencies on the ransom note, the result should be an empty
# counter because counter behaves as a multiset for the difference.
#
# Time complexity: O(n) - Where n is the number of characters in both
# inputs.
# Space complexity: O(n) - Where n is the number of characters in both
# inputs.
#
# Runtime: 66 ms, faster than 81.97%
# Memory Usage: 14.2 MB, less than 20.43%
class TwoCounters:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)


# We can optimize the counter solution using the set & operation instead
# of the difference.
#
# Time complexity: O(n) - Where n is the number of characters in both
# inputs.
# Space complexity: O(n) - Where n is the number of characters in both
# inputs.
#
# Runtime: 49 ms, faster than 95.47%
# Memory Usage: 14.2 MB, less than 53.79%
class CounterAnd:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_freq = Counter(ransomNote)
        return note_freq & Counter(magazine) == note_freq


def test():
    executors = [
        Iterative,
        TwoCounters,
        CounterAnd,
    ]
    tests = [
        ["a", "", False],
        ["a", "b", False],
        ["aa", "ab", False],
        ["aa", "aab", True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.canConstruct(t[0], t[1])
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
