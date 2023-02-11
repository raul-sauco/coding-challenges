# 1129. Shortest Path with Alternating Colors
# 🟠 Medium
#
# https://leetcode.com/problems/shortest-path-with-alternating-colors/
#
# Tags: Breadth-First Search - Graph

import timeit
from collections import deque
from typing import List


# Do two BFS traverses, both starting at 0, one using the red edge, one
# using the blue edge. This lets us use a stack and levels to perform
# the BFS.
#
# Time complexity: O(n) - We may visit each node once.
# Space complexity: O(n) - There are several structures of size n.
#
# Runtime 82 ms Beats 93.26%
# Memory 14.1 MB Beats 97.21%
class TwoPasses:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        # Create two adjacency lists, one for blue one for red.
        adj_b, adj_r = [[] for _ in range(n)], [[] for _ in range(n)]
        for a, b in redEdges:
            adj_r[a].append(b)
        for a, b in blueEdges:
            adj_b[a].append(b)
        # A function that performs BFS a level at a time taking into
        # account the color of the last edges that were traveled.
        def bfs(node: int, last_was_red: bool) -> List[int]:
            # Initialize the result, at the beginning we can only reach 0.
            res = [float("inf")] * n
            res[node] = 0
            # We need to check if we have arrived using the current
            # edge's color to this node already.
            visited_from_red, visited_from_blue = [False] * n, [False] * n
            visited_from_red[node] = True
            visited_from_blue[node] = True
            # The number of steps taken.
            steps = 0
            # Use a stack, equivalent to a queue for BFS if we do it one
            # level at a time.
            level = [node]
            while level:
                steps += 1
                next_level = []
                # Process the entire level.
                for _ in range(len(level)):
                    current = level.pop()
                    # Switch the edge color.
                    adj = adj_b if last_was_red else adj_r
                    visited = (
                        visited_from_blue if last_was_red else visited_from_red
                    )
                    for nei in adj[current]:
                        # If this is the shortest path to this neighbor.
                        if not visited[nei]:
                            visited[nei] = True
                            res[nei] = min(steps, res[nei])
                            next_level.append(nei)
                # Update the stacks.
                level = next_level
                last_was_red = not last_was_red
            return res

        red_dist, blue_dist = bfs(0, True), bfs(0, False)
        res = [min(red_dist[i], blue_dist[i]) for i in range(n)]
        return [val if val != float("inf") else -1 for val in res]


# Use a double ended queue and keep the information about the level and
# the last edge color used to arrive at the node in the queue elements
# themselves, this simplifies the algorithm.
#
# Time complexity: O(n) - We may visit each node once.
# Space complexity: O(n) - There are several structures of size n.
#
# Runtime 87 ms Beats 81.52%
# Memory 14.1 MB Beats 73.17%
class SinglePass:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        # Create two adjacency lists, one for blue one for red.
        adj = [[] for _ in range(n)], [[] for _ in range(n)]
        for a, b in redEdges:
            adj[0][a].append(b)
        for a, b in blueEdges:
            adj[1][a].append(b)
        res = [-1] * n
        res[0] = 0
        visited = [[True, True]] + [[False, False] for _ in range(n - 1)]
        # A queue of tuples, each tuple is (node, dist, color). Where
        # colors are red => 0, blue => 1.
        q = deque([(0, 0, 0), (0, 0, 1)])
        while q:
            node, dist, col = q.popleft()
            # We want to travel edges of the alternate color c
            alt = int(not col)
            for nei in adj[alt][node]:
                # If we have not visited this node using this color edge
                # before.
                if not visited[nei][alt]:
                    visited[nei][alt] = True
                    steps = dist + 1
                    if res[nei] == -1:
                        res[nei] = steps
                    q.append((nei, steps, alt))
        return res


def test():
    executors = [
        TwoPasses,
        SinglePass,
    ]
    tests = [
        [3, [[0, 1]], [[2, 1]], [0, 1, -1]],
        [3, [[0, 1], [1, 2]], [], [0, 1, -1]],
        [
            5,
            [[0, 1], [1, 2], [2, 3], [3, 4]],
            [[1, 2], [2, 3], [3, 1]],
            [0, 1, 2, 3, 7],
        ],
        [
            7,
            [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],
            [[0, 3], [0, 6], [1, 4], [6, 2]],
            [0, 1, -1, 1, 2, 3, 1],
        ],
        [
            6,
            [
                [1, 5],
                [2, 2],
                [5, 5],
                [3, 0],
                [4, 5],
                [2, 4],
                [4, 1],
                [1, 0],
                [1, 2],
                [5, 2],
                [2, 3],
                [0, 1],
            ],
            [[4, 4], [2, 5], [1, 1], [5, 4], [3, 3]],
            [0, 1, 3, -1, 4, 3],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.shortestAlternatingPaths(t[0], t[1], t[2])
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
