# 297. Serialize and Deserialize Binary Tree
# 🔴 Hard
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
#
# Tags: String - Tree - Depth-First Search - Breadth-First Search -
# Design - Binary Tree

import timeit
from collections import deque
from typing import Optional

from data import deserializeStringArrayToBinaryTree, serializeTreeToList


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # Improve visualization in the debugger.
    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


# Create a serializer that uses the same format as LeetCode, that way
# it can be used in other binary tree problem's tests.
#
# Runtime: 120 ms, faster than 95.45%
# Memory Usage: 20 MB, less than 96.74%
class Codec:
    # Function to encode a tree, given its root, to a single string.
    # We can use BFS, for each node, we push two values to the queue,
    # the values can be null if one, or both, children, are missing.
    #
    # Time complexity: O(n) - We visit each node once.
    # Space complexity: O(n) - The queue can contain half the nodes in
    # the tree.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Base case.
        if not root:
            return "[]"
        res = []
        q = deque([root])
        # While there are elements and they are not all null.
        while q and any(q):
            current = q.popleft()
            if not current:
                res.append("null")
            else:
                res.append(str(current.val))
                # Enqueue two values, either children or None.
                q.append(current.left)
                q.append(current.right)
        # Convert the list to a string.
        res = "[" + ",".join(res) + "]"
        return res

    # Function to decode a string into a binary tree and return its root.
    #
    # Time complexity: O(n) - We visit each value of the input once.
    # Space complexity: O(n) - The value queue holds n-1 values, the
    # nodes queue will hold one full level at a time, it can grow to
    # O(n/2), both of these simplify to O(n).
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Base case, null root.
        if data == "[]":
            return None
        # Convert the input string to a deque of strings.
        vals = deque(data[1:-1].split(","))
        # Deserialize one level at a time.
        # We know that root is not null.
        root = TreeNode(int(vals.popleft()))
        q = deque([root])
        # Process values.
        while vals:
            # The next two values are children of the leftmost node.
            current = q.popleft()
            left_val = vals.popleft()
            if left_val != "null":
                current.left = TreeNode(int(left_val))
                q.append(current.left)
            # Left could be the last value in the queue.
            if vals:
                right_val = vals.popleft()
                if right_val != "null":
                    current.right = TreeNode(int(right_val))
                    q.append(current.right)
        return root


def test():
    executors = [Codec]
    tests = [
        ["[]", "[]"],
        ["[1,2,3]", "[1,2,3]"],
        ["[1,null,2,3]", "[1,null,2,3]"],
        ["[1,2,3,null,null,4,5]", "[1,2,3,null,null,4,5]"],
        ["[5,4,7,3,null,2,null,-1,null,9]", "[5,4,7,3,null,2,null,-1,null,9]"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                ser = executor()
                deser = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                serialized = ser.serialize(root)
                result = serializeTreeToList(deser.deserialize(serialized))
                exp = serializeTreeToList(
                    deserializeStringArrayToBinaryTree(t[1])
                )
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
