# 109. Convert Sorted List to Binary Search Tree
# 🟠 Medium
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
#
# Tags: Linked List - Divide and Conquer - Tree - Binary Search Tree - Binary Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree, TreeNode
from utils.linked_list import LinkedList, ListNode


# Use a divide and conquer approach, use two pointers to find the middle
# of the linked list, use the middle node as the root of the BST, then
# use two recursive calls with the unused left and right linked lists to
# generate the left and right subtrees.
#
# Time complexity: O(n) - Each node will be visited one, two or three
# times.
# Space complexity: O(log(n)) - The height of the call stack.
#
# Runtime 126 ms Beats 63.28%
# Memory 17.7 MB Beats 97.19%
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return
        # Use two pointers to find the middle of the list.
        slow, fast = ListNode(0, next=head), head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        middle = slow.next
        root = TreeNode(middle.val)
        if middle is not head:
            # Slice the list
            slow.next = None
            root.left = self.sortedListToBST(head)
        if middle.next:
            root.right = self.sortedListToBST(middle.next)
        return root


def test():
    executors = [Solution]
    tests = [
        [[], []],
        [[-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result = sol.sortedListToBST(head)
                result = BinaryTree(result).toList()
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
