# 438. Find All Anagrams in a String
# 🟠 Medium
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
#
# Tags: Hash Table - String - Sliding Window

import timeit
from collections import defaultdict
from typing import List


# A very similar problem to LeetCode 567. Permutation in String, create
# a hashmap of character frequencies in p, then start iterating over a
# window of s of the same length as p using the hashmap to check if the
# sliding window contains exactly the same characters, and in the same
# frequency as p, to slide the window, we add the character to the right
# and remove the one to the left from the frequencies dictionary.
#
# Time complexity: O(n) - Where n is the number of characters in s, we
# iterate over all characters in s and do O(1) work for each.
# Space complexity: O(1) - The input strings can only have English
# lowercase letters, the frequency dictionary can grow at max to 26.
#
# Runtime: 98 ms Beats 95.92%
# Memory Usage: 15.2 MB Beats 33.28%
class SlidingWindow:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Base cases
        if len(p) > len(s):
            return []
        # Dictionary with character frequencies that we need for a match.
        # Positive entries denote too many of a character, negative ones
        # too few.
        freq = defaultdict(int)
        for c in p:
            freq[c] -= 1
        # Add the matches of the first substring of size p.
        for i in range(len(p)):
            key = s[i]
            # We need to match one less of this character.
            freq[key] += 1
            if freq[key] == 0:
                del freq[key]
        # Store the indexes at which an anagram starts.
        result = []
        # Base case where the first sequence matches.
        if not freq:
            result.append(0)
        # Use an explicit left pointer and a for loop for an implicit
        # right pointer.
        left = 0
        for right in range(len(p), len(s)):
            # Remove one occurrence of the left character from the
            # frequencies map.
            key = s[left]
            freq[key] -= 1
            if freq[key] == 0:
                del freq[key]
            left += 1
            # Add an occurrence of the right character to the
            # frequencies map.
            key = s[right]
            freq[key] += 1
            if freq[key] == 0:
                del freq[key]
            # When the frequencies map shows that we have a match,
            # add it to the result set.
            if not freq:
                result.append(left)
        return result


# An optimization of the previous solution that uses arrays to store
# the frequencies of elements.
#
# Time complexity: O(n) - Where n is the number of characters in s.
# Space complexity: O(1) - We use an array of size 26.
#
# Runtime 102 ms Beats 93.63%
# Memory 15.2 MB Beats 74.41%
class UseArray:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Base case.
        if len(p) > len(s):
            return []
        # Array of frequencies. Initialized to the missing frequencies
        # in p.
        freq, base = [0] * 26, ord("a")
        for i in range(len(p)):
            freq[ord(p[i]) - base] -= 1
            freq[ord(s[i]) - base] += 1
        # Store the indexes at which an anagram starts.
        result = [0] if not any(freq) else []
        # Use an explicit left pointer and a for loop for an implicit
        # right pointer.
        left = 0
        for right in range(len(p), len(s)):
            # Remove one occurrence of the left character from the
            # frequencies map.
            freq[ord(s[left]) - base] -= 1
            left += 1
            # Add an occurrence of the right character to the
            # frequencies map.
            freq[ord(s[right]) - base] += 1
            # When the frequencies map shows that we have a match,
            # add it to the result set.
            if not any(freq):
                result.append(left)
        return result


def test():
    executors = [
        SlidingWindow,
        UseArray,
    ]
    tests = [
        ["a", "a", [0]],
        ["baa", "aa", [1]],
        ["abab", "ab", [0, 1, 2]],
        ["cbaebabacd", "abc", [0, 6]],
        ["aaaaaaaaaa", "aaaaaaaaac", []],
        ["abacbabc", "abc", [1, 2, 3, 5]],
        ["aaaaaaaaaa", "aaaaaaaaaa", [0]],
        ["aaaaaaaaaa", "aaaaaaaaaaaaa", []],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findAnagrams(t[0], t[1])
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
