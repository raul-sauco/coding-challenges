# https://leetcode.com/problems/subtree-of-another-tree/

# Tags: Tree - Depth-First Search - String Matching - Binary Tree - Hash Function

import timeit
from functools import lru_cache
from typing import Optional

from data import TreeNode, deserializeStringArrayToBinaryTree


# We need to find if any node in the main tree has the same value as sub-root and, if found, the values of
# its children are exactly the same, and in the same order, as the ones in the main tree.
#
# Time complexity: O(n*m) - we may have to visit each node of the main tree
# Space complexity: O(n*m) - we may have as many calls in the stack as nodes in the bigger tree
#
# Runtime: 113 ms, faster than 95.07% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 15.2 MB, less than 12.87% of Python3 online submissions for Subtree of Another Tree.
class RecursiveDFS:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If one of the nodes is null, make sure the other is null as well
        if not p or not q:
            return not p and not q
        # The node values should be the same and the subtrees on each branch should be the same
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def containsSubTree(root: Optional[TreeNode]) -> bool:
            # If one of the nodes is null, make sure the other is null as well
            if not root or not subRoot:
                return not root and not subRoot
            if self.isSameTree(root, subRoot):
                return True
            return containsSubTree(root.left) or containsSubTree(root.right)

        return containsSubTree(root)


# In the leetcode discuss section, someone uses the Merkle hash to compare nodes of the tree,
# https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)
# they suggest that this results in a time complexity of O(m+n), better than the recursive O(m*n), but I think that
# is a mistake and this results in exploring all nodes of the root tree on each iteration.
# This could be improved storing the Merkle hashes for each node in a memo object.
# https://en.wikipedia.org/wiki/Merkle_tree
#
# Runtime: 185 ms, faster than 50.57% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 17.1 MB, less than 5.15% of Python3 online submissions for Subtree of Another Tree.
class MerkleHash:
    def isSubtree(self, root, subRoot):
        from hashlib import sha256

        def hash_(x: str):
            S = sha256()
            S.update(x.encode("utf-8"))
            return S.hexdigest()

        def merkle(node):
            if not node:
                return "#"
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_(m_left + str(node.val) + m_right)
            return node.merkle

        merkle(root)
        merkle(subRoot)

        def dfs(node):
            if not node:
                return False
            return node.merkle == subRoot.merkle or dfs(node.left) or dfs(node.right)

        return dfs(root)


def test():
    p1 = deserializeStringArrayToBinaryTree("[3,4,5,1,2]")
    q1 = deserializeStringArrayToBinaryTree("[4,1,2]")
    p2 = deserializeStringArrayToBinaryTree("[3,4,5,1,2,null,null,null,null,0]")
    q2 = deserializeStringArrayToBinaryTree("[4,1,2]")
    executors = [RecursiveDFS, MerkleHash]
    tests = [
        [p1, q1, True],
        [p2, q2, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1e4"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.isSubtree(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
