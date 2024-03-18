# 1171. Remove Zero Sum Consecutive Nodes from Linked List
# 🟠 Medium
#
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
#
# Tags: Hash Table - Linked List

import timeit
from typing import Optional

from data import ListNode, deserializeListToLinkedList, serializeLinkedList


# Use each element in the input list as the start of a loop where we
# check the current sum of elements, and remove any sub-lists that sum
# up to zero.
#
# Time complexity: O(n^2) - Nested loops that iterate over the entire
# input list.
# Space complexity: O(1) - We store three pointers.
#
# Runtime 67 ms Beats 20%
# Memory 16.7 MB Beats 84%
class Solution:
    def removeZeroSumSublistsNested(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        start = dummy
        # Try each node in the list as the start node.
        while start and start.next:
            total = 0
            cur = start
            while cur.next:
                cur = cur.next
                total += cur.val
                if total == 0:
                    start.next = cur.next
                    total = 0
            start = start.next
        return dummy.next


# Use a hashmap of prefix sums, loop twice, on the first loop compute
# the prefix sums, on the second, remove any sums for which a further
# point on the list had the same prefix sum.
#
# Time complexity: O(n) - We iterate twice over the input list.
# Space complexity: O(n) - The hashmap will have one entry for each
# unique prefix sum, it could grow to n entries.
#
# Runtime 39 ms Beats 80%
# Memory 16.84 MB Beats 43%
class Solution:
    def removeZeroSumSublists(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        current_sum, node, sums = 0, dummy, {}
        while node:
            current_sum += node.val
            sums[current_sum] = node
            node = node.next
        node, current_sum = dummy, 0
        while node:
            current_sum += node.val
            # Unlink any section that sums to zero linking to the last
            # node with the same prefix sum, it could be the current node.
            node.next = sums[current_sum].next
            node = node.next
        return dummy.next


def test():
    executors = [Solution]
    tests = [
        [[1, 2, -3, 3, 1], [3, 1]],
        [[1, 2, 3, -3, 4], [1, 2, 4]],
        [[1, 2, 3, -3, -2], [1]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.removeZeroSumSublists(
                    deserializeListToLinkedList(t[0])
                )
                result = serializeLinkedList(result)
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
