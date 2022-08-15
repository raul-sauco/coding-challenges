# 13. Roman to Integer
# 🟢 Easy
#
# # https://leetcode.com/problems/roman-to-integer/
#
# Tags: Hash Table - Math - String

import timeit


# Create a dictionary to map symbols with their value, then iterate over
# the input checking each value and the next, if any, at the same time,
# when a value is greater than the next, we add its value to the result,
# if smaller, we subtract it from the result.
#
# Time complexity: O(n) - We iterate over all values.
# Space complexity: O(1) - The dictionary and two variables.
#
# Runtime: 70 ms, faster than 62.87%
# Memory Usage: 13.9 MB, less than 76.66%
class HashMap:
    def romanToInt(self, s: str) -> int:
        # Dictionary to store all Roman Symbols.
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        # Initialize the result.
        result = 0
        # Iterate through the Roman string characters.
        for i in range(len(s)):
            # If we are on the last symbol of the string.
            if i == len(s) - 1:
                # Add the current symbol to the result.
                result += roman_dict[s[i]]
            # If we are not on the last symbol of the string.
            else:
                # If the current's symbol value is greater than the
                # next's symbol value.
                if roman_dict[s[i]] >= roman_dict[s[i + 1]]:
                    # Add the current symbol to the result
                    result += roman_dict[s[i]]
                # If the current symbol value is less than the next's
                # symbol value.
                else:
                    # Subtract the current symbol from the result.
                    result -= roman_dict[s[i]]
        # Return the result.
        return result


# Easier to read version merging the if-else statements into one.
#
# Time complexity: O(n) - We iterate over all values.
# Space complexity: O(1) - The dictionary and two variables.
#
# Runtime: 86 ms, faster than 35.07%
# Memory Usage: 13.8 MB, less than 76.66%
class HashMapMergedIf:
    def romanToInt(self, s: str) -> int:
        # Dictionary to store all Roman Symbols.
        dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        # Initialize the result.
        result = 0
        # Iterate through the Roman string characters.
        for i in range(len(s)):
            current = dictionary[s[i]]
            next = dictionary[s[i + 1]] if i < len(s) - 1 else None
            # If we are on the last value, or this value is greater than
            # the next value, add it to the result.
            if not next or current >= next:
                result += current
            # If the current value is smaller than the next value,
            # subtract it from the result.
            else:
                result -= current
        # Return the result.
        return result


def test():
    executors = [
        HashMap,
        HashMapMergedIf,
    ]
    tests = [
        ["III", 3],
        ["IV", 4],
        ["IX", 9],
        ["LVIII", 58],
        ["MCMXCIV", 1994],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.romanToInt(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
