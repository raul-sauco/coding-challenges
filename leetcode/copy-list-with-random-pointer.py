# 138. Copy List with Random Pointer
# 🟠 Medium
#
# https://leetcode.com/problems/copy-list-with-random-pointer/
#
# Tags: Hash Table - Linked List

import timeit
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = x
        self.next = next
        self.random = random

    def __repr__(self):
        return f"Node({self.val})"


# Iterate once over the list copying all the nodes in order and
# inserting each node's copy right after the original. Then iterate
# again over the list visiting simultaneously the original and copy
# nodes, assign the copy's random pointer to original.random.next.
#
# Time complexity; O(n) - We visit each node twice.
# Space complexity: O(1) - No extra memory used.
#
# Runtime: 72 ms, faster than 26.81%
# Memory Usage: 14.9 MB, less than 82.88%
class Interweaving:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        # Iterate over the list making copies of all nodes.
        current = head
        while current:
            # Make a copy of current.
            copy = Node(current.val)
            # Interweave it between current and next.
            copy.next = current.next
            current.next = copy
            # Move to the next original node.
            current = copy.next
        # Iterate the new list visiting originals and copies simultaneously.
        original, copy = head, head.next
        while original:
            # Update the random pointer.
            copy.random = original.random.next if original.random else None
            # Slide the pointer to the original node forwards two positions.
            original = copy.next
            # If we are not at the end of the list yet.
            if original:
                # Remove the original node from the list.
                copy.next = copy.next.next
                copy = original.next
        # Return the new list.
        return head.next


# TODO check the method that uses the random pointer to interweave.


def test():
    executors = [Interweaving]
    tests = []
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.copyRandomList(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        # stop = timeit.default_timer()
        # used = str(round(stop - start, 5))
        # cols = "{0:20}{1:10}{2:10}"
        # res = cols.format(executor.__name__, used, "seconds")
        # print(f"\033[92m» {res}\033[0m")
        print(f"\033[91m» No local tests for this file!!\033[0m")


test()
