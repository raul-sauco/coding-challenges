# 112. Path Sum
# 🟢 Easy
#
# https://leetcode.com/problems/path-sum/
#
# Tags: Tree - Depth-First Search - Breath-First-Search - Binary Tree

import timeit
from typing import Optional

from data import TreeNode, deserializeStringArrayToBinaryTree


# We can use inorder traversal to visit each subtree and add the value
# of the current root, if at some leaf we have the target sum, return
# True, otherwise return False when we run out of options. We can use
# the same hasPathSum, if either the left or right tree have the target
# sum of target-root.val, we can return True, otherwise False.
#
# Time complexity: O(n) - We visit every node once.
# Space complexity: O(n) - The call stack will grow in size
# proportionally to the size of the input.
#
# Runtime: 82 ms, faster than 21.61% of Python3 online submissions for
# Path Sum.
# Memory Usage: 15 MB, less than 57.89% of Python3 online submissions
# for Path Sum.
class RecursiveDFS:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case, empty tree, no paths. Having this base case
        # simplifies the code because we can make recursive calls
        # without checking if the children are None.
        if not root:
            return False
        # Base case, we are in a leaf, return whether the leaf value is
        # equal to targetSum
        if not root.left and not root.right:
            return root.val == targetSum
        # Explore the sub-trees, if any of them has a targetSum that is
        # equal to the current targetSum - the value of this node, then
        # this tree has a path that adds up to the target sum.
        return self.hasPathSum(
            root.left, targetSum - root.val
        ) or self.hasPathSum(root.right, targetSum - root.val)


# Travel down the tree using inorder traversal. Add the current root
# value to each of its children's value. When we get to a leaf, check if
# the leaf's value, representing the sum of values of that path, matches
# the target sum. If no path matches the target sum, return false.
#
# Time complexity: O(n) - We visit each node.
# Space complexity: O(n) - For the stack.
#
# Runtime: 47 ms, faster than 89.31% of Python3 online submissions for
# Path Sum.
# Memory Usage: 15 MB, less than 57.89% of Python3 online submissions
# for Path Sum.
class IterativeDFS:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Edge case.
        if not root:
            return False
        stack = [root]
        # Inorder traversal of the tree.
        while stack:
            # Pop the current node.
            current = stack.pop()
            # If this node is a leaf, check whether this path had the
            # target sum.
            if not current.left and not current.right:
                if current.val == targetSum:
                    return True
            # Add its value to the children's value.
            if current.left:
                current.left.val += current.val
                stack.append(current.left)
            if current.right:
                current.right.val += current.val
                stack.append(current.right)

        # If we couldn't find any matches, return False.
        return False


def test():
    executors = [RecursiveDFS, IterativeDFS]
    tests = [
        ["[5,4,8,11,null,13,4,7,2,null,null,null,1]", 22, True],
        ["[1,2,3]", 5, False],
        ["[]", 0, False],  # Empty tree has no paths.
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.hasPathSum(
                    deserializeStringArrayToBinaryTree(t[0]), t[1]
                )
                exp = t[2]
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
# drawTree(deserializeStringArrayToBinaryTree("[6,2,8,0,4,7,9,null,null,3,5]"))
