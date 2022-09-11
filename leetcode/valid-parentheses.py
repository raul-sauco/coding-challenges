# 20. Valid Parentheses
# 🟢 Easy
#
# https://leetcode.com/problems/valid-parentheses/
#
# Tags: String - Stack


import timeit


# Use a stack, visit each character in the string and check if it can be
# used to close the last open parentheses, the top of the stack, if it
# can, remove the matching symbol and move to the next, if it cannot,
# add it to the stack. If the string is composed of valid parentheses,
# at the end of the execution, the stack should be empty.
#
# Time complexity: O(n) - We visit each element and do O(1) work.
# Space complexity: O(n) - The stack could grow to the size of the input.
#
# Runtime: 33 ms, faster than 91.84%
# Memory Usage: 14 MB, less than 26.59%
class Stack:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {")": "(", "]": "[", "}": "{"}
        # Iterate over the symbols in the input.
        for c in s:
            if c in closing:
                # Needs to match the last opening character
                if not stack or closing[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        # If the string is valid, the stack should be empty.
        return not stack


# Another way to check if the symbols that we iterate over form a valid
# group of parentheses. The main logic is the same as in the previous
# solution.
#
# Time complexity: O(n) - We visit each element and do O(1) work.
# Space complexity: O(n) - The stack could grow to the size of the input.
#
# Runtime: 55 ms, faster than 36.00%
# Memory Usage: 14 MB, less than 26.59%
class Stack2:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            # If it is an opening parentheses, append it to the stack.
            if c in "({[":
                stack.append(c)
            else:
                # If it is a closing parentheses, check that it matches
                # the symbol currently opened.
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    # If this symbol does not match, return false now.
                    return False
        return stack == []


def test():
    executors = [
        Stack,
        Stack2,
    ]
    tests = [
        ["()[]{}", True],
        ["", True],
        ["([{{{[()]}}}])[{{()}}]{[[(({{}}))]]}", True],
        ["(]", False],
        ["()[]{", False],
        ["()[]{", False],
        ["(", False],
        ["]", False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isValid(t[0])
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
