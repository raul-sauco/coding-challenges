# 1669. Merge In Between Linked Lists
# 🟠 Medium
#
# https://leetcode.com/problems/merge-in-between-linked-lists/
#
# Tags: Linked List

import timeit

from utils.linked_list import LinkedList
from utils.list_node import ListNode


# Get pointers to the insertion points and splice list1 inserting list2 at the
# given nodes.
#
# Time complexity: O(m+n) - We fully traverse list2 and traverse b nodes on list1.
# Space complexity: O(1) - We only store pointers.
#
# Runtime 179 ms Beats 94%
# Memory 21.09 MB Beats 70%
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        nodea = list1
        for _ in range(a - 1):
            nodea = nodea.next
        nodeb = nodea
        for _ in range(b - a + 1):
            nodeb = nodeb.next
        nodea.next = list2
        tail2.next = nodeb.next
        return list1


def test():
    executors = [Solution]
    tests = [
        [
            [10, 1, 13, 6, 9, 5],
            3,
            4,
            [1000000, 1000001, 1000002],
            [10, 1, 13, 1000000, 1000001, 1000002, 5],
        ],
        [
            [0, 1, 2, 3, 4, 5, 6],
            2,
            5,
            [1000000, 1000001, 1000002, 1000003, 1000004],
            [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head1 = LinkedList.fromList(t[0]).getHead()
                head2 = LinkedList.fromList(t[3]).getHead()
                result_head = sol.mergeInBetween(head1, t[1], t[2], head2)
                result = LinkedList(result_head).toList()
                exp = t[4]
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
