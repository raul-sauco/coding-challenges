# 1328. Break a Palindrome
# 🟠 Medium
#
# https://leetcode.com/problems/break-a-palindrome/
#
# Tags: String - Greedy

import timeit


# Iterate over the first half of the input trying to update the leftmost
# possible character to an "a", if this is impossible, then the best
# solution will be to update the rightmost character to a "b".
#
# Time complexity: O(n) - We visit half the characters once.
# Space complexity: O(n) - The mutable list has the same size as the
# input and output.
#
# Runtime: 46 ms, faster than 67.59%
# Memory Usage: 13.7 MB, less than 96.39%
class Greedy:
    def breakPalindrome(self, palindrome: str) -> str:
        # We can never make a single character a palindrome.
        if len(palindrome) == 1:
            return ""
        chars = list(palindrome)
        # Iterate over the first half, excluding the middle character,
        # checking if we can convert any character in a non-a.
        # This loop tries to reduce the lexicographical order of the
        # input palindrome.
        for idx in range(len(palindrome) // 2):
            if chars[idx] != "a":
                chars[idx] = "a"
                return "".join(chars)
        # If we cannot, then convert the rightmost character to a b,
        # thus increasing the lexicographical order, since we know that
        # chars 0..len(n)//2 are all "a", we can substitute the last
        # character for a "b".
        chars[-1] = "b"
        return "".join(chars)


def test():
    executors = [Greedy]
    tests = [
        ["a", ""],
        ["aa", "ab"],
        ["bab", "aab"],
        ["aba", "abb"],
        ["abccba", "aaccba"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.breakPalindrome(t[0])
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
