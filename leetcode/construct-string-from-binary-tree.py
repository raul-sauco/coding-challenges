# 606. Construct String from Binary Tree
# 🟢 Easy
#
# https://leetcode.com/problems/construct-string-from-binary-tree/
#
# Tags: String - Tree - Depth-First Search - Binary Tree

import timeit
from typing import Optional

from data import TreeNode, deserializeStringArrayToBinaryTree


# Preorder DFS over the tree, each subtree gets wrapped recursively in
# parentheses, when a node only has a right child, we add an empty
# parentheses before it.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - The call stack will grow to the height of the
# tree, which can grow to size n, for example a tree where each node
# only has one children.
#
# Runtime: 59 ms, faster than 86.02%
# Memory Usage: 16.6 MB, less than 5.63%
class HelperFn:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # Define a recursive function that explores the tree using
        # preorder DFS.
        def dfs(node: TreeNode) -> str:
            # If we are at a leaf, return only its value.
            if not node.left and not node.right:
                return str(node.val)
            # Node cannot be null. Create a list that starts with node.
            s = [str(node.val)]
            # We have a left child, process it.
            if node.left:
                s.append("(" + dfs(node.left) + ")")
            # We don't have a left child, only a right one. Append an
            # empty parentheses to disambiguate the right child.
            else:
                s.append("()")
            # We have a right child, process it.
            if node.right:
                s.append("(" + dfs(node.right) + ")")
            # Return this subtree values.
            return "".join(s)

        return dfs(root)


# Once we make the observation that the problem can be solved using
# recursive DFS, like in the previous solution, we can improve the code
# removing the unnecessary helper function if we call recursively the
# main tree2str function adding a null check that returns an empty
# string when root is null.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - The call stack will grow to the height of the
# tree, which can grow to size n, for example a tree where each node
# only has one children.
#
# Runtime: 66 ms, faster than 75.52%
# Memory Usage: 16.6 MB, less than 5.63%
class RecursiveDFS:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # We may call tree2str with a null root. Return an empty string.
        if not root:
            return ""
        # Format the left child string, we want to also check if there
        # is a right child, if there is no left child but there is a
        # right one, we want to add an empty parentheses to
        # disambiguate the serialization.
        left = (
            "({})".format(self.tree2str(root.left))
            if (root.left or root.right)
            else ""
        )
        # Process the right child. We want an empty string if it is null.
        right = "({})".format(self.tree2str(root.right)) if root.right else ""
        # Return the string that represents this subtree.
        return "{}{}{}".format(root.val, left, right)


def test():
    executors = [
        HelperFn,
        RecursiveDFS,
    ]
    tests = [
        ["[1]", "1"],
        ["[1,null, 6]", "1()(6)"],
        ["[1,2,3,4]", "1(2(4))(3)"],
        ["[1,2,3,null,4]", "1(2()(4))(3)"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.tree2str(root)
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
