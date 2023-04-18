# 1768. Merge Strings Alternately
# 🟢 Easy
#
# https://leetcode.com/problems/merge-strings-alternately/
#
# Tags: Two Pointers - String

import timeit


# Iterate over characters in word1 and word2 alternatively until we
# consume one, or both, of them. If we have only consumed one of them,
# append the remainder of the other to the end of the result.
#
# Time complexity: O(m+n) - We iterate over all characters in both input
# strings.
# Space complexity: O(m+n) - We store all characters in extra memory.
#
# Runtime 27 ms Beats 90.33%
# Memory 13.8 MB Beats 55.13%
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        res = []
        for i in range(min(m, n)):
            res.append(word1[i])
            res.append(word2[i])
        # Append whatever is left of the other string.
        if m > n:
            res += word1[n:]
        elif n > m:
            res += word2[m:]
        return "".join(res)


def test():
    executors = [Solution]
    tests = [
        ["abc", "pqr", "apbqcr"],
        ["ab", "pqrs", "apbqrs"],
        ["abcd", "pq", "apbqcd"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.mergeAlternately(t[0], t[1])
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
