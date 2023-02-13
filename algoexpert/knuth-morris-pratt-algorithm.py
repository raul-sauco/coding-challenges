# Knuth–Morris–Pratt Algorithm
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/knuth-morris-pratt-algorithm
#
# Tags: Famous Algorithms - Searching

import timeit


# Use the Knuth-Morris-Prat algorithm for string matching.
# https://en.wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm
#
# Time complexity: O(m+n) - We iterate a maximum of two times over both
# the haystack and the needle.
# Space complexity: O(n) - The LPS table has the same size as the needle.
class Solution:
    def knuthMorrisPrattAlgorithm(self, string, substring):
        m, n = len(string), len(substring)
        if n == 0:
            return 0
        # Initialize the LPS array. LPS pointers points to index 1.
        lps, left, right = [0] * n, 0, 1
        while right < n:
            # If the characters match, the lps is one character
            # longer.
            if substring[left] == substring[right]:
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
            if string[haystack_idx] == substring[needle_idx]:
                haystack_idx += 1
                needle_idx += 1
            elif needle_idx == 0:
                haystack_idx += 1
            else:
                needle_idx = lps[needle_idx - 1]
            # If we get to the index after the end of the needle, we
            # have matched the needle.
            if needle_idx == n:
                return True
        return False


def test():
    executors = [Solution]
    tests = [
        ["aefoaefcdaefcdaed", "aefcdaed", True],
        ["aaabaabacdedfaabaabaaa", "aabaabaaa", True],
        ["testwafwafawfawfawfawfxwfawfawfa", "fawfawfawfawfa", False],
        ["testwafwafawfawfawfawfawfawfawfa", "fawfawfawfawfa", True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.knuthMorrisPrattAlgorithm(t[0], t[1])
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
