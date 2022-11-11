# 24. Swap Nodes in Pairs
# 🟠 Medium
#
# https://leetcode.com/problems/swap-nodes-in-pairs/
#
# Tags: Linked List - Two Pointers

import timeit
from typing import Optional

from data import LinkedList, ListNode


# Keep a pointer to the node right before the current group, then swap
# the pointers from the front node to the back node, and make the front
# node point to the next node after the back one.
#
# Time complexity: O(n) - We iterate over the entire list one time.
# Space complexity: O(1) - We only store pointers in memory.
#
# Runtime: 35 ms, faster than 89.78%
# Memory Usage: 13.8 MB, less than 65.67%
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        # Use four pointers.
        dummy = ListNode(0, head)
        prev, one, two, next = dummy, head, head.next, None
        while one and two:
            # Update next and prev pointers.
            next, prev.next, prev = two.next, two, one
            # Update internal group pointers.
            one.next, two.next = two.next, one
            # Shuffle working node pointers.
            one = next
            if one:
                two = one.next
        return dummy.next


def test():
    executors = [Solution]
    tests = [
        [[], []],
        [[1], [1]],
        [[1, 2], [2, 1]],
        [[1, 2, 3], [2, 1, 3]],
        [[1, 2, 3, 4], [2, 1, 4, 3]],
        [[1, 2, 3, 4, 5], [2, 1, 4, 3, 5]],
        [[1, 2, 3, 4, 5, 8], [2, 1, 4, 3, 8, 5]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result = LinkedList(sol.swapPairs(head)).toList()
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
