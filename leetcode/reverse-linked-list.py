# 206. Reverse Linked List
# 🟢 Easy
#
# https://leetcode.com/problems/reverse-linked-list/
#
# Tags: Linked List - Recursion


import timeit
from typing import Optional

from utils.linked_list import LinkedList
from utils.list_node import ListNode


# Iterate over all the list nodes, for each, create a temporary pointer
# to it, then make the right node point to the left one and the left to
# the next one.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(1) - We use constant memory.
#
# Runtime: 39 ms, faster than 92.11%
# Memory Usage: 15.4 MB, less than 55.68%
class Iterative:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current, next = head, head.next
        while next:
            # Get a reference to the current node to point its next to
            # later, then shift current and next pointers forward.
            prev, current, next = current, next, next.next
            # Reverse the pointer from current.
            current.next = prev
        head.next = None
        # Return the head of the reversed list.
        return current


# Recursively call the function with each node and its previous one.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - The call stack will have one call for each
# node in the input list.
#
# Runtime: 96 ms, faster than 5.40%
# Memory Usage: 20.5 MB, less than 8.12%
class Recursive:
    def reverseList(
        self, head: Optional[ListNode], prev: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        if not head:
            return prev
        curr, head.next = head.next, prev
        return self.reverseList(curr, head)


def test():
    executors = [
        Iterative,
        Recursive,
    ]
    tests = [
        [[], []],
        [[1, 2], [2, 1]],
        [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result = sol.reverseList(head)
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
