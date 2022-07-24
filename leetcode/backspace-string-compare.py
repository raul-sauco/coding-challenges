# 844. Backspace String Compare
# 🟢 Easy
#
# https://leetcode.com/problems/backspace-string-compare/
#
# Tags: Two Pointers - String - Stack - Simulation

import timeit
from itertools import zip_longest


# Use two stacks, iterate over the characters in the input strings pushing and popping as required then compare the
# resulting stacks.
#
# Time complexity: O(n) - We iterate over all elements in the input.
# Space complexity: O(n) - The stacks could grow to the same size as the input strings.
#
# Runtime: 48 ms, faster than 51.20% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 13.8 MB, less than 73.78% of Python3 online submissions for Backspace String Compare.
class StackSol:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def type(word: str) -> str:
            res = []
            for c in word:
                if c == "#":
                    if res:
                        res.pop()
                else:
                    res.append(c)
            return res

        ss = type(s)
        st = type(t)
        return type(s) == type(t)


# Define a function that simulates typing a word, taking into account the backspace character "#" and use it to
# obtain the result of typing both input strings, then use built-in functions to compare them.
#
# Time complexity: O(s+t) - We visit each element in the input strings twice. Once to build the "typed" string and
# once more to compare the results.
# Space complexity: O(1) - We are not using any data structures but generating values as they are used.
#
# Runtime: 33 ms, faster than 91.44% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 13.8 MB, less than 98.23% of Python3 online submissions for Backspace String Compare.
class BuiltInFn:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Define a function that simulates typing a word. Characters input the characters and "#" simulates backspace.
        def typeWord(word):
            # Count the contiguous backstrokes that we have seen and haven't used yet.
            skip = 0
            # Iterate over the characters in the word starting from the back.
            for c in reversed(word):
                # If the current character is "#" add a backspace stroke to the current count.
                if c == "#":
                    skip += 1
                # If the current character is not "#" but we have unused backspace strokes, use them up "deleting"
                # characters that we have typed previously. We are visiting these characters after the backspaces
                # because we are traveling the word in reverse.
                elif skip:
                    skip -= 1
                # If the current character is not "#" and we don't have any unused backspaces, yield the character.
                else:
                    yield c

        # Use itertools zip with fill and all() to check if the values in both strings match. This takes advantage of
        # the improved performance of the functions written in C.
        return all(x == y for x, y in zip_longest(typeWord(s), typeWord(t)))


def test():
    executors = [StackSol, BuiltInFn]
    tests = [
        ["y#fo##f", "y#f#o##f", True],
        ["ab#c", "ad#c", True],
        ["ab##", "c#d#", True],
        ["a#c", "b", False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.backspaceCompare(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
