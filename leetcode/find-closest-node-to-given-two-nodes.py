# 2359. Find Closest Node to Given Two Nodes
# 🟠 Medium
#
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
#
# Tags: Depth-First Search - Breadth-First Search - Graph

import timeit
from typing import List


# We can compute the distance between the start nodes and all other
# nodes using BFS, since the nodes have, at most, one outgoing edge, we
# don't need to use a queue or stack and can simply keep a pointer to
# the next node. Compute all distances from one of the start nodes, then
# compute the distances from the other node while checking if the
# current node has the minimum maximal distance to either node1 or node2.
#
# Time complexity: O(n) - We iterate twice over a max of all the nodes
# in the input.
# Space complexity: O(n) - We keep two arrays of size n and a few
# pointers.
#
# Runtime 1070 ms Beats 91.95%
# Memory 28.9 MB Beats 77.59%
class BFSPointers:
    def closestMeetingNode(
        self, edges: List[int], node1: int, node2: int
    ) -> int:
        # Initialize the best node and distance.
        res = (float("inf"), -1)
        # Arrays with the distances between the input nodes and all
        # the rest.
        d1 = [float("inf")] * len(edges)
        d2 = [float("inf")] * len(edges)
        # d2 = [float("inf")] * len(edges)
        steps, current = 0, node1
        # While we have a current node that we have not visited already.
        while current != -1 and d1[current] == float("inf"):
            d1[current] = steps
            steps += 1
            current = edges[current]
        steps, current = 0, node2
        # Travel the graph from node2 while checking the best distance
        # from both nodes.
        while current != -1 and d2[current] == float("inf"):
            d2[current] = steps
            dist = max(steps, d1[current])
            if dist < res[0] or (
                dist != float("inf") and dist == res[0] and current < res[1]
            ):
                res = (dist, current)
            steps += 1
            current = edges[current]
        return res[1]


def test():
    executors = [
        BFSPointers,
    ]
    tests = [
        [[1, 2, -1], 0, 2, 2],
        [[2, 2, 3, -1], 0, 1, 2],
        [[4, 4, 4, 5, 1, 2, 2], 1, 1, 1],
        [[5, 4, 5, 4, 3, 6, -1], 0, 1, -1],
        [[4, 4, 8, -1, 9, 8, 4, 4, 1, 1], 5, 6, 1],
        [
            [-1, 7, 15, 15, -1, 4, 16, 2, 16, 7, 11, 6, 10, 4, 9, 1, 14, -1],
            1,
            6,
            7,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.closestMeetingNode(t[0], t[1], t[2])
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
