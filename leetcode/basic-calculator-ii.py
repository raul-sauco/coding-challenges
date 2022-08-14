# 227. Basic Calculator II
# 🟠 Medium
#
# https://leetcode.com/problems/basic-calculator-ii/
#
# Tags: Math - String - Stack

import timeit


# The operators "*" and "/" have precedence, we can start pushing into
# the stack numbers and "+" and "-" signs but immediately compute the
# result of product and division operations, once we process the whole
# string, reverse the stack and start popping from it to compute sums
# and subtractions.
#
# Time complexity: O(n) - Linear time over the number of characters of
# the input.
# Space complexity: O(n) - We could store the entire input in the stack.
#
# Runtime: 274 ms, faster than 8.04%
# Memory Usage: 19 MB, less than 6.46%
class StackTwoLoops:
    def calculate(self, s: str) -> int:
        # Store operations in the stack.
        stack = []
        idx = 0
        while idx < len(s):
            # Use a variable to construct integers from digits.
            digits = []
            # Get the next integer.
            while idx < len(s) and s[idx] not in "+-*/":
                # Skip blank spaces.
                if s[idx] in "0123456789":
                    digits.append(s[idx])
                idx += 1
            # Convert digits to an integer.
            val = int("".join(digits))
            # If there is nothing in the stack, or the last operator has
            # low priority, push the vale in the stack in case we find
            # a high priority operator later.
            if not stack or stack[-1] in "+-":
                stack.append(val)
            else:
                # The last value is a high priority operand.
                operator = stack.pop()
                first = stack.pop()
                if operator == "*":
                    result = first * val
                else:
                    result = first // val
                stack.append(result)

            # If we have any elements after the current index.
            # The index will be pointing to an operand, not a digit or
            # blank space.
            if idx < len(s) - 1:
                stack.append(s[idx])
                idx += 1

        # Now we need to process sums and subtractions starting from
        # the left and going right.
        stack = stack[::-1]
        while len(stack) > 1:
            op1 = stack.pop()
            operator = stack.pop()
            op2 = stack.pop()
            if operator == "+":
                result = op1 + op2
            else:
                result = op1 - op2
            stack.append(result)
        # Return the first value of the stack.
        return stack[0]


# We can make the observation that the second loop in the previous
# solution only adds the positive values and subtracts the negative
# ones, we could optimize the code if instead of pushing the "+" and "-"
# operands we push positive and negative values to the stack and then
# get the sum of all values. We can also optimize by storing the last
# operator seen in a variable instead of pushing/popping it from the
# stack.
#
# Time complexity: O(n) - Linear time over the number of characters of
# the input.
# Space complexity: O(n) - We could store the entire input in the stack.
#
# Runtime: 141 ms, faster than 50.49%
# Memory Usage: 15.6 MB, less than 71.25%
class StackSum:
    def calculate(self, s: str) -> int:
        # Initialize the last operator and last digit seen to neutral
        # values. Declare the stack.
        last_operator, val, stack = "+", 0, []
        # Iterate over the
        for idx, c in enumerate(s):
            # If we see a digit, keep constructing the integer.
            if c.isdigit():
                val = 10 * val + int(c)
            # If we see an operator or get to the end of the input,
            # compute the result of the operator and operands.
            if c in "+-*/" or idx == len(s) - 1:
                if last_operator == "+":
                    stack.append(val)
                elif last_operator == "-":
                    stack.append(-val)
                elif last_operator == "*":
                    stack.append(stack.pop() * val)
                elif last_operator == "/":
                    stack.append(int(stack.pop() / val))
                # If the current character is an operator, reset the
                # variables.
                last_operator, val = c, 0
        # Return the sum of values in the stack.
        return sum(stack)


# We can further improve the space complexity of the previous solution
# if we use a variable to store the current result, instead of pushing
# values into the stack and calculating their sum at the end.
#
# Time complexity: O(n) - Linear time over the number of characters of
# the input.
# Space complexity: O(1) - We use constant space.
#
# Runtime: 154 ms, faster than 41.54%
# Memory Usage: 15.3 MB, less than 84.04%
class StackVar:
    def calculate(self, s: str) -> int:
        # Initialize the last operator and last digit seen to neutral
        # values. Declare the stack.
        last_operator, val, last_value, result = "+", 0, 0, 0
        # Iterate over the
        for idx, c in enumerate(s):
            # If we see a digit, keep constructing the integer.
            if c.isdigit():
                val = 10 * val + int(c)
            # If we see an operator or get to the end of the input,
            # compute the result of the operator and operands.
            if c in "+-*/" or idx == len(s) - 1:
                if last_operator == "+":
                    result += last_value
                    last_value = val
                elif last_operator == "-":
                    result += last_value
                    last_value = -val
                elif last_operator == "*":
                    last_value *= val
                    # stack.append(stack.pop() * val)
                elif last_operator == "/":
                    # Python truncates negative division towards -inf.
                    if last_value < 0:
                        last_value = -(-last_value // val)
                    else:
                        last_value //= val
                    # stack.append(int(stack.pop() / val))
                # If the current character is an operator, reset the
                # variables.
                last_operator, val = c, 0
        result += last_value
        # Return the sum of values in the stack.
        return result


def test():
    executors = [
        StackTwoLoops,
        StackSum,
        StackVar,
    ]
    tests = [
        ["14-3/2", 13],
        ["0-2147483647", -2147483647],
        ["1-1+1", 1],
        ["100101216300", 100101216300],
        ["     3     ", 3],
        ["3+2*2", 7],
        ["0+2*2", 4],
        ["0/2*2", 0],
        [" 3/2 ", 1],
        [" 3+5 / 2 ", 5],
        [" 250 / 25 ", 10],
        [" 250 / 25 * 5 ", 50],
        ["250/ 25 * 5 / 10", 5],
        [" 3+250 / 25 ", 13],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.calculate(t[0])
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
