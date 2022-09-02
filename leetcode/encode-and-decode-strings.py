# 271. Encode and Decode Strings
# 🟠 Medium
#
# https://leetcode.com/problems/encode-and-decode-strings/ 🔒
# https://www.lintcode.com/problem/659/
#
# Tags: String - Design

import timeit
from typing import List


# We can start each string by a series of digits denoting its length
# followed by a delimiter followed by the word itself. To decode, we
# start by finding the length of the next word, by reading all the
# digits found before we hit the delimiter, then processing the word,
# then moving to the next word.
#
# Time complexity: O(n) - Both encode and decode need to read each
# character of the input.
# Space complexity: O(n) - At worst we will double the number of
# characters in the input when we encode.
#
# Runtime: 591 ms, faster than 57.00%
# Memory Usage: 6.12 MB, less than 53.79%
class Solution:
    def __init__(self) -> None:
        self.delimiter = "&"

    def encode(self, strs: List[str]) -> str:
        # Iterate over the input strings, for each string, we prepend it
        # with its number of characters followed by the chosen especial
        # character.
        result = ""
        for s in strs:
            # i.e. "love" => "4", "&", "love"
            result += str(len(s)) + self.delimiter + s
        return result

    def decode(self, str: str) -> List[str]:
        # Manually manage the index to be able to fast-forward.
        i = 0
        # Store the words that we have decoded.
        words = []
        # Keep processing words while we have string remaining.
        while i < len(str):
            # Start by finding the digits of the next word.
            digits = []
            while str[i].isdigit():
                digits.append(str[i])
                i += 1
            # We have run out of digits, compute the length of the word.
            word_length = int("".join(digits))
            # We can also found the boundaries, it makes the code more
            # readable even if it isn't strictly necessary.
            right = i + 1 + word_length
            # Move the left pointer one position forward to avoid using
            # the digit/word boundary.
            i += 1
            # Now process the characters in the word.
            word = []
            while i < right:
                word.append(str[i])
                i += 1
            # We have processed all characters of the word, add it to
            # the result set and move to the next one.
            words.append("".join(word))
        # Return all the words once we decode them.
        return words


def test():
    executors = [Solution]
    tests = [
        [[]],
        [["4"]],
        [["we", "say", ":", "yes"]],
        [["lint", "code", "love", "you"]],
        [["20&something", "4&", "foo20&bar"]],
    ]

    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                # The result of decoding the encoded string should be
                # the input.
                result = sol.decode(sol.encode(t[0]))
                exp = t[0]
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
