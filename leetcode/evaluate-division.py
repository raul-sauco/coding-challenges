# 399. Evaluate Division
# 🟠 Medium
#
# https://leetcode.com/problems/evaluate-division/
#
# Tags: Array - Depth-First Search - Breadth-First Search - Union Find
# - Graph - Shortest Path

import timeit
from collections import defaultdict, deque
from typing import List


# Use the equations and values to construct an adjacency list, when we
# get a query, compute the shortest path between src and dest.
#
# TODO: Make a more robust version of this solution, a union find
# structure could be used to quickly determine if the nodes are
# connected. BFS is guaranteed to return a correct answer because the
# description tells us that there are not contradictions, if we obtained
# a different result going through another path, that would be a
# contradiction and would break that premise.
#
# Time complexity: O(n*(e+v)) - Where n is the number of queries, e is
# the number of edges and v is the number of nodes, vertices. For each
# of the n calls to bfs, we run a BFS over the entire graph that could
# visit v vertices and e edges. We could improve this storing results or
# computing the distance between all nodes once and storing that in a
# matrix. It would be necessary if the search space was greater.
# Space complexity: O(n) - The adjacency matrix will have the same
# number of entries as the equations and values arrays times 2.
#
# Runtime 44 ms Beats 31.85%
# Memory 16.4 MB Beats 25.75%
class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        # Construct an adjacency list with the given equations and
        # distances.
        adj = defaultdict(list)
        for (x, y), val in zip(equations, values):
            adj[x].append((y, val))
            adj[y].append((x, 1 / val))

        # Find the shortest way between src and dest.
        def bfs(src, dest):
            if src not in adj or dest not in adj:
                return -1
            q, visited = deque(), set()
            q.append([src, 1])
            while q:
                cur, total_weight = q.popleft()
                if cur == dest:
                    return total_weight
                for nei, edge_weight in adj[cur]:
                    if nei not in visited:
                        q.append([nei, total_weight * edge_weight])
                        visited.add(nei)
            return -1

        return [bfs(a, b) for a, b in queries]


def test():
    executors = [Solution]
    tests = [
        [
            [["a", "b"]],
            [0.5],
            [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
            [0.50000, 2.00000, -1.00000, -1.00000],
        ],
        [
            [["a", "b"], ["c", "d"]],
            [1.0, 1.0],
            [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]],
            [-1.00000, -1.00000, 1.00000, 1.00000],
        ],
        [
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            [6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
        ],
        [
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            [3.75000, 0.40000, 5.00000, 0.20000],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.calcEquation(t[0], t[1], t[2])
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
