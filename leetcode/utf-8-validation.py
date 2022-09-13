# 393. UTF-8 Validation
# 🟠 Medium
#
# https://leetcode.com/problems/utf-8-validation/
#
# Tags: Array - Bit Manipulation

import timeit
from typing import List


# Iterate over the input converting the integer to string
# representations of their 8 less significant bits. When a single byte
# character is found, move to the next one, when a multi-byte character
# is found, check that the next bytes match the expected format.
#
# Time complexity: O(n) - Where n is the number of integers in the input.
# Space complexity: O(1) - Constant space.
#
# Runtime: 115 ms, faster than 94.59%
# Memory Usage: 14.1 MB, less than 96.64%
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # Use a counter to determine wether we are processing a multi
        # byte character.
        remaining_bytes = 0
        # Iterate over the input values checking if they form a valid
        # utf-8 string.
        for val in data:
            # Only consider the last 8 bits.
            bits = format(val, "08b")
            # If we are in the middle of processing a multi-byte
            # character.
            if remaining_bytes > 0:
                # The byte should start with 10, checking with two
                # conditionals is more readable and faster than slicing.
                if bits[0] == "1" and bits[1] == "0":
                    remaining_bytes -= 1
                # If we are processing a multi-byte character and the
                # byte does not start with 10, the sequence is wrong.
                else:
                    return False
            # Else, we are not processing a multi-byte character.
            else:
                # We only need to handle multi-byte start bytes, we can
                # safely ignore single byte characters and move to the
                # next.
                if bits[0] == "1":
                    # Count the number of leading 1s followed by a 0. If there are
                    # more than 4, stop counting.
                    idx = 0
                    while idx < 5 and bits[idx] == "1":
                        idx += 1
                    # Idx indicates the number of leading 1s followed
                    # by a 0. Valid range is 2 to 4.
                    if not 2 <= idx <= 4:
                        return False
                    # Now lets find the remaining bytes of this multi
                    # byte character.
                    remaining_bytes = idx - 1
        # If all the bytes were valid and we have no pending multi-byte
        # character bytes, the string is valid.
        return not remaining_bytes


# TODO add the bit manipulation solution to avoid string conversion.


def test():
    executors = [Solution]
    tests = [
        [[0], True],  # Correct one byte starts with 0
        [[237], False],  # Incorrect multi-byte but missing next bytes.
        [[197, 130, 1], True],
        [[235, 140, 4], False],
        [[250, 145, 145, 145, 145], False],  # Too many 1s on first byte.
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.validUtf8(t[0])
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
