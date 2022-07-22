# https://leetcode.com/problems/partition-list/

# Tags: Linked List - Two Pointers

import timeit
from typing import Optional

from data import LinkedList, ListNode


# Create two new, empty, lists, left and right. Iterate over the elements of the original list placing elements < x
# into the left list, and elements >= x into the right list. When we run out of elements we check if the left list
# has any elements, if it does, we return left + right, otherwise we return the right head, this takes case of the
# edge case where both lists are empty.
#
# Time complexity: O(n) - we visit each element once.
# Space complexity: O(1) - we use 6 variables, not dependent on the input size.
#
# Runtime: 64 ms, faster than 27.39% of Python3 online submissions for Partition List.
# Memory Usage: 14 MB, less than 31.57% of Python3 online submissions for Partition List.
class TwoLists:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Keep track of two lists, left side with values < x and right side with values >= x
        left_head, left_current, right_head, right_current = None, None, None, None
        prev, current = head, head.next

        # Add the head to the head of its list
        head.next = None
        if prev.val < x:
            left_head = prev
            left_current = left_head
        else:
            right_head = prev
            right_current = right_head

        while current:
            # Store the next linked node and remove the reference
            next = current.next
            current.next = None
            if current.val < x:
                # Add to left list
                if left_current:
                    left_current.next = current
                    left_current = current
                else:
                    left_head, left_current = current, current
            else:
                # Add to right list
                if right_current:
                    right_current.next = current
                    right_current = current
                else:
                    right_head, right_current = current, current

            # Walk forward one position
            current = next

        # Merge the lists if the left list has any values
        if left_current:
            left_current.next = right_head
            return left_head

        # If the left list is empty, return the right list
        return right_head


# Similar solution to above, but we can avoid the conditional checks inside the while loop using two dummy nodes as
# the heads of left and right.
#
# Time complexity: O(n) - we visit each element once.
# Space complexity: O(1) - we use 6 variables, not dependent on the input size.
#
# Runtime: 43 ms, faster than 77.34% of Python3 online submissions for Partition List.
# Memory Usage: 14 MB, less than 31.57% of Python3 online submissions for Partition List.
#
# Based on the LeetCode official solution: https://leetcode.com/problems/partition-list/solution/
class DummyNodes:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Use dummy nodes to make some conditional checks unnecessary.
        left_current = left_head = ListNode(0)
        right_current = right_head = ListNode(0)

        # Use head directly, instead of current.
        while head:
            # Insert left
            if head.val < x:
                left_current.next = head
                left_current = left_current.next
            # Insert right
            else:
                right_current.next = head
                right_current = right_current.next

            # Walk forward one position
            head = head.next

        # Remove the link from the last node of right, not doing this could lead to cyclic loops besides giving
        # the wrong result.
        right_current.next = None

        # No need for the conditional, if left is empty, left_current is the dummy node, if right is empty, we are
        # assigning None to left_current.next which is the desired behavior.
        left_current.next = right_head.next

        # Return the left head, node after the left dummy head. It could be the right head if the left list was empty.
        return left_head.next


def test():
    executors = [TwoLists, DummyNodes]
    tests = [
        [[-30], 10, [-30]],  # One element only, to the left list
        [[30], 10, [30]],  # One element only, to the left list
        [[1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]],  # Normal case
        [[1, 4, 3, 2, 5, 2], -3, [1, 4, 3, 2, 5, 2]],  # All elements go to the right list
        [[1, 4, 3, 2, 5, 2], 30, [1, 4, 3, 2, 5, 2]],  # All elements go to the left list
        [[2, 1], 2, [1, 2]],  # Head goes to right, everything else to left
        [[2, 1], -1, [2, 1]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.partition(LinkedList.fromList(t[0]).getHead(), t[1])
                exp = t[2]
                serialized_result = LinkedList(result).toList()
                assert (
                    serialized_result == exp
                ), f"\033[93m» {serialized_result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
