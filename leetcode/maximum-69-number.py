# 1323. Maximum 69 Number
# 🟢 Easy
#
# https://leetcode.com/problems/maximum-69-number/
#
# Tags: Math - Greedy

import timeit


# We can obtain the largest number converting the 6 with the highest
# order into a 9, if none are found, then it is optimal to not modify
# the input.
#
# Time complexity: O(1) - We iterate 3 times over the input, converting
# to a list of strings, finding the first 6 and casting back to int.
# Since the input has a maximum of 4 digits, time is bounded.
# Space complexity: O(1) - Where n is the number of digits in the input,
# we create a list of digits. Since the input has a maximum of 4 digits,
# space is bounded.
#
# Runtime: 38 ms, faster than 84.45%
# Memory Usage: 13.8 MB, less than 54.69%
class Parsing:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))


# Use divmod inside a loop to find the index of the furthest left 6 in
# the input, then add 3 at that position to update that value to a 9.
#
# Time complexity: O(1) - The loop will execute a maximum of 4 times
# because num <= 10^4.
# Space complexity: O(1) - Constant space.
#
# Runtime: 67 ms, faster than 10.70%
# Memory Usage: 14 MB, less than 9.69%
class Math:
    def maximum69Number(self, num: int) -> int:
        # The digit that we are visiting left to right.
        i = 0
        # Make a copy of num to mutate it.
        quotient = num
        # Store the furthest left index at which we find a number 6.
        highest_six = -1
        while quotient > 0:
            quotient, remainder = divmod(quotient, 10)
            if remainder == 6:
                highest_six = i
            i += 1
        # If we found any 6, update the highest 6 found to become a 9
        # by adding 3 at that position in the input number.
        return (num + 3 * (10**highest_six)) if highest_six != -1 else num


def test():
    executors = [
        Parsing,
        Math,
    ]
    tests = [
        [9669, 9969],
        [9996, 9999],
        [9999, 9999],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maximum69Number(t[0])
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
