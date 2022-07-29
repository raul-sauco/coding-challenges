# 148. Sort List
# 🟠 Medium
#
# https://leetcode.com/problems/sort-list/
#
# Tags: Linked List - Two Pointers - Divide and Conquer - Sorting
# - Merge Sort

import timeit
from typing import Optional, Tuple

from data import LinkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Use merge sort. Very similar to implementing merge-sort in a list but
# we need to manually take care of the pointers.
#
# Time complexity: O(n*log(n)) - Merge sort complexity.
# Space complexity: O(n) - For the call stack.
#
# Runtime: 716 ms, faster than 71.06% of Python3 online submissions for
# Sort List.
# Memory Usage: 36.5 MB, less than 54.39% of Python3 online submissions
# for Sort List.
class MergeSort:
    # Define a function that takes the head of a linked list and returns
    # the head of two linked lists each containing half, or the closest
    # possible, the nodes of the original list.
    #
    # [-1, 5, 3, 4, 0] => ([-1, 5, 3], [4, 0])
    def split(self, head: ListNode) -> Tuple[ListNode, ListNode]:
        # Use the slow/fast pointer method to split the lists.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Use the first element after the mid as the head of the right
        # half. Set the pointer of mid to none to mark it as the end of
        # the first half.
        right_head = slow.next
        slow.next = None
        return (head, right_head)

    # Define a function that takes the heads of two sorted lists and
    # returns the head of the sorted list resulting from merging them
    # into one.
    #
    # [-1, 3, 5], [4, 0] => [-1, 0, 3, 4, 5]
    def mergeLists(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        # Use a discardable ListNode to build the merged list.
        temp = ListNode(0)
        # Get a pointer to the last element of the merged list.
        current = temp

        # Check which head has a higher value while both are not null
        # append it to the merged list and move the pointer.
        while head_a and head_b:
            if head_a.val < head_b.val:
                current.next = head_a
                head_a = head_a.next
            else:
                current.next = head_b
                head_b = head_b.next
            current = current.next

        # Check that we completely consume list_a
        if head_a:
            current.next = head_a

        # Check that we completely consume list_b
        if head_b:
            current.next = head_b

        # Return the head of the merged list.
        return temp.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case, if there are 0 or 1 nodes, do nothing, covers the
        # case where the input is null and the base case of the merge
        # sort where we consider the single element list sorted.
        if not head or not head.next:
            return head

        # Split the input linked list into two.
        a, b = self.split(head)
        a = self.sortList(a)
        b = self.sortList(b)

        # Merge the lists.
        return self.mergeLists(a, b)


def test():
    executors = [MergeSort]
    tests = [
        [[], []],
        [[4, 2, 1, 3], [1, 2, 3, 4]],
        [[-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]],
        [
            [2, 300, -1, 70],
            [-1, 2, 70, 300],
        ],
        [
            [2, 300, -1, 0, 70],
            [-1, 0, 2, 70, 300],
        ],
        [
            [2, 300, -1, 0, 70, 3, 50, 4, -10],
            [-10, -1, 0, 2, 3, 4, 50, 70, 300],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                ll = LinkedList.fromList(t[0])
                result_head = sol.sortList(ll.getHead())
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

# Auxiliary function to debug split function.
def testSplit():
    executors = [MergeSort]
    tests = [
        [[2, 300, -1, 0, 70], [2, 300, -1], [0, 70]],
        [[2, 300, -1], [2, 300], [-1]],
        [[0, 70], [0], [70]],
        [[4, 1, 3], [4, 1], [3]],
        [[4, 2, 1, 3], [4, 2], [1, 3]],
        [[-1, 5, 3, 4, 0], [-1, 5, 3], [4, 0]],
    ]
    for executor in executors:
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                ll = LinkedList.fromList(t[0])
                a, b = sol.split(ll.getHead())
                a = LinkedList(a).toList()
                b = LinkedList(b).toList()
                exp1 = t[1]
                assert a == exp1, (
                    f"\033[93m» {a} <> {exp1}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
                exp2 = t[2]
                assert b == exp2, (
                    f"\033[93m» {b} <> {exp2}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )


testSplit()

# Auxiliary function to debug merge function.
def testMerge():
    executors = [MergeSort]
    tests = [
        [[2, 300], [-1], [-1, 2, 300]],
        [[70], [0], [0, 70]],
        [[2], [1], [1, 2]],
        [[-2], [1], [-2, 1]],
        [[1, 4], [3], [1, 3, 4]],
        [
            [-1, 0, 2, 3, 4, 70],
            [-10, 50, 300],
            [-10, -1, 0, 2, 3, 4, 50, 70, 300],
        ],
    ]
    for executor in executors:
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                la = LinkedList.fromList(t[0])
                lb = LinkedList.fromList(t[1])
                merged = sol.mergeLists(la.getHead(), lb.getHead())
                result = LinkedList(merged).toList()
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )


testMerge()
