# 839. Similar String Groups
# 🔴 Hard
#
# https://leetcode.com/problems/similar-string-groups/
#
# Tags: Array - String - Depth-First Search - Breadth-First Search - Union Find

import timeit
from typing import List


# Create a disjoint set data structure. Iterate over every pair of
# input strings O(n^2) checking if they are similar by checking the
# number of positions at which they have different characters, when the
# strings are similar, we join their sets since we are guaranteed that
# we can use this pair to connect any other strings in their current
# disjoint groups. The answer is the number of disjoint groups.
#
# Time complexity: O(m*n^2) - Where m is the number of characters of the
# input strings, they all have the same, and n is the number of input
# strings. We iterate over a pair of inputs, for each pair, we check
# m positions for equality.
# Space complexity: O(n) - Parents and ranks arrays have size n.
#
# Runtime 2875 ms Beats 13.77%
# Memory 16.6 MB Beats 10.16%
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        m, n = len(strs[0]), len(strs)
        parents = [i for i in range(n)]
        rank = [1] * n

        # Find function.
        def findParent(a: int) -> int:
            if parents[a] == a:
                return a
            # Use path compression, following calls will be O(1)
            parents[a] = findParent(parents[a])
            return parents[a]

        # Union by rank function.
        def union(a: int, b: int) -> None:
            # Find the parents.
            pa, pb = findParent(a), findParent(b)
            # Custom break, we may be calling union with elements that
            # are already in the same disjoint set. This only affects
            # the union by rank, it would not give a wrong result.
            if pa == pb:
                return
            if rank[pb] > rank[pa]:
                pa, pb = pb, pa
            parents[pb] = pa
            rank[pa] += rank[pb]

        # Construct the disjoint set element.
        for i in range(n):
            for j in range(i + 1, n):
                # If the strings are similar, none or 2 changes.
                changes = sum(1 for c in range(m) if strs[i][c] != strs[j][c])
                if not changes or changes == 2:
                    union(i, j)
        return len(set([findParent(x) for x in range(n)]))


def test():
    executors = [Solution]
    tests = [
        [["omv", "ovm"], 1],
        [["tars", "rats", "arts", "star"], 2],
        [
            [
                "ajdidocuyh",
                "djdyaohuic",
                "ddjyhuicoa",
                "djdhaoyuic",
                "ddjoiuycha",
                "ddhoiuycja",
                "ajdydocuih",
                "ddjiouycha",
                "ajdydohuic",
                "ddjyouicha",
            ],
            2,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numSimilarGroups(t[0])
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
