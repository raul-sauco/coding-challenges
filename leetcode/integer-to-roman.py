# 12. Integer to Roman
# 🟠 Medium
#
# https://leetcode.com/problems/integer-to-roman/
#
# Tags: Hash Table - Math - String

import timeit


# For each weight, handle separately the unique cases, then use integer
# division to know how many of the characters that represent this
# weight to add.
#
# Time complexity: O(1) - We iterate over the 13 keys in the dictionary.
# Space complexity: O(1) - The result array can grow to max size 9.
#
# Runtime: 53 ms, faster than 91.79%
# Memory Usage: 13.8 MB, less than 98.85%
class Solution:
    def intToRoman(self, num: int) -> str:
        # Create a dictionary of values mapped to their characters.
        mappings = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        res = []
        for key in mappings:
            # Use division to compute the number of this character to add.
            res += (num // key) * mappings[key]
            # Mod by this value to move to the next.
            num %= key
        return "".join(res)


def test():
    executors = [Solution]
    tests = [
        [1, "I"],
        [9, "IX"],
        [3, "III"],
        [58, "LVIII"],
        [1994, "MCMXCIV"],
        [3999, "MMMCMXCIX"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.intToRoman(t[0])
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
