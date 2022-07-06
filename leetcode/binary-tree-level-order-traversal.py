# https://leetcode.com/problems/binary-tree-level-order-traversal/


from collections import deque
import timeit
from typing import List, Optional
from data import TreeNode

# 1000 iterations:
#
# » FasterBFS           0.01962   seconds
# » QueueBFS            0.0274    seconds
# » HelperArray         0.02953   seconds


# A performance improvement is to detect null values early and not add them to the queue
# this saves later iterations over None values and if checks and improves performance
# even though the Time and space complexity both remain at O(n)
# Time complexity comes from visiting each node of the tree once
# Space complexity comes from the fact that the queue may grow to O(n/2) => O(n)
#
# Runtime: 47 ms, faster than 65.11% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.1 MB, less than 84.03 % of Python3 online submissions for Binary Tree Level Order Traversal.
class FasterBFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue, result = deque([root]), []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result


# Runtime: 80 ms, faster than 5.76% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 15 MB, less than 8.74 % of Python3 online submissions for Binary Tree Level Order Traversal.
class HelperArray:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def helper(node: TreeNode, level: int):
            while len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        if root:
            helper(root, 0)
        return result

# Intuitive BFS, we queue a value for each child of each node
# for None values, we don't do anything


class QueueBFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque([root])

        # BFS
        while q:
            # Store all the level's values in an array
            level = []
            # Right now the queue only has the current level's nodes
            for _ in range(len(q)):
                node: TreeNode = q.popleft()
                # We could have added None values to the queue
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # Level could be just None nodes
            if level:
                result.append(level)
        return result


def test():
    executors = [HelperArray, FasterBFS,  QueueBFS]
    node15 = TreeNode(val=15)
    node7 = TreeNode(val=7)
    node20 = TreeNode(val=20, left=node15, right=node7)
    node9 = TreeNode(val=9)
    node3 = TreeNode(val=3, left=node9, right=node20)
    node21 = TreeNode(val=1)
    tests = [
        [node3, [[3], [9, 20], [15, 7]]],
        [node21, [[1]]],
        [None, []],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = executor()
                result = sol.levelOrder(t[0])
                expected = t[1]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
