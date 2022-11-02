# 1971. Find if Path Exists in Graph
# 🟢 Easy
#
# https://leetcode.com/problems/find-if-path-exists-in-graph/
#
# Tags: Depth-First Search - Breadth-First Search - Union Find - Graph

import timeit
from collections import defaultdict, deque
from typing import List

# 1e4 calls
# » BFS                 0.02536   seconds
# » UnionFind           0.03754   seconds

# Use Breadth-First search, start at the source node and queue all
# neighbors, recursively queue their neighbors, marking them as seen,
# until we either arrive at the destination vertex or run out of
# vertexes to explore.
#
# Time complexity: O(n) - We will visit each node once at max.
# Space complexity: O(n) - The queue will grow to O(v) depending on the
# connectivity of the graph, but the seen set could grow to the same
# size as the input - 1 if there were no path from source to destination.
#
# Runtime: 4163 ms, faster than 16.83%
# Memory Usage: 116.2 MB, less than 35.30%
class BFS:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        # Iterate over the edges adding edges creating a dictionary of
        # neighbors.
        neighbors = defaultdict(set)
        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)
        q = deque([source])
        # Keep processing nodes that we can arrive at.
        while q:
            current = q.popleft()
            # If this is the destination, return True
            if current == destination:
                return True
            # Process this node's neighbors if it has any and has not
            # been processed already.
            if current in neighbors:
                # Append this node's neighbors to the queue.
                q.extend(neighbors[current])
                # Mark this node as processed by removing its entry from
                # the dictionary.
                del neighbors[current]
        # If we could not arrive at the destination, return false.
        return False


# We are only interested in determining whether two vertexes are
# connected or not, we can use union find and compare the two nodes
# parents, if the parents are the same, the nodes are connected.
#
# Time complexity: O(e*log(v)) - We iterate over all the edges, for each
# edge we need to find the parents of both vertex connected by the edge,
# this will initially require up to v calls to find parent where v is the
# number of vertexes between the current ones and their parents, but, as
# more vertexes are grouped, we will start to hit parents as immediately
# averaging O(log(v)) per parent find.
# Space complexity: O(n) - The parents array is of size n.
#
# Runtime: 2154 ms, faster than 87.71%
# Memory Usage: 102.5 MB, less than 97.06%
class UnionFind:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        # Define an array that stores the parent of each node,
        # initially each node has itself as a parent.
        parents = [x for x in range(n)]

        # Define a function that finds the parent of a given node.
        def findParent(node: int) -> int:
            if parents[node] == node:
                return node
            return findParent(parents[node])

        # Define a function that puts two nodes in the same group.
        def group(a: int, b: int) -> None:
            parent_a = findParent(a)
            parent_b = findParent(b)
            parents[parent_a] = parent_b

        # Iterate over all the edges grouping them into connected
        # components.
        for a, b in edges:
            group(a, b)
        # The nodes are connected if they have the same parent.
        return findParent(source) == findParent(destination)


def test():
    executors = [
        BFS,
        UnionFind,
    ]
    tests = [
        [3, [[0, 1], [1, 2], [2, 0]], 0, 2, True],
        [6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.validPath(t[0], t[1], t[2], t[3])
                exp = t[4]
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
