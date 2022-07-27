# 43. Multiply Strings
# 🟠 Medium
#
# https://leetcode.com/problems/multiply-strings/
#
# Tags: Math - String - Simulation

import timeit


# The obvious solution is out.
# "Note: You must not use any built-in BigInteger library or convert the inputs to integer directly."
#
# Even so, it still passes the tests and it is very efficient.
#
# Runtime: 34 ms, faster than 95.63% of Python3 online submissions for Multiply Strings.
# Memory Usage: 13.8 MB, less than 98.05% of Python3 online submissions for Multiply Strings.
class BuiltInFn:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


# Another solution is to convert to integer parsing digits one at a time. In python we don't need to worry about
# integer overflow, which is probably a main consideration in other languages.
#
# Time complexity: O(n) - n: combined number of digits of the two input strings.
# Space complexity: O(n) - n: combined number of digits of the two input strings.
#
# Runtime: 60 ms, faster than 65.43% of Python3 online submissions for Multiply Strings.
# Memory Usage: 13.8 MB, less than 74.17% of Python3 online submissions for Multiply Strings.
class Iterative:
    def multiply(self, num1: str, num2: str) -> str:
        # Base case, if any of them is 0 return 0
        if num1 == "0" or num2 == "0":
            return "0"

        # Provide a mapping between characters and digits.
        mapping = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        # Function that converts strings to int.
        def strToInt(num: str) -> int:
            # The number we will return.
            n = 0
            # Iterate over the digits of num from less weight to more weight.
            for idx, digit in enumerate(reversed(num)):
                # Save time remembering the last power of 10
                if idx == 0:
                    exp = 1
                elif idx == 1:
                    exp = 10
                else:
                    exp *= 10
                # Add to the digit we are building this digit times the power of 10 of its position.
                n += mapping[digit] * exp
            # Return the int value of the input str.
            return n

        # Multiply the integer value of both input strings and return it.
        return str(strToInt(num1) * strToInt(num2))


# Looking at the solution in LeetCode, it turns out that the description wasn't very clear, it is OK to use int() to
# convert one string digit to int at a time, what they expected you to do is to not use the multiplication operator,
# that would lead to overflow, in some languages though not Python, if we could not use a big integer library.
#
# With that in mind, we can correct the solution above to not use the multiplication operator and, instead, simulate
# the multiplication process. Since we already have a dictionary that helps us convert digits to int, we can use that
# and avoid calling int().
#
# Time complexity: O(len(num1) + len(num2)) - We multiply each number in n * each one in m.
# Space complexity: O(len(num1) + O(len(num2))) - The product array is of size n + m.
#
# Runtime: 295 ms, faster than 17.57% of Python3 online submissions for Multiply Strings.
# Memory Usage: 13.9 MB, less than 74.17% of Python3 online submissions for Multiply Strings.
class Simulated:
    def multiply(self, multiplicand: str, multiplier: str) -> str:
        # Base case, if any of them is 0 return 0.
        if multiplicand == "0" or multiplier == "0":
            return "0"

        # Provide a mapping between characters and digits.
        mapping = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        # Prepare an empty array where we will build the product of num1 * num2.
        product = [0] * (len(multiplicand) + len(multiplier))

        # Reverse the multiplicand and multiplier. We will process them starting at the least significant digit.
        multiplicand, multiplier = multiplicand[::-1], multiplier[::-1]

        # Nested loop, iterate over the digits of both numbers.
        for multiplicand_idx in range(len(multiplicand)):
            for multiplier_idx in range(len(multiplier)):

                # Avoid using * by adding n m times.
                n = mapping[multiplicand[multiplicand_idx]]
                m = mapping[multiplier[multiplier_idx]]

                # The for loop is equivalent to digit = m * n, but slower.
                digit = 0
                for _ in range(m):
                    digit += n

                # Use the result and carry digit.
                product[multiplicand_idx + multiplier_idx] += digit
                product[multiplicand_idx + multiplier_idx + 1] += product[multiplicand_idx + multiplier_idx] // 10
                product[multiplicand_idx + multiplier_idx] = product[multiplicand_idx + multiplier_idx] % 10

        # Remove all 0s from the back of the array O(1) per removal => O(n)
        # These would have been leading 0s when reversed.
        while product[-1] == 0:
            product.pop()

        # Return the joined list of integers cast to string.
        return "".join([str(digit) for digit in reversed(product)])


def test():
    executors = [
        BuiltInFn,
        Iterative,
        Simulated,
    ]
    tests = [
        [
            "401716832807512840963",
            "167141802233061013023557397451289113296441069",
            "67143675422804947379429215144664313370120390398055713625298709447",
        ],
        ["2", "3", "6"],
        ["123", "456", "56088"],
        ["0", "456", "0"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.multiply(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
