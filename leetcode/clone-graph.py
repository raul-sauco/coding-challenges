# 133. Clone Graph
# 🟠 Medium
#
# https://leetcode.com/problems/clone-graph/
#
# Tags: Hash Table - Depth-First Search - Breath-First Search - Graph

import timeit
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Use two loops, on the first one, use BFS to make copies of all nodes,
# on the second, use BFS again to add the correct adjacency list to the
# newly created nodes.
#
# Time complexity: O(n) - We iterate over all the nodes twice.
# Space complexity: O(n) - The dictionary and the seen set will grow to
# the size of the input, if we consider that the input is limited to
# 100 nodes max, then O(1)
#
# Runtime: 91 ms, faster than 5.40%
# Memory Usage: 14.4 MB, less than 77.29%
class TwoLoopsBFS:
    def cloneGraph(self, node: Node) -> Node:
        # Base case, if not node return None.
        if not node:
            return None
        # Use BFS to process the nodes and a hashmap to keep a pointer
        # to the new nodes.
        q = deque([node])
        d = {}
        # Process all nodes making copies of them.
        while q:
            current: Node = q.popleft()
            # If we haven't processed this node yet.
            if current.val not in d:
                # Make a copy and save it to the dictionary.
                copy = Node(current.val)
                d[copy.val] = copy
                # Enqueue the neighbors.
                q.extend(current.neighbors)
        # We have copies of all original nodes, link them back starting
        # by the original root.
        q = deque([node])
        seen = set()
        while q:
            current = q.popleft()
            # If we haven't processed this nodes' adjacency list yet.
            if current.val not in seen:
                # Mark the node processed.
                seen.add(current.val)
                # Get the node's copy.
                copy: Node = d[current.val]
                # Append the copies of the original neighbors.
                new_neighbors = []
                for n in current.neighbors:
                    # Append this neighbor to the queue.
                    q.append(n)
                    # Append its copy to the new node's neighbors.
                    new_neighbors.append(d[n.val])
                # Link the adjacency list to the node.
                copy.neighbors = new_neighbors
        # Return the new root.
        return d[node.val]


# Optimize the previous solution using only one loop. We append nodes
# that we have seen to an array and process their neighbors using the
# queue.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - The dictionary and the queue will grow with
# the size of the input, if we consider that they are limited to
# 100 values, then we can say that space is O(1).
#
# Runtime: 85 ms, faster than 8.98%
# Memory Usage: 14.4 MB, less than 26.32%
class OnePassBFS:
    def cloneGraph(self, node: Node) -> Node:
        # Base case, no root.
        if not node:
            return None
        # Use a dictionary to store clones.
        clones = {}
        clones[node.val] = Node(node.val, [])
        # Use a queue to process elements.
        q = deque([node])
        while q:
            current = q.popleft()
            copy: Node = clones[current.val]
            # Process this node's adjacency list
            for n in current.neighbors:
                # If we have not already processed this neighbor.
                if n.val not in clones:
                    clones[n.val] = Node(n.val, [])
                    q.append(n)
                # Append either the neighbor copy to this node's list.
                copy.neighbors.append(clones[n.val])
        # Return the clone of the input node.
        return clones[node.val]


# Optimize the previous solution avoiding having to hash the values
# using an array indexed by node values. We can do that because the
# node values are guaranteed to be <= 100.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - The array and the queue will grow with the
# size of the input, if we consider that they are limited to 100 values,
# then we can say that space is O(1).
#
# RRuntime: 45 ms, faster than 84.53%
# Memory Usage: 14.4 MB, less than 77.29%
class OnePassBFSList:
    def cloneGraph(self, node: Node) -> Node:
        # Base case, no root.
        if not node:
            return None
        # Node values are guaranteed to be <= 100, we can use an array
        # to store them, instead of a hashmap.
        clones = [None] * 101
        clones[node.val] = Node(node.val)
        # Use a queue to process elements.
        q = deque([node])
        while q:
            current = q.popleft()
            copy: Node = clones[current.val]
            # Process this node's adjacency list
            for n in current.neighbors:
                # If we have not already processed this neighbor.
                if not clones[n.val]:
                    clones[n.val] = Node(n.val, [])
                    q.append(n)
                # Append either the neighbor copy to this node's list.
                copy.neighbors.append(clones[n.val])
        # Return the clone of the input node.
        return clones[node.val]


def test():
    executors = [
        TwoLoopsBFS,
        OnePassBFS,
        OnePassBFSList,
    ]
    tests = []
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.cloneGraph(t[0])
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
