# 886. Possible Bipartition
# 🟠 Medium
#
# https://leetcode.com/problems/possible-bipartition/
#
# Tags: Depth-First Search - Breadth-First Search - Union Find - Graph

import timeit
from collections import defaultdict
from typing import List


# Use depth-first search to visit nodes related to any unassigned pair.
# A solution using BFS would be almost the same but using a queue
# instead of the stack in the inner function to queue nodes.
#
# Time complexity: O(n+e) - We iterate over all nodes once, for each
# node, we visit all the edges.
# Space complexity: O(n+e) - All the structures have a linear relation
# to the number of nodes in the input, except for the adjacency list
# that holds a list of outgoing edges for each node.
#
# Runtime 720 Beats 94.23%
# Memory 19.9 MB Beats 92.70%
class DFS:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Since we only need three states for the groups, unassigned, a
        # or b, we can use none and booleans values.
        group = [None] * (n + 1)
        dislikes_map = [[] for _ in range(n + 1)]
        for disliker, disliked in dislikes:
            dislikes_map[disliker].append(disliked)
            dislikes_map[disliked].append(disliker)
        # A function that uses BFS to explore all of a person's dislikes.
        def dfs(person: int) -> bool:
            stack = [person]
            while stack:
                current = stack.pop()
                for disliked in dislikes_map[current]:
                    if group[disliked] is None:
                        group[disliked] = not group[current]
                        stack.append(disliked)
                    elif group[current] == group[disliked]:
                        return False
                    # If disliked has the opposite group, skip it.
            return True

        # Iterate over the people in the array.
        for person in range(1, n + 1):
            # If the current person has not been assigned to a group,
            # assign them now.
            if group[person] is None:
                group[person] = True
            # Then run DFS, it could also be BFS, to make sure all their
            # disliked people can go to other groups, do it recursively.
            if dfs(person) is False:
                return False
        return True


# Similar solution that uses union find to group nodes, if the nodes in
# any of the input dislike arrays have the same parent node, we cannot
# split them into two groups.
#
# Time complexity: O(n+e) - We iterate over all nodes once, for each
# node, we visit all the edges.
# Space complexity: O(n+e) - All the structures have a linear relation
# to the number of nodes in the input, except for the adjacency list
# that holds a list of outgoing edges for each node.
#
# Runtime 1257 Beats 63.72%
# Memory 20 MB Beats 80.54%
class UnionFind:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        parents = [i for i in range(n + 1)]
        rank = [1 for _ in range(n + 1)]

        def findParent(a: int) -> int:
            if parents[a] == a:
                return a
            # Path compression.
            parents[a] = findParent(parents[a])
            return parents[a]

        def union(a: int, b: int) -> None:
            pa, pb = findParent(a), findParent(b)
            if pa == pb:
                return
            if rank[pa] < rank[pb]:
                pa, pb = pb, pa
            parents[pb] = pa
            rank[pa] += pb

        d = defaultdict(list)
        for a, b in dislikes:
            d[a].append(b)
            d[b].append(a)

        for current in range(1, n + 1):
            for disliked in d[current]:
                if findParent(current) == findParent(disliked):
                    return False
                union(d[current][0], disliked)
        return True


def test():
    executors = [
        DFS,
        UnionFind,
    ]
    tests = [
        [4, [[1, 2], [1, 3], [2, 4]], True],
        [3, [[1, 2], [1, 3], [2, 3]], False],
        [5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], False],
        [5, [[4, 5], [1, 2], [2, 3], [3, 4], [1, 5]], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.possibleBipartition(t[0], t[1])
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
