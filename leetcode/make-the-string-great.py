# 1544. Make The String Great
# 🟢 Easy
#
# https://leetcode.com/problems/make-the-string-great/
#
# Tags: String - Stack

import timeit


# Iterate over the elements of the input string pushing them into a
# stack, if the element that we visit is the uppercase or lowercase
# counterpart of the last element on the stack, pop that element.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input.
# Space complexity: O(n) - The stack could have n elements where n is
# the number of characters of the input.
#
# Runtime: 53 ms, faster than 76.90%
# Memory Usage: 13.8 MB, less than 61.93%
class StackPushPop:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and (
                (c.islower() and c.upper() == stack[-1])
                or (c.isupper() and c.lower() == stack[-1])
            ):
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


# Similar approach but simplify the if statement using character's ASCII
# values.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input.
# Space complexity: O(n) - The stack could have n elements where n is
# the number of characters of the input.
#
# Runtime: 24 ms, faster than 99.91%
# Memory Usage: 13.8 MB, less than 61.93%
class StackAndOrd:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


def test():
    executors = [
        StackPushPop,
        StackAndOrd,
    ]
    tests = [
        ["s", "s"],
        ["Pp", ""],
        ["abBAcC", ""],
        ["leEeetcode", "leetcode"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.makeGood(t[0])
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
