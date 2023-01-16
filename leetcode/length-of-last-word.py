# 58. Length of Last Word
# 🟢 Easy
#
# https://leetcode.com/problems/length-of-last-word/
#
# Tags: String

import timeit


# Use the built-in str.split function to get the last word.
#
# Time complexity: O(n) - The function iterates over all characters in
# the input.
# Space complexity: O(n) - The function creates an array with all the
# words in the input.
#
# Runtime 33 ms Beats 73.47%
# Memory 13.8 MB Beats 76.78%
class BuiltIn:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


# Start iterating over the characters in the input string starting from
# the back, first ignore all whitespace, then count characters, as soon
# as we see whitespace again, stop iterating and return the length of
# the word.
#
# Time complexity: O(n) - We may iterate over all the input.
# Space complexity: O(1) - We only use pointers.
#
# Runtime 33 ms Beats 85.69%
# Memory 13.8 MB Beats 76.78%
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in reversed(range(len(s))):
            # Skip any whitespace while we don't have a word.
            if s[i] == " ":
                # If we already computed a word's length, return it.
                if res:
                    return res
                # If this is whitespace at the end, ignore it.
                continue
            res += 1
        return res


def test():
    executors = [
        BuiltIn,
        Solution,
    ]
    tests = [
        ["l     ", 1],
        ["     e", 1],
        ["Hello World", 5],
        ["luffy is still joyboy", 6],
        ["   fly me   to   the moon  ", 4],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.lengthOfLastWord(t[0])
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
