# 557. Reverse Words in a String III
# 🟢 Easy
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/
#
# Tags: Two Pointers - String

import timeit


# Reverse the entire string and nested reverse the list of words split
# by whitespace.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input.
# Space complexity: O(c) - Where c is the number of characters in the
# longest word in the input.
#
# Runtime: 44 ms, faster than 85.68%
# Memory Usage: 14.7 MB, less than 14.14%
class DoubleReversal:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])[::-1]


# Split the input by whitespace, reverse each token individually and
# return the joined result.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input.
# Space complexity: O(c) - Where c is the number of characters in the
# longest word in the input.
#
# Runtime: 61 ms, faster than 61.24%
# Memory Usage: 14.7 MB, less than 46.10%
class SplitAndJoin:
    def reverseWords(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split()])


# Iterate over the input characters keeping track of the index before
# the start of the last word seen, when we get to the end of that word,
# use two pointers to swap the position of all its characters.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input string.
# Space complexity: O(1) - Only constant space used.
#
# Runtime: 299 ms, faster than 5.04%
# Memory Usage: 14.3 MB, less than 99.72%
class TwoPointers:
    def reverseWords(self, s: str) -> str:
        # Convert the input string to a list.
        ls = list(s)
        # Initialize a pointer to before the start of the last word.
        before = -1
        # Iterate over all positions in the string.
        for i in range(len(ls) + 1):
            # When we find the end of a word.
            if i == len(s) or ls[i] == " ":
                # Initialize two pointers to the start and end of the word.
                l, r = before + 1, i - 1
                # Iterate over the word's characters swapping their
                # position until the pointers meet.
                while l < r:
                    # Swap the characters
                    ls[l], ls[r] = ls[r], ls[l]
                    # Update the pointers.
                    l += 1
                    r -= 1
                # Move to the next word updating its before pointer to
                # the current after pointer.
                before = i
        # Join the mutable list into an immutable string.
        return "".join(ls)


def test():
    executors = [
        SplitAndJoin,
        DoubleReversal,
        TwoPointers,
    ]
    tests = [
        ["Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"],
        ["God Ding", "doG gniD"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(10000):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.reverseWords(t[0])
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
