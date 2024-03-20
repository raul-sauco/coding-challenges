# 2807. Insert Greatest Common Divisors in Linked List
# 🟠 Medium
#
# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
#
# Tags: Linked List - Math - Number Theory

import timeit

from math import gcd
from typing import Optional
from utils.linked_list import LinkedList
from utils.list_node import ListNode


# Traverse the input list computing the gcd of each pair of nodes and
# inserting that as a new node between each pair.
#
# Time complexity: O(n) - We fully traverse the input list inserting nodes.
# Space complexity: O(1) - We only store pointers.
#
# Runtime 71 ms Beats 52%
# Memory 19.58 MB Beats 78%
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        node = head
        while node.next:
            gcd_node = ListNode(
                val=gcd(node.val, node.next.val), next=node.next
            )
            node.next = gcd_node
            node = gcd_node.next
            # It can also be written as:
            # node.next = ListNode(val=gcd(node.val, node.next.val), next=node.next)
            # node = node.next.next
        return head


def test():
    executors = [Solution]
    tests = [
        [[7], [7]],
        [[18, 6, 10, 3], [18, 6, 6, 2, 10, 1, 3]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head1 = LinkedList.fromList(t[0]).getHead()
                result_head = sol.insertGreatestCommonDivisors(head1)
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
