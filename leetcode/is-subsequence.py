# https://leetcode.com/problems/is-subsequence/

import timeit


# Runtime: 48 ms, faster than 57.69% of Python3 online submissions for Is Subsequence.
# Memory Usage: 13.9 MB, less than 44.81 % of Python3 online submissions for Is Subsequence.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if not s:
            return True
        pointer = 0
        for char in t:
            if pointer == len(s):
                return True
            if char == s[pointer]:
                pointer += 1
        return pointer == len(s)


def test():
    executor = [
        {'executor': Solution, 'title': 'Solution', },
    ]
    tests = [
        ["", "", True],
        ["", "abc", True],
        ["b", "abc", True],
        ["d", "abcabcabcabcabcd", True],
        ["d", "abcabcabcabcabc", False],
        ["abc", "ahbgdc", True],
        ["axc", "ahbgdc", False],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for t in tests:
                sol = e['executor']()
                result = sol.isSubsequence(t[0], t[1])
                expected = t[2]
                assert result == expected, f'{result} != {expected} for {t[0]}:{t[1]} using {e["title"]} solution'
        used = str(round(timeit.default_timer() - start, 5))
        result = "{0:20}{1:10}{2:10}".format(e['title'], used, "seconds")
        print(f"\033[92m» {result}\033[0m")


test()
