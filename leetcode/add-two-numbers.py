# 2. Add Two Numbers
# 🟠 Medium
#
# https://leetcode.com/problems/add-two-numbers/
#
# Tags: Linked List - Math - Recursion

import timeit
from typing import Optional

from data import LinkedList, ListNode

# Iterate over both lists nodes adding their values and keeping the
# carry value in memory for the next iteration. Use the sum of
# the carry and both current node values to set the value of the
# new node in the result list and compute the carry.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity; O(1) - No extra memory.
#
# Runtime: 152 ms, faster than 18.37%
# Memory Usage: 13.9 MB, less than 43.17%
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Create a new dummy head
        dummy = ListNode(-1)
        curr = dummy
        # Initialize the carry of the previous sum as 0
        carry = 0
        # Iterate over the values in both lists simultaneously until we
        # run out of both of them.
        a, b = l1, l2
        while a or b:
            if a:
                carry += a.val
                a = a.next
            if b:
                carry += b.val
                b = b.next
            # Calculate the new node value and carry
            carry, remainder = divmod(carry, 10)
            next = ListNode(remainder)
            curr.next = next
            curr = curr.next
        # Edge case, the last two nodes had a carry.
        if carry:
            curr.next = ListNode(carry)
        return dummy.next


def test():
    executors = [Solution]
    tests = [
        [[2, 4, 3], [5, 6, 4], [7, 0, 8]],
        [[0], [0], [0]],
        [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result: LinkedList = sol.addTwoNumbers(
                    LinkedList.fromList(t[0]).getHead(),
                    LinkedList.fromList(t[1]).getHead(),
                )
                exp = t[2]
                # The result is a ListNode, create a linked list and
                # serialize it to list.
                serialized_result = LinkedList(result).toList()
                assert serialized_result == exp, (
                    f"\033[93m» {serialized_result} <> {exp}\033[91m "
                    + f"for test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
