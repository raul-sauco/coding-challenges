# Remove Duplicates From Linked List
# 🟢 Easy
#
# https://www.algoexpert.io/questions/remove-duplicates-from-linked-list
#
# Tags: Linked List

import timeit

from utils.linked_list import LinkedList
from utils.list_node import ListNode


# Iterate over the list nodes, at each node, check the following node's
# value, while the following node's value is the same, slice it off the
# list and delete the node.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(1) - We use constant memory.
class Solution:
    def removeDuplicatesFromLinkedList(self, linkedList: ListNode):
        # Iterate over the list checking the current and next node's
        # value.
        current = linkedList
        while current:
            while current.next and current.next.val == current.val:
                tmp = current.next
                current.next = current.next.next
                del tmp
            # Once we have removed all duplicates on this section,
            # move the current pointer to the next distinct node.
            current = current.next
        return linkedList


def test():
    executors = [Solution]
    tests = [
        [[], []],
        [[4], [4]],
        [[1, 1, 2], [1, 2]],
        [[1, 1, 1, 1, 1], [1]],
        [[1, 1, 2, 3, 3], [1, 2, 3]],
        [[1, 1, 3, 4, 4, 4, 5, 6, 6], [1, 3, 4, 5, 6]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result = sol.removeDuplicatesFromLinkedList(head)
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
