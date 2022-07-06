# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

import timeit
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Runtime: 85 ms, faster than 38.18% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16.3 MB, less than 48.82 % of Python3 online submissions for N-ary Tree Preorder Traversal.
class RecursiveDFS:
    def preorder(self, root: Node) -> List[int]:
        if not root:
            return []
        values = []

        def dfs(node: Node):
            values.append(node.val)
            if node.children:
                for child_node in node.children:
                    dfs(child_node)
        dfs(root)
        return values


# Runtime: 88 ms, faster than 33.42% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16 MB, less than 80.88 % of Python3 online submissions for N-ary Tree Preorder Traversal.
class IterativeDFS:
    def preorder(self, root: Node) -> List[int]:
        if not root:
            return []
        values = []
        stack = [root]
        while stack:
            node = stack.pop()
            # Visit the node we just popped
            values.append(node.val)
            # In python we need to check if the children [] is none before the for loop
            if node.children:
                # Reverse-push the children in the stack for pre-order
                for child_node in reversed(node.children):
                    stack.append(child_node)
        return values


class SelfRecursive:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = [root.val]
        for node in root.children:
            result.extend(self.preorder(node))
        return result


def test():
    executors = [RecursiveDFS, IterativeDFS, SelfRecursive]
    node6 = Node(val=6, children=[])
    node5 = Node(val=5, children=[])
    node4 = Node(val=4, children=[])
    node3 = Node(val=3, children=[node5, node6])
    node2 = Node(val=2, children=[])
    node1 = Node(val=1, children=[node3, node2, node4])
    tests = [
        [node1, [1, 3, 5, 6, 2, 4]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for t in tests:
                sol = executor()
                result = sol.preorder(t[0])
                expected = t[1]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
