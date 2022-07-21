# https://leetcode.com/problems/reverse-linked-list-ii/

# Tags: Linked List


import timeit
from typing import Optional

from data import ListNode, deserializeListToLinkedList, serializeLinkedList


# Go through the nodes until we are at left, store left - 1 in a variable, go through left to right reversing the
# links, finish by linking left to right.
#
# Time complexity: O(n) - one pass over all list elements.
# Space complexity: O(1) - a fixed number of variables.
#
# Runtime: 55 ms, faster than 32.79% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 14 MB, less than 51.75% of Python3 online submissions for Reverse Linked List II.
class TwoLoops:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        current, prev = head, None

        # Navigate to the left node
        for _ in range(left - 1):
            prev, current = current, current.next

        # Keep a reference to the leftmost node of the reversed section and another to the first node of the
        # section that we are reversing
        last_before_reverse = prev
        first_reversed_node = current

        # Iterate over the nodes between left and right reversing the links
        for _ in range(left, right + 1):
            next = current.next
            current.next = prev
            prev, current = current, next

        # Finish by linking the last node before the reverse sequence with the first reversed node
        # and the last node of the reversed sequence with the next node
        if last_before_reverse:
            last_before_reverse.next = prev
        elif left == 1:
            # If we have reversed from the start of the linked list, head should point to the first reversed node
            head = prev
        # Point the last reversed node to the first node outside the reversed section, it can be null
        first_reversed_node.next = current

        return head


# Similar solution but using a while loop instead of two for loops.
#
# Time complexity: O(n) - one pass over all list elements.
# Space complexity: O(1) - a fixed number of variables.
#
# Runtime: 55 ms, faster than 32.79% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 14.1 MB, less than 51.75% of Python3 online submissions for Reverse Linked List II.
class While:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        i = 0
        current, prev, left_node, right_node, last_before_reverse = head, None, None, None, None
        while current:
            i += 1
            if i == left - 1:
                last_before_reverse = current
            if i == left:
                left_node = current
            if i == right:
                right_node = current
            if i == right + 1:
                left_node.next = current
            if left <= i <= right:
                next = current.next
                current.next = prev
                prev = current
                current = next
            else:
                prev = current
                current = current.next

        if last_before_reverse:
            last_before_reverse.next = right_node
        else:
            head = right_node

        if i == right:
            left_node.next = None

        return head


def test():
    executors = [TwoLoops, While]
    tests = [
        [[3, 5], 1, 2, [5, 3]],
        [[1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]],
        [[1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1]],
        [[1, 2, -35, 4, 5], 2, 5, [1, 5, 4, -35, 2]],
        [[5], 1, 1, [5]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.reverseBetween(deserializeListToLinkedList(t[0]), t[1], t[2])
                exp = t[3]
                serialized_result = serializeLinkedList(result)
                assert (
                    serialized_result == exp
                ), f"\033[93m» {serialized_result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
