# 2130. Maximum Twin Sum of a Linked List
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
#
# Tags: Linked List - Two Pointers - Stack

import timeit
from typing import Optional

from utils.linked_list import LinkedList
from utils.list_node import ListNode


# Find the middle of the list and reverse the second half, then visit
# simultaneously nodes on the first and reversed second half computing
# their sums, return the highest one.
#
# Time complexity: O(n) - We visit each node 2 or 3 times.
# Space complexity: O(1) - Constant space.
#
# Runtime: 905 ms, faster than 97.14%
# Memory Usage: 45 MB, less than 84.97%
class UsePointers:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find the middle node.
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        # Reverse the second half.
        current, prev = middle, None
        while current:
            current.next, prev, current = prev, current, current.next
        # Iterate over both halves.
        res = 0
        node1, node2 = head, prev
        # Use the reversed list to determine when we are out of nodes
        # the last node of the first half still points to the second
        # list's previous head, now its last node.
        while node2:
            res = max(res, node1.val + node2.val)
            node1, node2 = node1.next, node2.next
        return res


# Use extra memory to store all the list's values in an array and then
# compute the sum of twins.
#
# Time complexity: O(n) - We visit the list nodes once and the array
# elements once.
# Space complexity: O(n) - The extra array has the same number of
# elements as the original list.
#
# Runtime: 1434 ms, faster than 69.9%
# Memory Usage: 54.7 MB, less than 23.61%
class UseArray:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums, current = [], head
        while current:
            nums.append(current.val)
            current = current.next
        l, r, res = 0, len(nums) - 1, 0
        while l < r:
            res = max(res, nums[l] + nums[r])
            l += 1
            r -= 1
        return res


# A combination of the two previous solutions where we only push half
# of the list into a stack and pop elements to access them.
#
# Time complexity: O(n) - We visit the list nodes once and the array
# elements once.
# Space complexity: O(n) - The extra array has the same number of
# elements as the original list.
#
# Runtime: 2583 ms, faster than 16.92%
# Memory Usage: 55.2 MB, less than 15.20%
class UseStack:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find the middle node.
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        current, stack = slow, []
        while current:
            stack.append(current.val)
            current = current.next
        res, current = 0, head
        while stack:
            res = max(res, stack.pop() + current.val)
            current = current.next
        return res


def test():
    executors = [
        UsePointers,
        UseArray,
        UseStack,
    ]
    tests = [
        [[5, 4, 2, 1], 6],
        [[4, 2, 2, 3], 7],
        [[1, 100000], 100001],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result = sol.pairSum(head)
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
