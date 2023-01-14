# 1061. Lexicographically Smallest Equivalent String
# 🟠 Medium
#
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
#
# Tags: String - Union Find

import timeit


# Use union find by rank where the rank is the reversed lexicographical
# order of the characters to be joined.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input, we visit all characters in s1 and s2 to construct the union
# find structure, then we visit all characters in base str to find their
# lexicographically smallest equivalents, the find parent operation runs
# in amortized O(1) because it uses path compression.
# Space complexity: O(1) - The parents dictionary can grow to size 26.
#
# Runtime 39 ms Beats 93.68%
# Memory 13.9 MB Beats 94.83%
class UseHashMap:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # A function that finds the representative of a disjoint set, in
        # this case the representative consists of the lexicographically
        # smallest member of the group.
        def findParent(a: str) -> str:
            if a not in parents:
                parents[a] = a
                return parents[a]
            if parents[a] == a:
                return a
            parents[a] = findParent(parents[a])
            return parents[a]

        # Merge two disjoint sets into one with the lexicographically
        # smaller parent as the parent of the merged result.
        def union(a: str, b: str) -> None:
            pa, pb = findParent(a), findParent(b)
            if ord(pa) > ord(pb):
                pa, pb = pb, pa
            parents[pb] = pa

        parents = {}
        # Find all the disjoint groups.
        for i in range(len(s1)):
            union(s1[i], s2[i])
        # Use the disjoint groups to update every character in base str
        # to the lexicographically lowest equivalent.
        res = [None] * len(baseStr)
        for i in range(len(baseStr)):
            res[i] = findParent(baseStr[i])
        return "".join(res)


# Improve the previous solution using an array instead of a dictionary.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input, we visit all characters in s1 and s2 to construct the union
# find structure, then we visit all characters in base str to find their
# lexicographically smallest equivalents, the find parent operation runs
# in amortized O(1) because it uses path compression.
# Space complexity: O(1) - The parents array is of size 26.
#
# Runtime 27 ms Beats 99.43%
# Memory 13.9 MB Beats 94.83%
class UseArray:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # A function that finds the representative of a disjoint set, in
        # this case the representative consists of the lexicographically
        # smallest member of the group.
        def findParent(a: str) -> str:
            idx = ord(a) - 97
            if parents[idx] != a:
                parents[idx] = findParent(parents[idx])
            return parents[idx]

        # Merge two disjoint sets into one with the lexicographically
        # smaller parent as the parent of the merged result.
        def union(a: str, b: str) -> None:
            pa, pb = findParent(a), findParent(b)
            if pa > pb:
                pa, pb = pb, pa
            parents[ord(pb) - 97] = pa

        # Initialize an array of parents.
        parents = [chr(i + ord("a")) for i in range(26)]
        # Find all the disjoint groups.
        for i in range(len(s1)):
            union(s1[i], s2[i])
        # Use the disjoint groups to update every character in base str
        # to the lexicographically lowest equivalent.
        res = [None] * len(baseStr)
        for i in range(len(baseStr)):
            res[i] = findParent(baseStr[i])
        return "".join(res)


def test():
    executors = [
        UseHashMap,
        UseArray,
    ]
    tests = [
        ["parker", "morris", "parser", "makkek"],
        ["hello", "world", "hold", "hdld"],
        ["leetcode", "programs", "sourcecode", "aauaaaaada"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.smallestEquivalentString(t[0], t[1], t[2])
                exp = t[3]
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
