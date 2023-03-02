# 443. String Compression
# 🟠 Medium
#
# https://leetcode.com/problems/string-compression/
#
# Tags: Two Pointers - String

import timeit
from typing import List


# Use two pointers, one to read and one to write, iterate over all the
# characters in the input reading characters while there are any and
# they are the same as the current sequence's character, when we run out
# of characters or find a new character, we write down the compressed
# sequence and check if there are more characters to read.
#
# Time complexity: O(n) - We visit each character in the input once.
# Space complexity: O(1) - We use pointers and create a new string of
# the digits of count that can be at most of length 4.
#
# Runtime 64 ms Beats 51.18%
# Memory 14 MB Beats 25.81%
class Solution:
    def compress(self, chars: List[str]) -> int:
        w, current, count = 0, chars[0], 1
        for r in range(1, len(chars) + 1):
            # In either of these cases we need to compress the sequence.
            if r == len(chars) or current != chars[r]:
                # Compress.
                chars[w] = current
                w += 1
                if count != 1:
                    for digit in str(count):
                        chars[w] = digit
                        w += 1
                # If not end of string, start new sequence.
                if r < len(chars):
                    current = chars[r]
                    count = 1
                    r += 1
            else:
                count += 1
        return w


def test():
    executors = [Solution]
    tests = [
        [["a"], 1, ["a"]],
        [
            ["a", "a", "b", "b", "c", "c", "c"],
            6,
            ["a", "2", "b", "2", "c", "3"],
        ],
        [
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
            4,
            ["a", "b", "1", "2"],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.compress(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
                # The input should be mutated.
                mutated = t[0][: t[1]]
                assert mutated == t[2], (
                    f"\033[93m» {mutated} <> {t[2]}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
