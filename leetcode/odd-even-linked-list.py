# 328. Odd Even Linked List
# 🟠 Medium
#
# https://leetcode.com/problems/odd-even-linked-list/
#
# Tags: Linked List

import timeit
from typing import Optional

from utils.linked_list import LinkedList
from utils.list_node import ListNode


# Maintain two heads, odd and even lists, and iterate over the original
# linked list alternatively linking elements to one, then the other list
# until we are out of either odd or even elements. Link the two lists
# and return them.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - We only keep pointers in memory.
#
# Runtime: 50 ms, faster than 85.69%
# Memory Usage: 16.6 MB, less than 78.70%
class TwoLists:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Do nothing for linked lists with O, 1 or 2 nodes.
        if not head:
            return head
        # Otherwise, use head as the head of the odd list and head.next
        # as the head of the even list.
        odd = head
        even_head = even = head.next
        # When even exists, the previous odd node also exists.
        while even and even.next:
            # Update the odd pointers.
            odd.next = even.next
            odd = odd.next
            # Update the even pointers.
            even.next = odd.next
            even = even.next
        # Link the even list at the end of the odd list.
        odd.next = even_head
        return head


def test():
    executors = [TwoLists]
    tests = [
        [[], []],
        [[3], [3]],
        [[2, 3], [2, 3]],
        [[1, 2, 3, 4], [1, 3, 2, 4]],
        [[1, 2, 3, 4, 5], [1, 3, 5, 2, 4]],
        [[1, 2, 3, 4, 5, 6], [1, 3, 5, 2, 4, 6]],
        [[2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                ll = LinkedList.fromList(t[0])
                result_head = sol.oddEvenList(ll.getHead())
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
