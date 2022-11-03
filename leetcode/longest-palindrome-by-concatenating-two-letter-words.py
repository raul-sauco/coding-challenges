# 2131. Longest Palindrome by Concatenating Two Letter Words
# 🟠 Medium
#
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
#
# Tags: Array - Hash Table - String - Greedy - Counting

import timeit
from typing import List


# We can create a dictionary of words that we have seen and how many
# times we have seen them, when we see a new word, we check if we can
# use it to build a palindrome by reversing it and checking it against
# the dictionary, if we can use it, we "consume" its palindromic entry
# from the dictionary and add 4 to the result.
#
# For example, if we have {'ab': 1} in the dictionary and we are
# evaluating 'ba', we remove one entry from 'ab' from the dictionary and
# add 4 to the result count. Note that in this case, removing 1 count
# of 'ab' removes the entry completely from the dictionary.
#
# Once we run out of words, we check the dictionary for a palindrome key
# that we have not consumed, for example 'aa', if we find one, we add 2
# to the result set, because we could use it to build the palindrome
# around it.
#
# Time complexity: O(n) - We visit each character in the input once.
# Space complexity: O(n) - The dictionary can grow to the same size as
# the input.
#
# Runtime: 1707 ms, faster than 71.76%
# Memory Usage: 38.3 MB, less than 87.66%
class TwoLoops:
    def longestPalindrome(self, words: List[str]) -> int:
        # Initialize the result at 0.
        count = 0
        # Create a dictionary with entries we have seen but haven't
        # consumed yet.
        available = {}
        # Iterate over the input.
        for word in words:
            rev = word[::-1]
            # Check if we can use the current word to increase the
            # length of the result.
            if rev in available:
                count += 4
                available[rev] -= 1
                # Remove any entries that are no longer available.
                if available[rev] == 0:
                    del available[rev]
            # If we cannot use the word at the moment, add it to the
            # available words.
            else:
                if word in available:
                    available[word] += 1
                else:
                    available[word] = 1
        # Once we have consumed all 4 letter possibilities, try to add
        # a 2 character palindrome at the center of the result.
        for word in available:
            if word[0] == word[1]:
                # If we find any 2 character palindrome, add it to the
                # result and exit the loop.
                count += 2
                break
        return count


# Similar to the above solution but merge the check for an available
# 2 character palindrome into the main loop. I expected this solution to
# perform better, but it actually performed worst on the LeetCode tests
# than the version above, which is easier to read.
#
# Time complexity: O(n) - We visit each character in the input once.
# Space complexity: O(n) - The dictionary can grow to the same size as
# the input.
#
# Runtime: 2387 ms, faster than 29.21%
# Memory Usage: 38.3 MB, less than 87.66%
class OneLoop:
    def longestPalindrome(self, words: List[str]) -> int:
        # Initialize the result at 0.
        count = 0
        # Create a dictionary with entries we have seen but haven't
        # consumed yet.
        available = {}
        # Keep a count of available 2 character palindromes to avoid
        # having to loop through the dictionary a second time.
        available_two_character_pal = 0
        # Iterate over the input.
        for word in words:
            rev = word[::-1]
            # Check if we can use the current word to increase the
            # length of the result.
            if rev in available:
                count += 4
                available[rev] -= 1
                # Remove any entries that are no longer available.
                if available[rev] == 0:
                    del available[rev]
                # If the character is a 2 letter palindrome, subtract
                # one from the count because we are consuming it.
                if word[0] == word[1]:
                    available_two_character_pal -= 1
            # If we cannot use the word at the moment, add it to the
            # available words.
            else:
                if word in available:
                    available[word] += 1
                else:
                    available[word] = 1
                # If the character is a 2 letter palindrome, add one to
                # the count because it is becoming available.
                if word[0] == word[1]:
                    available_two_character_pal += 1
        # Once we have consumed all 4 letter possibilities, try to add
        # a 2 character palindrome at the center of the result.
        if available_two_character_pal > 0:
            count += 2
        return count


def test():
    executors = [TwoLoops, OneLoop]
    tests = [
        [["ga"], 0],
        [["gg"], 2],
        [["cc", "ll", "xx"], 2],
        [["lc", "cl", "ga"], 4],
        [["lc", "cl", "gg"], 6],
        [["ab", "ty", "yt", "lc", "cl", "ab"], 8],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.longestPalindrome(t[0])
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
