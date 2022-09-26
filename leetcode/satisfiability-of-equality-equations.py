# 990. Satisfiability of Equality Equations
# 🟠 Medium
#
# https://leetcode.com/problems/satisfiability-of-equality-equations/
#
# Tags: Array - String - Union Find - Graph

import timeit
from string import ascii_lowercase
from typing import List


# Use union find, iterate once over the equations using equality
# functions to determine which symbols belong on the same disjoint set,
# then iterate again over the equations using inequality functions to
# determine if any two symbols that need to be unequal belong to the
# same disjoint set, if any pair does, return False.
#
# Time complexity: O(n) - We iterate over the input twice, for each
# element we do O(1) operations in both, the union find algorithm is
# amortized O(1) but, since it has a max depth of 26, we can see
# consider it O(1).
# Space complexity: O(1) - We keep a dictionary of operand: value pairs
# that can grow to size 26, the number of possible operands.
#
# Runtime: 63 ms, faster than 73.09%
# Memory Usage: 14.1 MB, less than 69.95%
class UnionFind:
    def equationsPossible(self, equations: List[str]) -> bool:
        # A dictionary of characters pointing to their disjoint set
        # parent.
        parents = dict(zip(ascii_lowercase, ascii_lowercase))

        # Define a function that finds the parent of a given character.
        def findParent(char: str) -> str:
            if parents[char] == char:
                return char
            parents[char] = findParent(parents[char])
            return parents[char]

        # Define a function that merges two characters into the same set.
        def group(a: str, b: str) -> None:
            parents[findParent(a)] = findParent(b)

        # Iterate over the input equations using equality functions to
        # create a disjoint set structure.
        for l, e, _, r in equations:
            if e == "=":
                group(l, r)

        # Iterate again over the input equations, this time using
        # inequality functions to check that two unequal elements do
        # not belong to the same set.
        for l, e, _, r in equations:
            if e == "!" and findParent(l) == findParent(r):
                return False

        # If we didn't find any contradiction, return True
        return True


def test():
    executors = [UnionFind]
    tests = [
        [["b!=b"], False],
        [["a==b", "b!=a"], False],
        [["b==a", "a==b"], True],
        [
            ["a==b", "c!=a", "c==d", "e!=f", "z==a", "z!=v", "m!=o", "o==a"],
            True,
        ],
        [
            ["a==b", "c!=a", "c==d", "e!=f", "d==a", "z!=v", "m!=o", "o==a"],
            False,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.equationsPossible(t[0])
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
