# 797. All Paths From Source to Target
# 🟠 Medium
#
# https://leetcode.com/problems/all-paths-from-source-to-target/
#
# Tags: Backtracking - Depth-First Search - Breath-First Search - Graph

import timeit
from typing import List

# 10e4 calls.
# » IterativeDFS        0.02985   seconds
# » RecursiveDFS        0.04888   seconds

# Use iterative depth-first search to travel all possible paths from
# 0 to n-1, when we get to n-1 we save the traveled path to the result
# list of paths.
#
# Time complexity: O(n*2^n) - Where n is the number of nodes in the
# input adjacency list. The decision tree splits in two at each level,
# O(2^n) but it also makes a copy of the list to add it to the paths at
# cost O(n) at each step.
# Space complexity: O(v*e) - The stack will hold a list of all possible
# paths in the graph.
#
# Runtime 94 ms Beats 98.10%
# Memory 15.6 MB Beats 78.57%
class IterativeDFS:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # The result array.
        paths = []
        # Use a stack for the depth-first search algorithm.
        stack = [[0]]
        while stack:
            # Pop a path from the stack and use it to visit the next
            # nodes.
            current_path = stack.pop()
            # Use the adjacency list to visit all the neighbors of the
            # last node in the current path.
            for neighbor in graph[current_path[-1]]:
                # If the neighbor is the last node in the graph, we have
                # found a path.
                if neighbor == len(graph) - 1:
                    paths.append(current_path + [neighbor])
                # If the neighbor is not the last node in the graph,
                # keep building the path.
                else:
                    stack.append(current_path + [neighbor])
        return paths


# Use recursive depth-first search to travel all possible paths from
# 0 to n-1, when we get to n-1 we save the traveled path to the result
# list of paths.
#
# Time complexity: O(n*2^n) - Where n is the number of nodes in the
# input adjacency list. The decision tree splits in two at each level,
# O(2^n) but it also makes a copy of the list to add it to the paths at
# cost O(n) at each step.
# Space complexity: O(n) - The call stack will grow to the size of the
# longest path, since the graph is acyclic, the longest path can, at
# most, visit each node once.
#
# Runtime 98 ms Beats 94.50%
# Memory 15.6 MB Beats 97.58%
class RecursiveDFS:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # The result array.
        paths = []
        # The recursive depth-first search function.
        def dfs(current_path: List[int]) -> None:
            for neighbor in graph[current_path[-1]]:
                current_path.append(neighbor)
                if neighbor == len(graph) - 1:
                    paths.append(current_path[:])
                else:
                    dfs(current_path)
                # Backtrack.
                current_path.pop()

        dfs([0])
        return paths


def test():
    executors = [
        IterativeDFS,
        RecursiveDFS,
    ]
    tests = [
        [[[1], []], [[0, 1]]],
        [[[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]],
        [
            [[4, 3, 1], [3, 2, 4], [3], [4], []],
            [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(10000):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.allPathsSourceTarget(t[0])
                exp = t[1]
                result.sort()
                exp.sort()
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
