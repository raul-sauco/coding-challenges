# 567. Permutation in String
# 🟠 Medium
#
# https://leetcode.com/problems/permutation-in-string/
#
# Tags: Hash Table - Two Pointers - String - Sliding Window

import timeit
from collections import defaultdict

# A very similar problem to LeetCode 438. Find All Anagrams in a String. We can use the same technique:
# Use a hashmap to keep track of characters that we need vs characters we have seen.
# Negative values denote characters in s1 that we haven't found in s2 yet, positive values denote characters that we
# have seen in s2 but aren't, or not in the same frequency, in s1. When we have the same frequency of the same
# character, we remove the entry from the dictionary.
# We use a sliding window of size s1 to iterate over s2 adding the newly seen right character and removing the left.
# If at some point the frequency dictionary is empty, we have a full match and can return True, if we get to the
# end of s2 without a match, we can return False.
#
# Time complexity: O(n) - with n being the len(s2)
# Space complexity: O(n) - with n being the len(s1)
#
# Runtime: 61 ms, faster than 98.26% of Python3 online submissions for Permutation in String.
# Memory Usage: 13.9 MB, less than 68.06% of Python3 online submissions for Permutation in String.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = defaultdict(int)
        # Mark each character in s1 as "need to match"
        for c in s1:
            freq[c] -= 1

        # Mark the characters in the first len(s1) characters on s2 as "seen"
        for c in s2[: len(s1)]:
            freq[c] += 1
            if freq[c] == 0:
                del freq[c]

        # Check if we have a match
        if not freq:
            return True

        # Iterate over the rest of the string s2 "unseeing" the left character and "seeing" the right one.
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
    executors = [Solution]
    tests = [
        ["ab", "eidbaooo", True],
        ["ab", "eidboaoo", False],
        ["ababaa", "ab", False],  # longer s1
        ["aabbcc", "cacbba", True],  # Full match
        ["aabcc", "cacbba", False],  # Order mismatch
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.checkInclusion(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
