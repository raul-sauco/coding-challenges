# 345. Reverse Vowels of a String
# 🟢 Easy
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/
#
# Tags: String - Two Pointers

import timeit


# Use two pointers to find vowels from the left and right, when both
# pointers have a vowel under them, swap them and slide the pointers
# towards each other, when they have anything but a vowel, slide the
# pointers towards each other.
#
# Time complexity: O(n) - We visit each element exactly once.
# Space complexity: O(n) - We cast the string to a list to be able to
# swap characters.
#
# Runtime: 80 ms, faster than 80.65%
# Memory Usage: 15.1 MB, less than 59.35%
class TwoPointers:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = set("aeiouAEIOU")
        l, r = 0, len(chars) - 1
        while l < r:
            if chars[l] in vowels and chars[r] in vowels:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
            if chars[l] not in vowels:
                l += 1
            if chars[r] not in vowels:
                r -= 1
        return "".join(chars)


def test():
    executors = [TwoPointers]
    tests = [
        ["a", "a"],
        ["ab", "ab"],
        ["abo", "oba"],
        ["hello", "holle"],
        ["leetcode", "leotcede"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.reverseVowels(t[0])
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
