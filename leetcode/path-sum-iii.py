# 437. Path Sum III
# 🟠 Medium
#
# https://leetcode.com/problems/path-sum-iii/
#
# Tags: Tree - Depth-First Search - Binary Tree

import timeit
from collections import defaultdict
from typing import Optional

from data import TreeNode, deserializeStringArrayToBinaryTree


# Travel through the tree using DFS, for each node that we visit, add
# its value to the current running sum and save it in a dictionary.
# We check if we can subtract any of the previous sums to the current
# sum to get the target sum. If we can, we add the number of times that
# we have seen that sum to the results, because the path between the
# current node and the nodes at which we had that sum will give the
# target sum.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - The call stack will grow proportionally to
# the size of the input.
#
# Runtime: 61 ms, faster than 88.31%
# Memory Usage: 15.3 MB, less than 55.74%
class DFS:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Edge case.
        if not root:
            return 0

        # Keep count of the number of results.
        self.res = 0

        # Define a function that takes a node, the current sum of the
        # branch up to its parent and a dictionary with sums that we
        # have seen along the current path, checks if we can get
        # the target sum using the value at this node, and recursively
        # calls the function for each of its children.
        def dfs(node: TreeNode, prev_sum: int, memo) -> None:
            # Compute the total sum from the root to this node along the
            # path traveled.
            current_sum = prev_sum + node.val
            # We are looking for entries in the dictionary that we could
            # subtract from the current_sum to equal target.
            #   current_sum - x = target
            # We can shift values to get the equivalent equation:
            #   x = current_sum - target
            match = current_sum - targetSum
            if match in memo:
                # Add the number of times we have seen the current_sum
                # complement to the results.
                self.res += memo[match]

            # Mark the current sum as seen, or seen one more time.
            memo[current_sum] += 1

            # Recursive call for each of the current node's children.
            if node.left:
                dfs(node.left, current_sum, memo)
            if node.right:
                dfs(node.right, current_sum, memo)

            # Remove the current sum from the memo as we are going up
            # the call stack.
            memo[current_sum] -= 1
            if memo[current_sum] == 0:
                del memo[current_sum]

        # Before we start, we have "seen" a total sum of 0.
        memo = defaultdict(int)
        memo[0] = 1
        # Initial call
        dfs(root, 0, memo)
        return self.res


def test():
    executors = [DFS]
    tests = [
        ["[10]", 10, 1],
        ["[10,null,-10]", 0, 1],
        ["[10,null,-10,10,10]", 0, 3],
        ["[10,5,-3,3,2,null,11,3,-2,null,1]", 8, 3],
        ["[10,null,-10,1,2,10,-1,null,null,-1]", 0, 4],
        ["[5,4,8,11,null,13,4,7,2,null,null,5,1]", 22, 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for i, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.pathSum(root, t[1])
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
