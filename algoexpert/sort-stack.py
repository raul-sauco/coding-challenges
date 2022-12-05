# Sort Stack
# 🟠 Medium
#
# https://www.algoexpert.io/questions/sort-stack
#
# Tags: Array - Stack - Sorting

import timeit


# This is a template that can be used as the starting point of a
# solution with minimal changes.
class Solution:
    def sortStack(self, stack):
        # An empty stack and a stack with one element are sorted.
        if len(stack) < 2:
            return stack
        # Pop one value from the stack, make sure it is the greater of
        # the last two values.
        num = stack.pop()
        stack = self.sortStack(stack)
        while num < stack[-1]:
            num2 = stack.pop()
            stack.append(num)
            num = num2
            stack = self.sortStack(stack)
        stack.append(num)
        return stack


def test():
    executors = [Solution]
    tests = [
        [[], []],
        [[1], [1]],
        [[-5, 2, -2, 4, 3, 1], [-5, -2, 1, 2, 3, 4]],
        [
            [2, 4, 22, 1, -9, 0, 6, 23, -2, 1],
            [-9, -2, 0, 1, 1, 2, 4, 6, 22, 23],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.sortStack(t[0])
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
