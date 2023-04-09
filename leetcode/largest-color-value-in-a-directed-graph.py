# 1857. Largest Color Value in a Directed Graph
# 🔴 Hard
#
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
#
# Tags: Hash Table - Dynamic Programming - Graph - Topological Sort
# - Memoization - Counting

import json
import os
import timeit
from typing import List


# Traverse all edges creating two structures, an adjacency list and an
# array of indegrees, starting at each node that has an indegree of 0,
# meaning that it could be the root of a tree in the forest, depth-first
# search to travel all paths of the current tree, each node returns a
# list of length 26 with the highest path frequency of each color in the
# subtree rooted at the given node.
#
# Time complexity: O(e+v) - Where e is the number of edges and v the
# number of vertices, we iterate all the edges and may iterate all nodes
# for each we iterate over all neighbor's and colors 26.
# Space complexity: O(n) - The call stack may hold n calls, each call
# returns an array of size 26.
#
# Runtime 2717 ms Beats 48.81%%
# Memory 198 MB Beats 13.10%%
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        # Use a manual cache.
        cache = [None] * n
        # Store an adjacency list.
        adj = [[] for _ in range(n)]
        # Compute the indegree of all nodes.
        indegree = [0] * n
        for src, dest in edges:
            adj[src].append(dest)
            indegree[dest] += 1
        # The nodes that we have visited along the current path.
        path = set()
        # A function that does DFS from a given node and returns an
        # array with the highest frequencies for each color in the
        # subtree rooted at node.
        def dfs(node) -> List[int] | int:
            # If we see a node that we have visited along the current
            # path, we have a cycle.
            if node in path:
                return -1
            # If this is a cache hit return that.
            if cache[node]:
                return cache[node]
            path.add(node)
            # Initialize the color frequencies that are in this subtree.
            f = [0] * 26
            children = adj[node]
            # If this children is not a leaf, process children.
            for child in children:
                child_res = dfs(child)
                # Cycle detection.
                if child_res == -1:
                    return -1
                # Else, use the highest freq for each color in this
                # subtree because we can always choose the optimal
                # path below this node.
                f = [max(child_res[i], f[i]) for i in range(len(f))]

            # Now backtrack.
            path.remove(node)
            # Add this node's color to the frequencies.
            f[ord(colors[node]) - ord("a")] += 1
            cache[node] = f
            return f

        # Initialize the color frequencies that are in the forest.
        f = [0] * 26
        # The longest paths will be between tree roots and leaves, only
        # start DFS on tree roots, if we don't have any, we have cycles.
        for node in range(n):
            if indegree[node] == 0:
                path_res = dfs(node)
                if path_res == -1:
                    return -1
                f = [max(path_res[i], f[i]) for i in range(len(f))]
                cache[node] = f
        # If we have not visited all the nodes, there was a cyclic
        # component in which none of the nodes had an indegree of 0 that
        # we have not visited.
        if not all(cache):
            return -1
        # Otherwise, check the max of the frequencies.
        res = max(f)
        return res if res > 0 else -1


# TODO look into the topological sort solution.


def test():
    executors = [
        Solution,
    ]
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(
        os.path.join(
            __location__, "largest-color-value-in-a-directed-graph.json"
        )
    ) as json_file:
        tests = json.load(json_file)
        for executor in executors:
            start = timeit.default_timer()
            for _ in range(1):
                for col, t in enumerate(tests):
                    sol = executor()
                    result = sol.largestPathValue(t[0], t[1])
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
