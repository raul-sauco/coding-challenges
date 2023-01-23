# 997. Find the Town Judge
# 🟢 Easy
#
# https://leetcode.com/problems/find-the-town-judge/
#
# Tags: Array - Hash Table - Graph

import timeit
from typing import List


# We can solve this problem using topological sorting, create sets of
# elements that are trusted by the current one and elements that the
# current one trusts, return the element that does not trust any others
# and is trusted by n-1 others.
#
# Time complexity: O(n+t) - Where n is n and t is the number of items
# in the trust array. We iterate over all the elements in trust to
# create the topological sorting, then iterate over a max of n elements
# to find the one that matches the given conditions.
#
# Runtime 736 ms Beats 88.56%
# Memory 18.9 MB Beats 59.7%
class UseSets:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # In and outdegree arrays.
        trusted_by, trusts = [set() for _ in range(n + 1)], [
            set() for _ in range(n + 1)
        ]
        for trustee, trusted in trust:
            trusted_by[trusted].add(trustee)
            trusts[trustee].add(trusted)
        for i in range(1, n + 1):
            if len(trusted_by[i]) == n - 1 and len(trusts[i]) == 0:
                return i
        # We can't determine the judge.
        return -1


# We can solve this problem using topological sorting, count the
# elements that are trusted by the current one and elements that the
# current one trusts, return the element that does not trust any others
# and is trusted by n-1 others.
#
# Time complexity: O(n+t) - Where n is n and t is the number of items
# in the trust array. We iterate over all the elements in trust to
# create the topological sorting, then iterate over a max of n elements
# to find the one that matches the given conditions.
#
# Runtime 726 ms Beats 94.15%
# Memory 18.9 MB Beats 59.7%
class Count:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # In and outdegree arrays.
        trusted_by, trusts = [0] * (n + 1), [0] * (n + 1)
        for trustee, trusted in trust:
            trusted_by[trusted] += 1
            trusts[trustee] += 1
        for i in range(1, n + 1):
            if trusted_by[i] == n - 1 and trusts[i] == 0:
                return i
        # We can't determine the judge.
        return -1


def test():
    executors = [
        UseSets,
        Count,
    ]
    tests = [
        [1, [], 1],
        [2, [[1, 2]], 2],
        [3, [[1, 3], [2, 3]], 3],
        [3, [[1, 3], [2, 3], [3, 1]], -1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findJudge(t[0], t[1])
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
