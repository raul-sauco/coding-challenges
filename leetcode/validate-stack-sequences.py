# 946. Validate Stack Sequences
# 🟠 Medium
#
# https://leetcode.com/problems/validate-stack-sequences/
#
# Tags: Array - Stack - Simulation

import timeit
from typing import List


# Use an extra stack of memory and simulate the operations that took
# place, push the next element, then, while the top of the stack matches
# the next element that needs to be popped, pop it.
#
# Time complexity: O(n) - We visit each element on the pushed array and
# do amortized O(1) for each.
# Space complexity: O(n) - The stack can grow to the same size as the
# input.
#
# Runtime 57 ms Beats 99.86%
# Memory 14.1 MB Beats 85.31%
class Solution:
    def validateStackSequences(
        self, pushed: List[int], popped: List[int]
    ) -> bool:
        # Try to simulate the stack, we pop when we can and push
        # when we cannot pop.
        n, stack, next_pop = len(pushed), [], 0
        for el in pushed:
            # Push the next element.
            stack.append(el)
            # Pop all elements that match.
            while stack and next_pop < n and stack[-1] == popped[next_pop]:
                stack.pop()
                next_pop += 1
        # If the sequence is valid, we would have popped everything.
        return next_pop == n


def test():
    executors = [Solution]
    tests = [
        [[1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True],
        [[1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.validateStackSequences(t[0], t[1])
                exp = t[2]
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
