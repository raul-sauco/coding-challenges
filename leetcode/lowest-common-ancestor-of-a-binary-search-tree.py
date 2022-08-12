# 235. Lowest Common Ancestor of a Binary Search Tree
# 🟠 Medium
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#
# Tags: Tree - Depth-First Search - Binary Search Tree - Binary Tree

import timeit

from data import TreeNode, deserializeStringArrayToBinaryTree


# We can determine where the values we are seeking will be from the
# value of any node that is the root of the tree we are currently
# inspecting:
#
# - If both values are greater than the value of the current node,
#   both values will be located in the right subtree.
# - If both values are smaller than the value of the current node, both
#   values will be located in the left subtree.
# - If the current root's value is equal to one of the values we are
#   looking for, the other one will be a child and we have found the LCA.
# - If the current root's value is between the values of the nodes we
#   are searching, one is on the left subtree, and one is on the right
#   subtree, the current root is also the LCA.
#
# Time complexity: O(log(n)) - in each iteration, we either find the
# result or discard half of the remaining nodes.
# Space complexity: O(1) - We only need to keep a pointer to the node we
# are currently visiting.
#
# Runtime: 84 ms, faster than 91.10%
# Memory Usage: 18.7 MB, less than 97.27%
class BinarySearch:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        lowest, highest = (p, q) if p.val < q.val else (q, p)
        current = root
        while True:
            # If the current node's value is greater than the highest
            # value we are seeking both p and q will be in the left
            # subtree.
            if highest.val < current.val:
                current = current.left
            # If the current's node value is less than the lowest value
            # we are seeking, both p, q will be in the right subtree.
            elif current.val < lowest.val:
                current = current.right
            # Otherwise lowest.val <= current.val <= highest.val,
            # therefore current is the LCA.
            else:
                return current


# Similar idea to the above but shorter code. The longer version is more
# readable and, in my opinion, should be preferred, but this one
# displays a couple of nice tricks, using the multiplication to compare
# three values a < b < c, and using a > comparison to decide which
# branch to discard, and which one to visit, depending on the relation
# between the current root and the values searched.
#
# Time complexity: O(log(n)) - in each iteration, we either find the
# result or discard half of the remaining nodes.
# Space complexity: O(1) - We only need to keep a pointer to the node we
# are currently visiting.
#
# Runtime: 114 ms, faster than 57.41%
# Memory Usage: 18.9 MB, less than 22.80%
class Shorter:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root


def test():
    root1 = deserializeStringArrayToBinaryTree("[6,2,8,0,4,7,9,null,null,3,5]")
    root2 = deserializeStringArrayToBinaryTree("[6,2,8,0,4,7,9,null,null,3,5]")
    root3 = deserializeStringArrayToBinaryTree("[2,1]")
    root4 = deserializeStringArrayToBinaryTree("[6,2,8,0,4,7,9,null,null,3,5]")
    executors = [BinarySearch, Shorter]
    tests = [
        [root1, root1.left, root1.right, root1],
        [root2, root2.left, root2.left.right, root2.left],
        [root3, root3, root3.left, root3],
        [
            root4,
            root4.left.right.left,
            root4.left.right.right,
            root4.left.right,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.lowestCommonAncestor(t[0], t[1], t[2])
                exp = t[3]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
