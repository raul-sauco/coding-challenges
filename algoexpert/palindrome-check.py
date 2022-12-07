# Palindrome Check
# 🟢 Easy
#
# https://www.algoexpert.io/questions/palindrome-check
#
# Tags: String

import timeit


# Use two pointers and check that the characters match from the start
# and end inside a while loop.
#
# Time complexity: O(n) - Visit each string position once.
# Space complexity: O(1) - Constant extra memory.
class TwoPointersWhile:
    def isPalindrome(self, string: str) -> bool:
        l, r = 0, len(string) - 1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True


# Use two pointers and check that the characters match from the start
# and end inside a for loop.
#
# Time complexity: O(n) - Visit each string position once.
# Space complexity: O(1) - Constant extra memory.
class TwoPointersFor:
    def isPalindrome(self, string: str) -> bool:
        for i in range(len(string) // 2 + 1):
            if string[i] != string[-i - 1]:
                return False
        return True


# Reverse the input and check the original against the reversed one.
#
# Time complexity: O(n) - Visit each string position once.
# Space complexity: O(n) - The reversed string has the same size as the
# original one.
class Reverse:
    def isPalindrome(self, string: str) -> bool:
        return string == string[::-1]


# Reverse the input and check the original against the reversed one.
#
# Time complexity: O(n) - Visit each string position once.
# Space complexity: O(n) - The reversed string has the same size as the
# original one.
class ListComprehension:
    def isPalindrome(self, string: str) -> bool:
        return all(
            string[i] == string[-i - 1] for i in range(len(string) // 2 + 1)
        )


def test():
    executors = [
        TwoPointersWhile,
        TwoPointersFor,
        Reverse,
        ListComprehension,
    ]
    tests = [
        ["a", True],
        ["ab", False],
        ["aba", True],
        ["abcdcba", True],
        ["abcdefghhgfedcba", True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isPalindrome(t[0])
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
