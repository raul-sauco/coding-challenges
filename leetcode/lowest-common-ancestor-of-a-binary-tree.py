# 236. Lowest Common Ancestor of a Binary Tree
# 🟠 Medium
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#
# Tags: Tree - Depth-First Search - Binary Tree

import timeit

from data import TreeNode, deserializeStringArrayToBinaryTree, drawTree


# Explore the tree using DFS, for each branch, return the number of nodes found in that branch, then check the root.
# When we find 2 matches, p and q, return the root of the subtree we are currently exploring.
#
# Time complexity: O(n) - We may need to visit every node.
# Space complexity: O(n) - The recursive call stack grows linearly with the size of the tree.
#
# Runtime: 96 ms, faster than 66.38% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 26.3 MB, less than 30.85% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
class DFSMatchCount:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Define a recursive function that returns the number of p and q found in a subtree.
        def dfs(node: TreeNode) -> int:
            # Base case when dfs gets called with None as a parameter.
            if not node:
                return 0

            # Recursive call with check to see if we already have a result.
            # If we already found the LCA, return it up the call chain.
            left = dfs(node.left)
            if isinstance(left, TreeNode):
                return left
            right = dfs(node.right)
            if isinstance(right, TreeNode):
                return right

            # If the sum of the matches in each branch plus matching this node's value is 2, we have found the LCA.
            found = left + right + int(node.val in [p.val, q.val])
            if found == 2:
                return node
            return found

        return dfs(root)


# TODO add an iterative solution.


def test():
    root1 = deserializeStringArrayToBinaryTree("[3,5,1,6,2,0,8,null,null,7,4]")
    root2 = deserializeStringArrayToBinaryTree("[3,5,1,6,2,0,8,null,null,7,4]")
    root3 = deserializeStringArrayToBinaryTree("[1,2]")
    executors = [DFSMatchCount]
    tests = [
        [root1, root1.left, root1.right, root1],
        [root2, root2.left, root2.left.right.right, root2.left],
        [root3, root3, root3.left, root3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.lowestCommonAncestor(t[0], t[1], t[2])
                exp = t[3]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()

# drawTree(deserializeStringArrayToBinaryTree("[1,2]"))
