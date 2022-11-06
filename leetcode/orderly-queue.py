# 899. Orderly Queue
# 🔴 Hard
#
# https://leetcode.com/problems/orderly-queue/
#
# Tags: Math - String - Sorting

import timeit

# When k is at least 2, we will be able to sort the input string
# completely, and return the smallest lexicographical string, we only
# need to handle the case when k == 1. In that special case, we can only
# rotate the string and have to check which is the rotation that leads
# to the smallest lexicographical string. Booth's algorithm computes
# that in O(n).
# https://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation
#
# Time complexity: O(n*log(n)) - Where n is the number of characters in
# the input. The case k == 1 can be solved in O(n) but the more general
# case requires sorting the input.
# Space complexity: O(n) - Sorting in python can take up to n/2 space.
#
# Runtime: 57 ms, faster than 65.48%
# Memory Usage: 13.9 MB, less than 39.29%
class Solution:
    # An implementation of Booth's algorithm from Wikipedia.
    def booth(self, s: str) -> str:
        n = len(s)
        f = [-1] * (2 * n)
        k = 0
        for j in range(1, 2 * n):
            i = f[j - k - 1]
            while i != -1 and s[j % n] != s[(k + i + 1) % n]:
                if s[j % n] < s[(k + i + 1) % n]:
                    k = j - i - 1
                i = f[i]
            if i == -1 and s[j % n] != s[(k + i + 1) % n]:
                if s[j % n] < s[(k + i + 1) % n]:
                    k = j
                f[j - k] = -1
            else:
                f[j - k] = i + 1
        # k is the number of rotations that will lead to the result.
        return s[k:] + s[:k]

    def orderlyQueue(self, s: str, k: int) -> str:
        return "".join(sorted(s)) if k > 1 else self.booth(s)


def test():
    executors = [Solution]
    tests = [
        ["cba", 1, "acb"],
        ["baaca", 3, "aaabc"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.orderlyQueue(t[0], t[1])
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
