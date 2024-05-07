# 2816. Double a Number Represented as a Linked List
# 🟠 Medium
#
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
#
# Tags: Linked List - Math - Stack

import timeit
from typing import Optional

from utils.linked_list import LinkedList
from utils.list_node import ListNode


# Reverse the list, then reverse it back again, the second time, double
# the value of the current node and check the value of the next node
# when the value is more than 10, mod it by 10 and add the multiples of
# ten to the current node, same as if we were manually doing an addition.
#
# Time complexity: O(n) - We iterate over the nodes twice, once to
# reverse the list and a second time to reverse and double the values
# at the same time.
# Space complexity: O(1) - Constant extra memory used.
#
# Runtime 262 ms Beats 44%
# Memory 19.46 MB Beats 54%
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, prev = head, None
        while current:
            current.next, current, prev = prev, current.next, current
        # Reverse while doubling node values, check if next.val > 10.
        current, prev = prev, None
        while current:
            current.val *= 2
            current.next, current, prev = prev, current.next, current
            if prev and prev.next and prev.next.val >= 10:
                prev.val += prev.next.val // 10
                prev.next.val %= 10
        if prev.val >= 10:
            prev = ListNode(prev.val // 10, prev)
            prev.next.val %= 10
        return prev


# A much nicer solution, iterate over the nodes doubling them and discarding
# anything but the unit digit, then check if the next node's value is greater
# than 4 and will produce a carry when doubled, if so, add one to the current
# node's value. Do the same for the head before iterating over the list.
#
# Time complexity: O(n) - We iterate over the nodes once and do constant time
# work for each node.
# Space complexity: O(1) - Constant extra memory used.
#
# Runtime 219 ms Beats 85%
# Memory 19.42 MB Beats 54%
class Solution2:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head.val > 4:
            head = ListNode(0, head)
        cur = head
        while cur:
            cur.val = (cur.val * 2) % 10
            if cur.next and cur.next.val > 4:
                cur.val += 1
            cur = cur.next
        return head


def test():
    executors = [
        Solution,
        Solution2,
    ]
    tests = [
        [[5], [1, 0]],
        [[1, 5], [3, 0]],
        [[1, 8, 9], [3, 7, 8]],
        [[9, 9, 9], [1, 9, 9, 8]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result = LinkedList(sol.doubleIt(head)).toList()
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
