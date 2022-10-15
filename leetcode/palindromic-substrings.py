# 647. Palindromic Substrings
# 🟠 Medium
#
# https://leetcode.com/problems/palindromic-substrings/
#
# Tags: String - Dynamic Programming

import timeit

# 100 calls.
# » BruteForce          0.02709   seconds
# » DP                  0.01912   seconds
# » ExpandFromCenter    0.00466   seconds
# » Manacher            0.00806   seconds

# The naive brute force solution checks every combination of indexes to
# see if the substring between them is a palindrome.
#
# Time complexity: O(n^3) - For each combination of 2 indexes O(n^2), we
# check if the substring between them is a palindrome O(n).
# Space complexity: O(n) - Reversing the string happens in memory.
#
# This solution would fail with Time Limit Exceeded.
class BruteForce:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                ss = s[i : j + 1]
                if ss == ss[::-1]:
                    res += 1
        return res


# We can sacrifice memory to improve the results of the brute force
# solution, if we start building palindromes of length 1, 2, 3... and
# we store wether the string between two given indexes left-right is,
# or is not, a palindrome, then we can check in O(1) wether the
# substring i:j is a palindrome by checking if the string i+1:j-1 is a
# palindrome and s[i] == s[j].
#
# Time complexity: O(n^2) - We still check each pair of characters, but
# this time we only do O(1) work for each.
# Space complexity: O(n^2) - We save a value in the dp object for each
# pair of indexes in the input.
#
# Runtime: 778 ms, faster than 14.45%
# Memory Usage: 21.7 MB, less than 22.96%
class DP:
    def countSubstrings(self, s: str) -> int:
        # Store computations in a 2D array of size len(s)^2
        dp = [[0] * len(s) for _ in range(len(s))]
        # All single character strings are palindromes. O(n)
        res = 0
        for i in range(len(s)):
            dp[i][i] = True
            res += 1
        # Now check pairs of characters
        for i in range(len(s) - 1):
            if s[i + 1] == s[i]:
                dp[i][i + 1] = True
                res += 1
        # Start trying to build longer palindromes. O(n^2)
        for sub_str_size in range(3, len(s) + 1):
            for left in range(len(s) + 1 - sub_str_size):
                right = left + sub_str_size - 1
                # If the center is a palindrome and we add the same
                # character on each end, we obtain a palindrome.
                if dp[left + 1][right - 1] and s[left] == s[right]:
                    dp[left][right] = True
                    res += 1
        return res


# Find all the centers, characters and whitespace between characters,
# and start expanding from them, for each palindrome formed, add it to
# the total count.
#
# Time complexity: O(n^2) - We still visit each combination of 2 indexes
# but this time only do O(1) work for each.
# Space complexity: O(1) - We only store one integer for the result and
# a few pointers for the iteration.
#
# Runtime: 444 ms, faster than 28.06%
# Memory Usage: 13.9 MB, less than 75.46%
class ExpandFromCenter:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in [i, i + 1]:
                # Start from all single characters s[i:i] and character
                # pairs s[i:i+1]
                left, right = i, j
                # While the current value is a palindrome and the two
                # characters that we will visit are the same.
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
        return res


# Use Manacher's algorithm to find the length of palindromes that we can
# build.
#
# Good examples online, for example Wikipedia or:
# https://www.scaler.com/topics/data-structures/manachers-algorithm/
#
# Time complexity: O(n) - The algorithm uses the concept of palindromes
# being formed by inner palindromes to avoid checking each pair of
# indexes.
# Space complexity: O(n) - The length of the doubled up string and the
# array of length around centers.
#
# Runtime: 74 ms, faster than 99.28%
# Memory Usage: 13.8 MB, less than 75.43%
class Manacher:
    def countSubstrings(self, s: str) -> int:
        # Manacher's algorithm only computes the length of odd sized
        # palindromes, but we can circumvent this limitation inserting
        # a dummy character between each character in our input string.
        ss = "^." + ".".join(s) + ".$"
        # Array of center positions with the maximum length of a
        # palindrome found so far with that index at its center.
        centers = [0] * len(ss)
        # Initialize the center and width from which we will start the
        # algorithm.
        center = width = 0
        # Iterate over all possible palindrome palindrome widths.
        for i in range(1, len(ss) - 1):
            if i < width:
                centers[i] = min(width - i, centers[2 * center - i])
            # Expand around the center while the characters are the
            # same at both ends.
            while ss[i + centers[i] + 1] == ss[i - centers[i] - 1]:
                centers[i] += 1
            # Once we compute the longest palindrome at the current
            # center, update the center and size.
            if i + centers[i] > width:
                center, width = i, i + centers[i]
        # Return the number of palindromes that we can obtain.
        return sum((length + 1) // 2 for length in centers)
        # TODO compute the result inside the loop to avoid this O(n) sum.


def test():
    executors = [
        BruteForce,
        DP,
        ExpandFromCenter,
        Manacher,
    ]
    tests = [
        ["abc", 3],
        ["aaa", 6],
        ["abcdeedcba", 15],
        ["abcdefghijklmnopqrstuvwxyz", 26],
        ["ababacdefghijklmnopqrstuvwxyz", 33],
        ["ababacdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcababa", 95],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(100):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.countSubstrings(t[0])
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
