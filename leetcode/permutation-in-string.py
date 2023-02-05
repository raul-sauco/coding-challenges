# 567. Permutation in String
# 🟠 Medium
#
# https://leetcode.com/problems/permutation-in-string/
#
# Tags: Hash Table - Two Pointers - String - Sliding Window

import timeit
from collections import defaultdict


# A very similar problem to LeetCode 438. Find All Anagrams in a String.
# We can use the same technique: use a hashmap to keep track of
# characters that we need vs characters we have seen, negative values
# denote characters in s1 that we haven't found in s2 yet, positive
# values denote characters that we have seen in s2 but aren't, or not in
# the same frequency, in s1. When we have the same frequency of the same
# character, we remove the entry from the dictionary. We use a sliding
# window of size s1 to iterate over s2 adding the newly seen right
# character and removing the left. If at some point the frequency
# dictionary is empty, we have a full match and can return True, if we
# get to the end of s2 without a match, we can return False.
#
# Time complexity: O(n) - Where n is the number of characters in the s2
# we iterate over all characters in s2 and do O(1) work for each.
# Space complexity: O(1) - The input strings can only have English
# lowercase letters, the frequency dictionary can grow at max to 26.
#
# Runtime: 61 ms, faster than 98.26%
# Memory Usage: 13.8 MB, less than 94.40%
class SlidingWindow:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # For some reason the defaultdict is faster than Counter.
        # freq = Counter()
        freq = defaultdict(int)
        # Mark each character in s1 as "need to match".
        for c in s1:
            freq[c] -= 1
        # Mark the characters in the first len(s1) characters on s2 as
        # "seen".
        for c in s2[: len(s1)]:
            freq[c] += 1
            if freq[c] == 0:
                del freq[c]
        # Check if we have a match
        if not freq:
            return True
        # Iterate over the rest of the string s2 "unseeing" the left
        # character and "seeing" the right one.
        left, right = 0, len(s1) - 1
        while right < len(s2) - 1:
            freq[s2[left]] -= 1
            if freq[s2[left]] == 0:
                del freq[s2[left]]
            left += 1
            right += 1
            freq[s2[right]] += 1
            if freq[s2[right]] == 0:
                del freq[s2[right]]
            # If at any point we match s1, return True
            if not freq:
                return True
        # If none of the substrings matched, return False
        return False


def test():
    executors = [
        SlidingWindow,
    ]
    tests = [
        ["aba", "ab", False],
        ["adc", "dcda", True],
        ["ab", "eidbaooo", True],
        ["ab", "eidboaoo", False],
        ["aabbcc", "cacbba", True],
        ["aabcc", "cacbba", False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.checkInclusion(t[0], t[1])
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
