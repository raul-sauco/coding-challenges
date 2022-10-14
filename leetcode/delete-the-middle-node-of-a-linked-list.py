# 2095. Delete the Middle Node of a Linked List
# 🟠 Medium
#
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
#
# Tags: Linked List - Two Pointers

import timeit
from typing import Optional

from data import LinkedList, ListNode


# Use the fast&slow pointers technique to find the middle node, since we
# are interested in deleting it, we initialize the slow pointer to one
# position before the head, that way, when fast finds the end of the
# list, we can delete the node right after slow. To make the code easier
# to read, we can call the slow pointer "pre".
#
# Time complexity: O(n) - We visit each node at most once.
# Space complexity: O(1) - We only keep two extra pointers in memory.
#
# Runtime: 1883 ms, faster than 92.20%
# Memory Usage: 60 MB, less than 94.23%
class TwoPointers:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case, only one node.
        if not head.next:
            return None
        # Use a previous pointer to make deleting the middle node
        # easier, another option would be to first find the middle node,
        # then iterate over the list to delete it.
        pre = ListNode(next=head)
        # Use a fast and slow pointer technique to find the node right
        # before the middle one.
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            pre = pre.next
        # Not necessary, but we can explicitly delete the node.
        target = pre.next
        # Slice the middle node from the list, it could result on
        # pre.next being null.
        pre.next = pre.next.next
        # Remove the node from memory.
        del target
        return head


def test():
    executors = [TwoPointers]
    tests = [
        [[1], []],
        [[1, 2], [1]],
        [[1, 2, 3], [1, 3]],
        [[1, 2, 3, 4], [1, 2, 4]],
        [[1, 2, 3, 4, 5], [1, 2, 4, 5]],
        [[1, 2, 3, 4, 5, 6], [1, 2, 3, 5, 6]],
        [[1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result_head = sol.deleteMiddle(head)
                result = LinkedList(result_head).toList()
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
