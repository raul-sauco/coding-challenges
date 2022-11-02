# 113. Path Sum II
# 🟠 Medium
#
# https://leetcode.com/problems/path-sum-ii/
#
# Tags: Backtracking - Tree - Depth-First Search - Binary Tree

import timeit
from collections import deque
from typing import List, Optional

from data import TreeNode, deserializeStringArrayToBinaryTree

# 1e4 calls
# » RecursiveDFS        0.10539   seconds
# » BacktrackDFS        0.10922   seconds
# » IterativeDFS        0.09478   seconds
# » IterativeBFS        0.09348   seconds

# Travel down the tree adding the value of the nodes to a list of "seen"
# node values and, at the same time, subtracting the value from the
# target sum. When we get to a leaf, if its value matches the target sum
# add the path we traveled to get there to the solution list.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - For the call stack.
#
# Runtime: 103 ms, faster than 7.32%
# Memory Usage: 19.4 MB, less than 10.56%
class RecursiveDFS:
    def pathSum(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        # Store all the possible paths.
        paths = []

        def dfs(
            node: Optional[TreeNode], targetSum: int, path: List[int]
        ) -> None:
            # Base case.
            if not node:
                return
            # Mark the current node as visited along this path.
            path.append(node.val)
            # If we are in a leaf and the value matches the current
            # target sum, we have a path that matches, add it to the
            # solution set.
            if not node.left and not node.right:
                if node.val == targetSum:
                    paths.append(path)
            else:
                # We are not at a leaf.
                dfs(node.left, targetSum - node.val, [*path])
                dfs(node.right, targetSum - node.val, [*path])

        # Initial call.
        dfs(root, targetSum, [])
        return paths


# Similar to the previous depth first search solution but optimizing
# time and memory usage by not copying the path list at every call of
# the dfs function, instead using backtracking to add the current value
# for the children to access and remove it once the children have been
# processed and control returns to the parent. This way, the only time
# we copy the paths, on O(n) over the number of nodes in the path
# operation, is when we add them to the result set.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - For the call stack.
#
# Runtime: 86 ms, faster than 32.64%
# Memory Usage: 15.5 MB, less than 72.84%
class BacktrackDFS:
    def pathSum(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        # Base case, no root.
        if not root:
            return []
        # Save the paths found
        paths = []
        # Define the dfs function.
        def dfs(node: TreeNode, path: List[int], current_sum: int):
            # Add this node's value to the current sum and the path.
            current_sum += node.val
            path.append(node.val)
            # If this is a leaf.
            if not node.left and not node.right:
                # The sum matches.
                if current_sum == targetSum:
                    paths.append(path.copy())
            else:
                # Else, there is, at least, one child.
                if node.left:
                    dfs(node.left, path, current_sum)
                if node.right:
                    dfs(node.right, path, current_sum)
            # Backtrack
            path.pop()
            current_sum -= node.val

        # Initial call
        dfs(root, [], 0)
        return paths


# We can explore the tree inorder adding to the stack the current target
# sum, the remaining of the previous target sum after having visited
# this node, and a list of the node values that we have traveled to get
# here.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - For the call stack.
#
# Runtime: 67 ms, faster than 57.43%
# Memory Usage: 15.2 MB, less than 93.22%
class IterativeDFS:
    def pathSum(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        # Edge case.
        if not root:
            return []
        # Store all possible results.
        result = []
        # Instead of only pushing nodes to the stack, push a tuple with
        # the node, the current target sum, and the path traveled.
        stack = [(root, targetSum - root.val, [root.val])]
        # Inorder traversal of the tree.
        while stack:
            # Pop the current node.
            current, target, path = stack.pop()
            # If this node is a leaf, check whether this path had the
            # target sum.
            if not current.left and not current.right and target == 0:
                result.append(path)
            # If the node is not a leaf.
            if current.left:
                stack.append(
                    (
                        current.left,
                        target - current.left.val,
                        path + [current.left.val],
                    )
                )
            if current.right:
                stack.append(
                    (
                        current.right,
                        target - current.right.val,
                        path + [current.right.val],
                    )
                )

        # Return the results, it could be empty.
        return result


# We can modify slightly the previous solution to explore the tree using
# Breadth-First Search instead of DFS. Since we are keeping all the
# information we need inside the nodes that we are visiting, the
# solution is pretty much the same, only the order in which we visit
# the nodes changes.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - For the call stack.
#
# Runtime: 76 ms, faster than 40.97%
# Memory Usage: 15.2 MB, less than 93.22%
class IterativeBFS:
    def pathSum(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        # Edge case.
        if not root:
            return []
        # Store all possible results.
        result = []
        # Instead of only pushing nodes to the stack, push a tuple with
        # the node, the current target sum, and the path traveled.
        queue = deque()
        queue.append((root, targetSum - root.val, [root.val]))
        # Inorder traversal of the tree.
        while queue:
            # Pop the current node.
            current, target, path = queue.popleft()
            # If this node is a leaf, check whether this path had the
            # target sum.
            if not current.left and not current.right and target == 0:
                result.append(path)
            # If the node is not a leaf.
            if current.left:
                queue.append(
                    (
                        current.left,
                        target - current.left.val,
                        path + [current.left.val],
                    )
                )
            if current.right:
                queue.append(
                    (
                        current.right,
                        target - current.right.val,
                        path + [current.right.val],
                    )
                )

        # Return the results, it could be empty.
        return result


def test():
    executors = [
        RecursiveDFS,
        BacktrackDFS,
        IterativeDFS,
        IterativeBFS,
    ]
    tests = [
        [
            "[5,4,8,11,null,13,4,7,2,null,null,5,1]",
            22,
            [[5, 4, 11, 2], [5, 8, 4, 5]],
        ],
        ["[1,2,3]", 5, []],
        ["[1,2]", 0, []],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for i, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.pathSum(root, t[1])
                # Need to sort to make the order not matter.
                result.sort()
                exp = sorted(t[2])
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {i} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
