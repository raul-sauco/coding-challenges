# 25. Reverse Nodes in k-Group
# 🔴 Hard
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/
#
# Tags: Linked List - Recursion

import timeit
from typing import Optional, Tuple

from utils.linked_list import LinkedList
from utils.list_node import ListNode


# Iterate over the input list nodes in groups of size k, for each group
# we iterate twice, first to check if we have enough nodes to form a
# section of size k and, at the same time, to get a pointer to the first
# node after the next section of size k. We keep a pointer to the node
# right before the section that we are reversing and the one right after
# that section, then we use an auxiliary function to reverse the section
# and return its head and tail, we link the previous node with the head
# of the reversed section and the tail of the reversed section with the
# first node after it.
#
# Time complexity: O(n) - We visit each node twice.
# Space complexity: O(1) - We use constant memory.
#
# Runtime: 93 ms, faster than 63.67%
# Memory Usage: 15.2 MB, less than 85.27%
class Solution:
    # Given the head of a linked list, reverse and return a tuple
    # containing the new head and the tail.
    def reverseList(
        self, head: Optional[ListNode]
    ) -> Optional[Tuple[ListNode]]:
        if not head:
            return None
        current, next = head, head.next
        while next:
            # Get a reference to the current node to point its next to
            # later, then shift current and next pointers forward.
            prev, current, next = current, next, next.next
            # Reverse the pointer from current.
            current.next = prev
        head.next = None
        # Return the head and tail of the reversed list.
        return (current, head)

    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        # Base cases.
        if not head or k == 1:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next:
            # Do we have enough nodes to reverse a section?
            node, count, next_section_head = prev.next, k - 1, ListNode()
            while node.next and k:
                node = node.next
                count -= 1
                # Get a pointer to the node after this section and slice
                # the section.
                if not count:
                    next_section_head = node.next
                    node.next = None
            # If there are not enough nodes to make a full k section.
            if count:
                break
            # Append the reversed section to the tail of the previous
            # section.
            section_head, section_tail = self.reverseList(prev.next)
            # Make current point to the head of the reversed section.
            prev.next = section_head
            # Use the section tail as the new current and give it the
            # next node as its next.
            prev = section_tail
            prev.next = next_section_head
        return dummy.next


def test():
    executors = [Solution]
    tests = [
        [[], 4, []],
        [[1, 2, 3], 4, [1, 2, 3]],
        [[1, 2, 3, 4], 4, [4, 3, 2, 1]],
        [[1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]],
        [[1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result = sol.reverseKGroup(head, t[1])
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
