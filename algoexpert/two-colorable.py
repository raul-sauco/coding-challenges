# Two Colorable
# 🟠 Medium
#
# https://www.algoexpert.io/questions/two-colorable
#
# Tags: Matrix - Breadth-First Search - Array

import timeit
from collections import deque


# Use breadth-first search to travel through the graph, each level
# needs to be the opposite color of the previous one.
#
# Time complexity: O(n) - We will visit all nodes once.
# Space complexity: O(n) - The queue and sets will grow in size linearly
# with the size of the input.
class BFS:
    def twoColorable(self, edges):
        # Use BFS to visit all nodes in the graph starting at v 0.
        queue = deque([0])
        # Two sets of edges that we have seen already, red and blue.
        reds, blues = set(), set()
        # The color of this level.
        red = True
        while queue:
            # Switch colors.
            red = not red
            # Process an entire level at this color.
            for _ in range(len(queue)):
                current = queue.popleft()
                # The set of complementaries.
                comp = blues if red else reds
                # The set of this color's vertices.
                same_color = reds if red else blues
                # If this node has been seen assigned the complimentary
                # color.
                if current in comp:
                    return False
                if current not in same_color:
                    same_color.add(current)
                    for neighbor in edges[current]:
                        if neighbor == current:
                            return False
                        queue.append(neighbor)
        return True


# An improvement is to use an array to store nodes, this lets us store
# different values for nodes that we have not visited, and nodes of one
# or another color while saving the time to hash values.
#
# Time complexity: O(n) - We will visit all nodes once.
# Space complexity: O(n) - The stack and array will grow in size
# with the size of the input.
class UseArray:
    def twoColorable(self, edges):
        nodes = [None] * len(edges)
        nodes[0] = 0
        stack = [0]
        while stack:
            current = stack.pop()
            for neighbor in edges[current]:
                # If we have not visited this neighbor before, visit it.
                if nodes[neighbor] is None:
                    # This neighbor needs to the the opposite color
                    # than the current node.
                    nodes[neighbor] = not nodes[current]
                    # And we need to process this neighbor vertex.
                    stack.append(neighbor)
                elif nodes[neighbor] == nodes[current]:
                    # If the neighbor has the same color, we failed.
                    return False
        return True


def test():
    executors = [
        BFS,
        UseArray,
    ]
    tests = [
        [[[0]], False],
        [[[1], [0]], True],
        [[[1], [0, 2], [1]], True],
        [[[1, 2], [0, 2], [0, 1]], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.twoColorable(t[0])
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
