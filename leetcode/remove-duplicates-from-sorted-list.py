# 83. Remove Duplicates from Sorted List
# 🟢 Easy
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#
# Tags: Linked List

import timeit
from typing import Optional

from data import LinkedList, ListNode


# Iterate over the list checking if the next node has the same value
# as the current one, if it does, remove it from the list.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(1) - Only the input and output use variable memory.
#
# Runtime: 89 ms, faster than 26.93%
# Memory Usage: 14 MB, less than 29.62%
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # The algorithm takes care of null head and null head.next cases.
        current = head
        while current and current.next:
            if current.val == current.next.val:
                # Slice the next node from the list.
                current.next = current.next.next
            else:
                current = current.next
        return head


def test():
    executors = [Solution]
    tests = [
        [[], []],
        [[4], [4]],
        [[1, 1, 2], [1, 2]],
        [[1, 1, 1, 1, 1], [1]],
        [[1, 1, 2, 3, 3], [1, 2, 3]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result = sol.deleteDuplicates(head)
                result = LinkedList(result).toList()
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
