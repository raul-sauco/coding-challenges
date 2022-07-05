# https://leetcode.com/problems/longest-palindrome/

from collections import Counter, defaultdict
import timeit

# Runtime: 80 ms, faster than 5.54 % of Python3 online submissions for Longest Palindrome.
# Memory Usage: 13.8 MB, less than 97.88 % of Python3 online submissions for Longest Palindrome.


class Loop:
    def longestPalindrome(self, s: str) -> int:
        seen = defaultdict(int)
        # Flag to store whether we have any character in uneven numbers
        seen_uneven = 0
        length = 0
        for c in s:
            seen[c] += 1
        for c in seen:
            # If any of the characters is in an uneven number, we can build an uneven palindrome
            if not seen_uneven and seen[c] % 2 == 1:
                seen_uneven = 1
            # Add 2 per each pair found, discarding other single characters
            length += seen[c] // 2 * 2
        return length + seen_uneven


# Runtime: 62 ms, faster than 22.27% of Python3 online submissions for Longest Palindrome.
# Memory Usage: 13.9 MB, less than 21.85 % of Python3 online submissions for Longest Palindrome.
class ColCounter:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        for char_count in Counter(s).values():
            length += char_count // 2
        length *= 2
        if length < len(s):
            return length + 1
        return length


class CountOdds:
    def longestPalindrome(self, s: str) -> int:
        odds = sum(v & 1 for v in Counter(s).values())
        return len(s) - odds + bool(odds)


def test():
    executors = [
        {'executor': Loop, 'title': 'Loop', },
        {'executor': ColCounter, 'title': 'Counter', },
        {'executor': CountOdds, 'title': 'CountOdds', },
    ]
    tests = [
        ["abccccdd", 7],
        ["abbccccdd", 9],
        ["aAbbccccdd", 9],
        ["aAAbbccccdd", 11],
        ["aaAAbbccccdd", 12],
        ["a", 1],
        ["bb", 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for t in tests:
                sol = executor['executor']()
                result = sol.longestPalindrome(t[0])
                expected = t[1]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(
            executor['title'], used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
