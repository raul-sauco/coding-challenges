# 438. Find All Anagrams in a String
# 🟠 Medium
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
#
# Tags: Hash Table - String - Sliding Window

import timeit
from collections import defaultdict
from typing import List


# We can sort the characters in p alphabetically, then check all sequences of the same length in s, sort them
# and check to see if they match. But that would cost O(n*log(n)) because we need to sort each subsequence of s.
# A better method is to create a hashmap of character frequencies in the current substring, with two pointers, for
# each position, we need to subtract one character and add one in O(1) then check against the character frequencies
# on p.
#
# Time complexity: O(n) - we visit each position 1.
# Space complexity: O(n) - The result set could grow to size len(s) if all positions matched. The hashmap
# will have, at most p elements, if we do not consider the output in the complexity analysis, then O(p).
#
# Runtime: 209 ms, faster than 52.44% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 15.2 MB, less than 33.28% of Python3 online submissions for Find All Anagrams in a String.
class TwoPointers:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Base cases
        if len(p) > len(s):
            return []
        # Dictionary with character frequencies that we need for a match.
        # Positive entries denote too many of a character, negative ones too few.
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

        # Two pointers
        left, right = 0, len(p) - 1
        while right < len(s) - 1:
            # Remove one occurrence of the left character from the frequencies map.
            key = s[left]
            freq[key] -= 1
            if freq[key] == 0:
                del freq[key]
            left += 1
            right += 1
            # Add an occurrence of the right character to the frequencies map.
            key = s[right]
            freq[key] += 1
            if freq[key] == 0:
                del freq[key]

            # When the frequencies map shows that we have a match, add it to the result set.
            if not freq:
                result.append(left)

        return result


def test():
    executors = [TwoPointers]
    tests = [
        ["baa", "aa", [1]],
        ["cbaebabacd", "abc", [0, 6]],
        ["abab", "ab", [0, 1, 2]],
        ["a", "a", [0]],
        ["aaaaaaaaaa", "aaaaaaaaaaaaa", []],  # len(p) > len(s)
        ["aaaaaaaaaa", "aaaaaaaaaa", [0]],  # len(p) == len(s), match
        ["aaaaaaaaaa", "aaaaaaaaac", []],  # len(p) == len(s), not match
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findAnagrams(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
