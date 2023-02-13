# 28. Find the Index of the First Occurrence in a String
# 🟠 Medium
#
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
#
# Tags: Two Pointers - String - String Matching

import timeit


# The naive solution just checks the needle starting at each position of
# the haystack.
#
# Time complexity: O(m*n) - For each index of the haystack we may check
# each character of the needle until we find a mismatch.
# Space complexity: O(1) - No extra space is used.
#
# Runtime 34 ms Beats 56.78%
# Memory 14 MB Beats 11.55%
class Naive:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                # If the characters do not match, we have not match at
                # this position.
                if haystack[i + j] != needle[j]:
                    break
                # If we have matched the last character in the needle,
                # we have a full match and can return the position in
                # the haystack of the first character of the match.
                if j == len(needle) - 1:
                    return i
        # Failed to find the needle in the haystack.
        return -1


# Use the Knuth-Morris-Prat algorithm for string matching.
# https://en.wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm
#
# Time complexity: O(m+n) - We iterate a maximum of two times over both
# the haystack and the needle.
# Space complexity: O(n) - The LPS table has the same size as the needle.
#
# Runtime 24 ms Beats 96.43%
# Memory 13.6 MB Beats 96.20%
class KMP:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        # Initialize the LPS array. LPS pointers points to index 1.
        lps, left, right = [0] * n, 0, 1
        while right < n:
            # If the characters match, the lps is one character
            # longer.
            if needle[left] == needle[right]:
                lps[right] = left + 1
                left += 1
                right += 1
            # If the previous lps had length 0 and this character
            # does not match, the lps at this position is also 0.
            elif left == 0:
                lps[right] = 0
                right += 1
            # If the previous lps was longer than 0, check if the
            # previous character matched.
            else:
                left = lps[left - 1]
        # Initialize a pointer in the haystack and one in the needle.
        haystack_idx, needle_idx = 0, 0
        while haystack_idx < m:
            if haystack[haystack_idx] == needle[needle_idx]:
                haystack_idx += 1
                needle_idx += 1
            elif needle_idx == 0:
                haystack_idx += 1
            else:
                needle_idx = lps[needle_idx - 1]
            # If we get to the index after the end of the needle, we
            # have matched the needle.
            if needle_idx == n:
                return haystack_idx - n
        return -1


def test():
    executors = [
        Naive,
        KMP,
    ]
    tests = [
        ["a", "a", 0],
        ["aaa", "", 0],
        ["aaa", "aaaa", -1],
        ["sadbutsad", "sad", 0],
        ["leetcode", "leeto", -1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.strStr(t[0], t[1])
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
