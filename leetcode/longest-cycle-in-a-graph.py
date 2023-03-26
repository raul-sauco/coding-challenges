# 2360. Longest Cycle in a Graph
# 🔴 Hard
#
# https://leetcode.com/problems/longest-cycle-in-a-graph/
#
# Tags: Depth-First Search - Graph - Topological Sort

import timeit
from typing import List


# Use depth-first search starting from every node, keep visited nodes in
# a set to make sure we only visit each node once. Keep also a hashmap
# of sets that we have visited along the current path pointing to the
# position along the path at which we saw them, if we see a node that we
# already saw in the current path, we have found a cycle, the size of
# the cycle is the difference between the two positions at which we
# found the current node, if we get to a node that does not have any
# outbound edges, we can return 0 because the path will not have any
# cycles.
#
# Time complexity: O(n) - We visit each node once and do O(1) work,
# once a node is visited along one path, we will not visit it from
# another path, if a path leads to a node that was visited already, it
# will stop there.
# Space complexity: O(n) - The list of visited nodes and the dictionary
# of nodes seen along the path can both be of size n.
#
# Runtime 1328 ms Beats 72.28%
# Memory 157.9 MB Beats 36.76%
class DFS:
    def longestCycle(self, edges: List[int]) -> int:
        # A set of nodes that we have visited already.
        visited = [False] * len(edges)
        # The longest cycle seen so far.
        res = 0
        # A function that explores a path starting at a given node.
        def dfs(node: int, pos: int) -> int:
            # If we have seen this same node along this same path,
            # compute the length of the cycle, reset the path and exit.
            if node in path:
                return pos - path[node]
            # If we have seen this node as part of some other path, we
            # would have already found the longest cycle.
            if visited[node]:
                return 0
            # Mark this node as visited and travel to its child if any.
            path[node] = pos
            visited[node] = True
            if edges[node] != -1:
                return dfs(edges[node], pos + 1)
            return 0

        # Call the function starting at each node.
        for i in range(len((edges))):
            if not visited[i]:
                # A hashmap of nodes that we have seen along the current
                # path indexing the position along the path at which we
                # saw them.
                path = {}
                res = max(res, dfs(i, 0))
        return res if res > 0 else -1


def test():
    executors = [DFS]
    tests = [
        [[2, -1, 3, 1], -1],
        [[3, 3, 4, 2, 3], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.longestCycle(t[0])
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
