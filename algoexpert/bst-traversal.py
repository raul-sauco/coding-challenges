# BST Traversal
# 🟠 Medium
#
# https://www.algoexpert.io/questions/bst-traversal
#
# Tags: Binary Tree - Binary Search Tree

import timeit

from utils.binary_tree import BinaryTree


# Use the definition of the tree traversals to recursively call the
# functions and append values to the input array in the correct order.
#
# Time complexity: O(n) - On each of the traversals we will visit each
# node once.
# Space complexity: O(h) - On each of the traversals, the call stack
# will grow to the height of the tree, this would be log(n) on the best
# case, a perfectly balanced tree, to O(n) in the worst case, a totally
# skewed tree.
class Recursive:
    def inOrderTraverse(self, tree, array):
        if tree:
            # Explore left subtree, then the root, then right subtree.
            self.inOrderTraverse(tree.left, array)
            array.append(tree.value)
            self.inOrderTraverse(tree.right, array)
        return array

    def preOrderTraverse(self, tree, array):
        if tree:
            # Explore the root, the left subtree, then right subtree.
            array.append(tree.value)
            self.preOrderTraverse(tree.left, array)
            self.preOrderTraverse(tree.right, array)
        return array

    def postOrderTraverse(self, tree, array):
        if tree:
            # Explore the left subtree, the right subtree, then the root.
            self.postOrderTraverse(tree.left, array)
            self.postOrderTraverse(tree.right, array)
            array.append(tree.value)
        return array


class UseBinaryTreeFn:
    def inOrderTraverse(self, tree, array):
        return BinaryTree(tree).inOrderTraverse()

    def preOrderTraverse(self, tree, array):
        return BinaryTree(tree).preOrderTraverse()

    def postOrderTraverse(self, tree, array):
        return BinaryTree(tree).postOrderTraverse()


def test():
    executors = [
        Recursive,
        UseBinaryTreeFn,
    ]
    tests = [
        ["[]", [], [], []],
        ["[1]", [1], [1], [1]],
        ["[1,null,4]", [1, 4], [1, 4], [4, 1]],
        [
            "[10,5,15,2,5,13,22,1,null,null,null,null,14]",
            [1, 2, 5, 5, 10, 13, 14, 15, 22],
            [10, 5, 2, 1, 5, 15, 13, 14, 22],
            [1, 2, 5, 5, 14, 13, 22, 15, 10],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromStringArray(t[0]).getRoot()
                inorder = sol.inOrderTraverse(root, [])
                preorder = sol.preOrderTraverse(root, [])
                postorder = sol.postOrderTraverse(root, [])
                assert inorder == t[1], (
                    f"\033[93m» {inorder} <> {t[1]}\033[91m for"
                    + f" test {col} inorder using \033[1m{executor.__name__}"
                )
                assert preorder == t[2], (
                    f"\033[93m» {preorder} <> {t[2]}\033[91m for"
                    + f" test {col} preorder using \033[1m{executor.__name__}"
                )
                assert postorder == t[3], (
                    f"\033[93m» {postorder} <> {t[3]}\033[91m for"
                    + f" test {col} postorder using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
