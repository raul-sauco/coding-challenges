# 150. Evaluate Reverse Polish Notation
# 🟠 Medium
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
#
# Tags: Array - Math - Stack
#
# https://en.wikipedia.org/wiki/Reverse_Polish_notation

import timeit
from operator import add, mul, sub
from typing import List


# We can use a stack to solve this problem.
# Iterate over the input tokens. When we find an integer, we push it
# into the stack. When we find an operand in the set (+ - / +), we pop
# the last two values from the stack in order and perform the operation
# that the operator indicates, then push the result back into the stack.
#
# Time complexity: O(n) - We visit each element of the input.
# Space complexity: O(n) - The stack will grow linearly in relation to
# the size of the input.
#
# Runtime: 59 ms, faster than 99.58% of Python3 online submissions for
# Evaluate Reverse Polish Notation.
# Memory Usage: 14.4 MB, less than 57.26% of Python3 online submissions
# for Evaluate Reverse Polish Notation.
class Stack:
    def evalRPN(self, tokens: List[str]) -> int:
        # All operations work as expected except division because it
        # does not truncate towards 0 when the result in negative.
        # Define our own division truncate towards zero operation.
        def divtz(op1, op2):
            return int(op1 / op2)

        # Map strings to operations.
        mapping = {"+": add, "-": sub, "/": divtz, "*": mul}
        stack = []
        # Iterate over the tokens in the input.
        for token in tokens:
            # When we find an operator, fetch the two operands from the
            # stack and operate.
            if token in mapping:
                # Get the operands in the order they were inserted.
                operand2 = stack.pop()
                operand1 = stack.pop()
                # Push the result into the stack.
                stack.append(mapping[token](operand1, operand2))
            else:
                # Push the value into the stack as an int.
                stack.append(int(token))
        # The description guarantees that we are working with a valid
        # expression, it will always reduce down to one value and it
        # will be the result.
        return stack[0]


def test():
    executors = [Stack]
    tests = [
        [["3", "-2", "/", "3", "*"], -3],  # Test our divtz function.
        [["2", "1", "+", "3", "*"], 9],
        [["4", "13", "5", "/", "+"], 6],
        [
            [
                "10",
                "6",
                "9",
                "3",
                "+",
                "-11",
                "*",
                "/",
                "*",
                "17",
                "+",
                "5",
                "+",
            ],
            22,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.evalRPN(t[0])
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
