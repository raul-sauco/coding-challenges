# 2405. Optimal Partition of String
# 🟠 Medium
#
# https://leetcode.com/problems/optimal-partition-of-string/
#
# Tags: Hash Table - String - Greedy

import timeit


# Keep a hashmap, or a vector of indexes indexed by character, of the
# last position at which we have seen a given character, also
# save the start index of the current partition that we are building,
# then iterate over the characters in the input, if we see a character
# that is contained in the current partition, we need to start a new
# one.
#
# Time complexity: O(n) - We iterate over the characters in the input
# string and do constant time work for each.
# Space complexity: O(1) - We use constant extra space, pointers and a
# vector of size 26.
#
# Runtime 140 ms Beats 39.45%
# Memory 14.6 MB Beats 47.10%
class Solution:
    def partitionString(self, s: str) -> int:
        res, start = 1, 0
        last_seen = [-1] * 26
        for i, c in enumerate(s):
            idx = ord(c) - ord("a")
            if last_seen[idx] >= start:
                res += 1
                start = i
            last_seen[idx] = i
        return res


def test():
    executors = [Solution]
    tests = [
        ("abccba", 2),
        ("ssssss", 6),
        ("abacaba", 4),
        ("oygwwncfgewspmqvbez", 3),
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.partitionString(t[0])
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
