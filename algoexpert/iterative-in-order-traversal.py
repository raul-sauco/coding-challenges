# Iterative In Order Traversal
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/iterative-in-order-traversal
#
# Tags: Tree - Binary Tree

import timeit


# If we can use extra space, we can use a stack to store nodes that we
# travel through but don't have to process yet.
#
# Time complexity: O(n) - We will visit each node at most twice.
# Space complexity: O(n) - The stack could grow to the size of the tree.
class UseStack:
    def iterativeInOrderTraversal(self, tree, callback):
        stack, current = [], tree
        while current or stack:
            # We have a current node.
            if current:
                if current.left:
                    stack.append(current)
                    current = current.left
                else:
                    callback(current)
                    current = current.right
            else:
                # Pop a node from the stack and process it.
                node = stack.pop()
                callback(node)
                current = node.right


# In this problem the nodes have an extra pointer to the parent, using
# that pointer and an extra pointer to the node we just processed, we
# can improve the space complexity of the other solutions. If we are at
# the root of the tree of we came down from the parent, try to go left
# if we came from the left node, try to go right, if we came from the
# right, go back up to the parent.
#
# Time complexity: O(n) - We will visit each node at most twice.
# Space complexity: O(1) - We only use three pointers of extra memory.
class UsePointers:
    def iterativeInOrderTraversal(self, tree, callback):
        prev, current = None, tree
        while current:
            # We come from the parent.
            if not prev or prev == current.parent:
                if current.left:
                    nxt = current.left
                else:
                    callback(current)
                    nxt = current.right if current.right else current.parent
            elif prev is current.left:
                callback(current)
                nxt = current.right if current.right else current.parent
            else:
                nxt = current.parent
            prev = current
            current = nxt


def test():
    executors = [UseStack]
    tests = []
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.iterativeInOrderTraversal(t[0], t[1])
                exp = t[2]
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
