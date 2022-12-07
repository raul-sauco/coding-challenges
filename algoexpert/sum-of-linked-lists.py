# Sum Of Linked Lists
# 🟠 Medium
#
# https://www.algoexpert.io/questions/sum-of-linked-lists
#
# Tags: Linked List

import timeit

from utils.linked_list import LinkedList
from utils.list_node import ListNode


# In this problem the lists represent and integer with the higher digits
# coming later in the list, we can add the nodes as we encounter them
# and use one variable to store the carry, when we run out of nodes and
# the carry is 0, we have completed the addition.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(1) - Not counting inputs and output, we only use
# constant memory.
class Solution:
    def sumOfLinkedLists(self, linkedListOne, linkedListTwo):
        # Get two pointers to the current nodes that we are visiting in
        # each list. Use an extra dummy node to append result nodes to.
        node1, node2, dummy = linkedListOne, linkedListTwo, ListNode(0)
        # The carry between positions and a pointer to the previous
        # node on the sum list that we will build to append new nodes.
        carry, prev = 0, dummy
        # Iterate while there is anything to add.
        while node1 or node2 or carry:
            val = 0
            if node1:
                val += node1.value
                node1 = node1.next
            if node2:
                val += node2.value
                node2 = node2.next
            if carry:
                val += carry
            carry, val = divmod(val, 10)
            # Create a new node with the digit at this position.
            prev.next = ListNode(val)
            # Slide the sum pointer forward.
            prev = prev.next
        return dummy.next


def test():
    executors = [Solution]
    tests = [
        [[2, 4, 7, 1], [9, 4, 5], [1, 9, 2, 2]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head1 = LinkedList.fromList(t[0]).getHead()
                head2 = LinkedList.fromList(t[1]).getHead()
                sum_head = sol.sumOfLinkedLists(head1, head2)
                result = LinkedList(sum_head).toList()
                exp = t[2]
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
