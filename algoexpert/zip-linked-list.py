# Zip Linked List
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/zip-linked-list
#
# Tags: Linked Lists

import timeit

from utils.linked_list import LinkedList
from utils.list_node import ListNode


# Reverse the second half of the list, then iterate over the first half
# and the reversed second half at the same time interweaving nodes.
#
# Time complexity: O(n) - We visit each node a maximum of 3 times.
# Space complexity: O(1) - We use constant space.
class Solution:
    def zipLinkedList(self, linkedList: ListNode):
        # 1. Find the middle of the linked list.
        slow, fast = linkedList, linkedList
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Handle lists with less than 3 elements.
        if not slow.next:
            return linkedList
        # Slice the list halves.
        next_head = slow.next
        slow.next = None
        # 2. Reverse the second half of the list.
        current, next = next_head, next_head.next
        while next:
            # Get a reference to the current node to point its next to
            # later, then shift current and next pointers forward.
            prev, current, next = current, next, next.next
            # Reverse the pointer from current.
            current.next = prev
        next_head.next = None
        # The heads of the initial and reversed lists.
        front, tail = linkedList, current
        # 3. Interweave the lists.
        while front and tail:
            next_front, next_tail = front.next, tail.next
            front.next, tail.next = tail, next_front
            front, tail = next_front, next_tail
        return linkedList


def test():
    executors = [Solution]
    tests = [
        [[1], [1]],
        [[1, 2], [1, 2]],
        [[1, 2, 3], [1, 3, 2]],
        [[1, 2, 3, 4, 5], [1, 5, 2, 4, 3]],
        [[1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result_head = sol.zipLinkedList(head)
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
