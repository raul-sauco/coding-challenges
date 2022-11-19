# Node Swap
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/node-swap
#
# Tags: Linked Lists

import timeit

from utils.linked_list import LinkedList
from utils.list_node import ListNode


# Reverse each pair of nodes, ignore the final node if it does not form
# a pair.
#
# Time complexity: O(n) - We iterate over the list once.
# Space complexity: O(1) - We use constant space.
class Solution:
    def nodeSwap(self, head: ListNode):
        dummy = ListNode(0, head)
        prev, current, next = dummy, head, head.next
        while current and next:
            current.next = next.next
            next.next = current
            prev.next = next
            prev = current
            current = current.next
            next = current.next if current else None
        return dummy.next


def test():
    executors = [Solution]
    tests = [
        [[1], [1]],
        [[1, 2], [2, 1]],
        [[1, 2, 3], [2, 1, 3]],
        [[1, 2, 3, 4, 5], [2, 1, 4, 3, 5]],
        [[1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result_head = sol.nodeSwap(head)
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
