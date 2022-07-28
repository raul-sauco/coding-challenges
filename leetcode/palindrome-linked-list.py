# 234. Palindrome Linked List
# 🟢 Easy
#
# https://leetcode.com/problems/palindrome-linked-list/
#
# Tags: Linked List - Two Pointers - Stack - Recursion

import timeit
from typing import Optional

from data import LinkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# The most obvious solution is to convert to array, then check if the
# array is a palindrome.
#
# Time complexity: O(n) - We visit each node up to 3 times.
# Space complexity: O(n) - We create an array of size n.
#
# Runtime: 761 ms, faster than 97.01% of Python3 online submissions for
# Palindrome Linked List.
# Memory Usage: 46.9 MB, less than 29.08% of Python3 online submissions
# for Palindrome Linked List.
class ToArray:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # The code takes care of the base case when head is None.
        current = head
        values = []
        while current:
            values.append(current.val)
            current = current.next

        # The empty linked list is a palindrome.
        for i in range(len(values)):
            if values[i] != values[-i - 1]:
                return False

        # If the characters match, it is a palindrome.
        return True


# Follow-up question where they ask to do it on O(n) time and O(1)
# space.
# Idea:
#
# - Travel through the linked list once to get its length.
# - Travel again through the list, from the head, reversing the links
# - until we are at the middle node or between the two central nodes.
# - Check the value of each node on the tail against the value of its
# - symmetrical node on the middle half, now traveling in reverse.
#
# Time complexity: O(n) - We travel all nodes 3 times in a palindromic
# list.
# Space complexity: O(1) - We only store the number of nodes and a few
# references to nodes, independently of the input size.
#
# Runtime: 1559 ms, faster than 12.91% of Python3 online submissions for
# Palindrome Linked List.
# Memory Usage: 31.1 MB, less than 98.46% of Python3 online submissions
# for Palindrome Linked List.
class ReverseFirstHalf:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Take care of the empty head and single node cases.
        if not head or not head.next:
            return True

        # Get the node count on O(n)
        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        # Travel to the middle node reversing the list.
        # Subtracting 1 from count to find the middle is equivalent to
        # middle = (count // 2) if count % 2 == 1 else (count // 2 )- 1
        idx_middle, idx = (count - 1) // 2, 0

        # Some edge cases:
        # middle [0] == 0
        # middle [1, 2] == 0
        # middle [1, 2, 3] == 1
        # middle [1, 2, 3, 4] == 1
        # middle [1, 2, 3, 4, 5] == 2
        # middle [1, 2, 3, 4, 5, 6] == 2

        # Our objective is to have a pointer to traverse the first half
        # of the linked list backwards at the symmetrical node of the
        # one we are traveling forward.

        current = head
        next = current.next
        head.next = None
        while next and idx < idx_middle:
            prev = current
            current = next
            next = current.next
            current.next = prev
            idx += 1

        # For linked lists with an even number of nodes, current now
        # holds the first node of the head, next holds the last node,
        # now the head, of the first half. We can start comparing them.
        if count % 2 == 0:
            # For linked lists with even amount of nodes. Rename the
            # pointers to make it easier to read te code.
            prev = current

        # Now prev is the head of the reversed first half. Next is the
        # head of the second half. Both are pointing to the
        # correct node in their section of the linked list.
        # On lists with an uneven number of nodes, the middle node gets
        # ignored and we start checking on the node before and after it.
        while prev and next:
            # Check the values of the current symmetrical nodes.
            if prev.val != next.val:
                return False
            # Move one node away from the middle
            prev = prev.next
            next = next.next

        return True


def test():
    executors = [
        ToArray,
        ReverseFirstHalf,
    ]
    tests = [
        # [[], True],
        [[13], True],
        [[1, 2], False],
        [[1, 2, 1], True],
        [[1, 2, 2, 1], True],
        [[1, 2, 3, 4, 5, 5, 4, 3, 2, 2], False],
        [[1, 2, 3, 4, 5, 4, 3, 2, 2], False],
        [[1, 2, 3, 4, 5, 4, 3, 2, 1], True],
        [[1, 2, 3, 4, 5, 5, 4, 3, 2, 1], True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isPalindrome(LinkedList.fromList(t[0]).getHead())
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
