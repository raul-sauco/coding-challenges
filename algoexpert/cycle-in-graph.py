# Cycle In Graph
# 🟠 Medium
#
# https://www.algoexpert.io/questions/cycle-in-graph
#
# Tags: Graph - Depth-First Search

import timeit


# The nodes can have three states, not visited yet, visited and visited
# along the current path that we are exploring, if we ever visit a node
# that we have already seen in the current path, using depth-first
# search, we have found a cycle and we can immediately return True, if
# we process all nodes without finding a cycle, we can return False. We
# need three states for the nodes because the problem does not guarantee
# that the graph is connected, if we pick one node and complete dfs from
# it, we have no guarantees that we have visited all nodes in the graph.
#
# Time complexity: O(v+e) - We will visit all nodes and travel all edges.
# Space complexity: O(v) - The call stack could grow to the size of the
# input graph.
class Solution:
    def cycleInGraph(self, edges):
        # A set of edges that we have not visited yet.
        unvisited = {i for i in range(len(edges))}
        # A list of edges to mark edges that we have visited along the
        # current path.
        in_path = [False] * len(edges)
        # A DFS function that visits all nodes we can visit from an initial node.
        def dfs(node) -> bool:
            # If we have seen this node along this path, we have a cycle.
            if in_path[node]:
                return True
            # Mark the current node as visited along the current DFS path.
            in_path[node] = True
            # Also mark this node as visited.
            unvisited.discard(node)
            # Then visit all its neighbors.
            for neighbor in edges[node]:
                # Propagate cycle detection and stop the search.
                if dfs(neighbor):
                    return True
            # If we have processed all neighbors without finding a cycle
            # backtrack and return True
            in_path[node] = False
            return False

        while unvisited:
            if dfs(unvisited.pop()):
                return True
        # We have visited all nodes without finding a cycle, return False.
        return False


def test():
    executors = [Solution]
    tests = [
        [[[1, 3], [2, 3, 4], [0], [], [2, 5], []], True],
        [[[1], [2, 3, 4, 5, 6, 7], [], [2, 7], [5], [], [4], []], False],
        [[[1], [2, 3, 4, 5, 6, 7], [], [2, 7], [5], [], [4], [0]], True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.cycleInGraph(t[0])
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
