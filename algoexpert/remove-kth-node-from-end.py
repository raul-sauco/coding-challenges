# Remove Kth Node From End
# 🟠 Medium
#
# https://www.algoexpert.io/questions/remove-kth-node-from-end
#
# Tags: Linked List

import timeit

from utils.linked_list import LinkedList, ListNode


# Use a fast pointer that we advance k positions, then start advancing
# a slow pointer at the same time until the fast pointer is placed at
# the last node in the list, at that moment the slow pointer is placed
# right before the node that we need to remove, if the node is the head
# handle it according to the problem prompt, otherwise remove it from
# the list.
#
# Time complexity: O(n) - We iterate over n nodes.
# Space complexity: O(1) - Constant extra memory used.
class Solution:
    def removeKthNodeFromEnd(self, head, k):
        # Create a dummy in case we need to slice the head.
        dummy = ListNode(-1)
        dummy.next = head
        fast = slow = dummy
        # The list is guaranteed to have k nodes, advance the fast
        # pointer k positions.
        while fast.next:
            fast = fast.next
            if k > 0:
                k -= 1
            else:
                slow = slow.next
        if slow is dummy:
            remove = head.next
            head.val = head.next.val
            head.next = head.next.next
        else:
            remove = slow.next
            slow.next = slow.next.next
        del remove
        return head


def test():
    executors = [Solution]
    tests = [
        [[1, 2], 2, [2]],
        [[1, 2, 3, 4, 5, 6, 7, 8], 3, [1, 2, 3, 4, 5, 7, 8]],
        [[1, 2, 3, 4, 5, 6, 7, 8], 7, [1, 3, 4, 5, 6, 7, 8]],
        [[1, 2, 3, 4, 5, 6, 7, 8], 8, [2, 3, 4, 5, 6, 7, 8]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result = sol.removeKthNodeFromEnd(head, t[1])
                result = LinkedList(result).toList()
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
