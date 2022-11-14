# 947. Most Stones Removed with Same Row or Column
# 🟠 Medium
#
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
#
# Tags: Depth-First Search - Union Find - Graph

import timeit
from collections import defaultdict
from typing import List, Tuple


# We can remove all stones except the last one, out of any groups that
# share row/column at any point. Then the algorithm becomes finding out
# how many groups there are and returning len(stones) - len(groups)
#
# Time complexity: O(n) - Union find by rank with path compression has
# an amortized O(1) time complexity per union, and we do n unions where
# n is the number of stones in the input. Iterating over the stones
# adding each of them to the row and col dictionary is O(1) per stone.
# Space complexity: O(n) - We store one entry in the parents dictionary,
# one in the row dictionary and one in the column dictionary per stone.
#
# Runtime: 422 ms, faster than 46.48%
# Memory Usage: 15.2 MB, less than 34.06%
class UnionFindLong:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Find function with path compression.
        def findParent(a: Tuple[int]) -> Tuple[int]:
            if parents[a] == a:
                return a
            parents[a] = findParent(parents[a])
            return parents[a]

        # Union by rank.
        def union(a: Tuple[int], b: Tuple[int]) -> None:
            pa, pb = findParent(a), findParent(b)
            if rank[pa] > rank[pb]:
                pa, pb = pb, pa
            parents[pb] = findParent(pa)
            rank[pa] += rank[pb]

        # Parents dictionary: (row, col): (row, col)
        parents = {}
        # Rank dictionary: (row, col): rank
        rank = {}
        # Group all stones by row and column.
        row_stones, col_stones = defaultdict(list), defaultdict(list)
        for row, col in stones:
            row_stones[row].append(col)
            col_stones[col].append(row)
            parents[row, col] = (row, col)
            rank[row, col] = 1
        # Group all stones with the same row.
        for row in row_stones.keys():
            a = (row, row_stones[row][0])
            for col in row_stones[row][1:]:
                union(a, (row, col))
        # Group all stones with the same column.
        for col in col_stones.keys():
            a = (col_stones[col][0], col)
            for row in col_stones[col][1:]:
                union(a, (row, col))
        # We will be able to remove all stones except the last one from
        # every disjoint group.
        return len(stones) - len({findParent(key) for key in parents.keys()})


# Looking at the previous, complicated, solution, we can see a few
# places where we can make optimizations, the biggest one is that we are
# treating row and column groups as separate entities until the very end,
# if we could combine them earlier, it would make the algorithm simpler,
# we can union the row and column groups of any element that we find as
# they are guaranteed to be connected by this element, to differentiate
# the row and column numbers as group leaders, we can negate all column
# indexes.
#
# Time complexity: O(n) - Union find by rank with path compression has
# an amortized O(1) time complexity per union, and we do n unions where
# n is the number of stones in the input.
# Space complexity: O(n) - We store one entry in the parents dictionary
# per stone.
#
# Runtime: 377 ms, faster than 57.85%
# Memory Usage: 14.7 MB, less than 72.25%
class UnionFindShort:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Find parent function with path compression.
        def findParent(a: int) -> int:
            if a != parents[a]:
                parents[a] = findParent(parents[a])
            return parents[a]

        # Union by rank function.
        def union(a: int, b: int) -> None:
            # If not in the dictionary yet, add them.
            if a not in parents:
                parents[a], rank[a] = a, 1
            if b not in parents:
                parents[b], rank[b] = b, 1
            pa, pb = findParent(a), findParent(b)
            if rank[pa] > rank[pb]:
                pa, pb = pb, pa
            parents[pb] = findParent(pa)
            rank[pa] += rank[pb]

        # Parents dictionary: idx: idx. Rank: idx: rank
        parents, rank = {}, {}
        # Iterate over the stones calling union on them.
        for row, col in stones:
            union(row, ~col)
        return len(stones) - len({findParent(el) for el in parents})


def test():
    executors = [
        UnionFindLong,
        UnionFindShort,
    ]
    tests = [
        [[[0, 0]], 0],
        [[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]], 3],
        [[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]], 5],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.removeStones(t[0])
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
