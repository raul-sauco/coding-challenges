# Balanced Brackets
# 🟠 Medium
#
# https://www.algoexpert.io/questions/balanced-brackets
#
# Tags: Array - Stack

import timeit


# Use a stack to push/pop to and from, when we find a closing symbol
# it should be preceded by its matching opening symbol.
#
# Time complexity: O(n) - All elements are pushed and popped a maximum
# of 2 times from the stack.
# Space complexity: O(n) - All elements could be pushed into the stack.
class Solution:
    def balancedBrackets(self, string):
        stack = []
        closing = {")": "(", "}": "{", "]": "["}
        opening = set(["(", "{", "["])
        for c in string:
            if c in opening:
                stack.append(c)
            elif c in closing:
                # Check that the last unclosed symbol matches the
                # current one.
                if not stack or stack[-1] != closing[c]:
                    return False
                stack.pop()
        return not stack


def test():
    executors = [Solution]
    tests = [
        ["()[]{}{", False],
        ["([])(){}(())()()", True],
        ["((){{{{[]}}}})", True],
        ["(((((({{{{{[[[[[([)])]]]]]}}}}}))))))", False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.balancedBrackets(t[0])
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
