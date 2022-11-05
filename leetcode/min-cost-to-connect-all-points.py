# 1584. Min Cost to Connect All Points
# 🟠 Medium
#
# https://leetcode.com/problems/min-cost-to-connect-all-points/
#
# Tags: Array - Union Find - Minimum Spanning Tree

import timeit
from heapq import heapify, heappop, heappush
from typing import List


# Compute the Manhattan distance between all pairs of points, and store
# it in a list, heapify the list based on distance between points then
# start popping edges from the heap, if the two vertexes, points, at the
# ends of the edge we pop are not connected, we connect them and add the
# edge's weight to the result. We can use the union find algorithm to
# detect if the edges are connected and to connect them if they aren't,
# this algorithm should be efficient because we greedily choose the
# edges with the least weight and use them to build disjoint sets of
# points that we can connect as soon as an edge between them appears.
# We know that this edge will form part of the minimum spanning tree
# because we explore edges with less weight first. We can stop the
# algorithm as soon as we find n-1 edges, where n is the number of
# points.
#
# Time complexity: O(n^2) - Finding the distance between all vertexes is
# the step with the highest complexity. Heapify is O(n) and popping from
# the heap O(n*2log(n)) because we pop n-1 times and the size of the
# heap is n^2 hence each pop is 2*log(n).
# Space complexity: O(n^2) - The heap contains (n-1)^2 edges.
#
# Runtime: 958 ms, faster than 99.8%
# Memory Usage: 78.9 MB, less than 80.84%
class Kruskal:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        # Create a parents data structure, right now all points belong
        # to their own disjoint set of which they are the parent.
        parents = [i for i in range(len(points))]
        # Each set has one member at the start.
        rank = [1 for _ in range(len(points))]
        # Define a function that finds the parent of a point.
        def find(a: int) -> int:
            if parents[a] == a:
                return a
            # Path compression.
            parents[a] = find(parents[a])
            return parents[a]

        # Define a function that groups two nodes under the same parent.
        def union(a: int, b: int) -> None:
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if rank[pb] > rank[pa]:
                pa, pb = pb, pa
            parents[pb] = pa
            rank[pa] += rank[pb]

        costs = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                # Compute the manhattan distance between i and j.
                cost = abs(points[i][0] - points[j][0]) + abs(
                    points[i][1] - points[j][1]
                )
                costs.append((cost, i, j))
        # Heapify the costs.
        heapify(costs)
        # Store the result.
        res = 0
        # The number of edges that we need to find.
        found = len(points) - 1

        while costs:
            weight, a, b = heappop(costs)
            # If this points are not connected yet, connect them.
            if find(a) != find(b):
                union(a, b)
                res += weight
                found -= 1
                # Return the result as soon as we have added n-1 edges.
                # All points will be connected with minimum cost.
                if not found:
                    return res


# Use Prim's algorithm, start choosing any point in the set, mark all
# the other points as not visited. While there are points unvisited,
# calculate all the Manhattan distances between the current point and
# all the unvisited points and add them to the heap, then pop any
# distances with a destination point that has already been visited, use
# the first distance to an unvisited point to mark that point as visited
# and the next current point and add the edge to the total weight of the
# MST. Once there are not remaining nodes to visit, return the result.
#
# Time complexity: O(n^2) - While there are remaining nodes, we compute
# all the distances between the current node and the unvisited nodes,
# this means that we end up computing the distances between all nodes,
# same as with Kruskal's algorithm. Pushing and popping from the heap
# is more efficient because it contains less edges in average.
# Space complexity: O(n^2) - The unvisited set contains n-1 nodes, the
# heap could contain (n-1)^2 edges though in average it will contain
# less than that because in each iteration we only add n-1 edges max and
# we pop some of them.
#
# Runtime: 1677 ms, faster than 92.69%
# Memory Usage: 66 MB, less than 91.27%
class Prim:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Use a priority queue to store (cost, dest_point)
        heap = []
        # Initialize the total distance and the current point we are
        # processing, this could be any point, we can use 0.
        res = current = 0
        # Store the points that we need to travel to yet.
        unvisited = set(range(1, len(points)))
        while unvisited:
            # Add to the heap the distance between the current point and
            # all remaining points, the heap now contains distances
            # between all the points we have visited and all the
            # points we have not visited.
            for dest in unvisited:
                heappush(
                    heap,
                    (
                        abs(points[current][0] - points[dest][0])
                        + abs(points[current][1] - points[dest][1]),
                        dest,
                    ),
                )
            # Pop distances to points that we have already visited, this
            # distances could have been added before the point was added
            # to the visited joint set.
            while heap[0][1] not in unvisited:
                heappop(heap)
            # The first edge to a non-visited point is the shortest path
            # between the visited set and a non-visited node.
            weight, current = heappop(heap)
            # Mark points[i] as visited.
            unvisited.discard(current)
            res += weight
        return res


def test():
    executors = [
        Kruskal,
        Prim,
    ]
    tests = [
        [[[0, 0]], 0],
        [[[3, 12], [-2, 5], [-4, 1]], 18],
        [[[2, -3], [-17, -8], [13, 8], [-17, -15]], 53],  # LC 6
        [[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minCostConnectPoints(t[0])
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
