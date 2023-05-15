# 1721. Swapping Nodes in a Linked List
# 🟠 Medium
#
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
#
# Tags: Linked List - Two Pointers

import timeit
from typing import Optional

from utils.linked_list import LinkedList, ListNode


# Use a counter, first travel k nodes and get a pointer to that node,
# then use a fast and slow pointer, traveling at the same speed, to
# travel to the end of the linked list, when the fast pointer reaches
# the end of the list, the slow pointer will be at our second target
# node, swap these values and return the head.
#
# Time complexity: O(n) - We visit each node of the linked list and do
# O(1) work for each.
# Space complexity: O(1) - We only store four pointers in memory.
#
# Runtime 947 ms Beats 92.19%
# Memory 50.7 MB Beats 22.68%
class Solution:
    def swapNodes(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        idx = 1
        fast = slow = head
        while idx < k:
            fast = fast.next
            idx += 1
        # We traveled k nodes, get a pointer to the first node we need
        # to exchange.
        first = fast
        while fast.next:
            slow, fast = slow.next, fast.next
        first.val, slow.val = slow.val, first.val
        return head


def test():
    executors = [Solution]
    tests = [
        [[1, 2, 3, 4, 5], 2, [1, 4, 3, 2, 5]],
        [[7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5, [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result = sol.swapNodes(head, t[1])
                result = LinkedList(result).toList()
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
