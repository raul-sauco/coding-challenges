# 237. Delete Node in a Linked List
# 🟠 Medium
#
# https://leetcode.com/problems/delete-node-in-a-linked-list/
#
# Tags: LinkedList

import timeit

from data import LinkedList, ListNode


# Shift all the values starting from the given node to the left by one,
# when we get to the end of the list, use a previous pointer to set the
# next reference of the one to last node to null.
#
# Time complexity: O(n) - We only visit nodes once from the given one
# to the end of the list.
# Space complexity: O(1) - We only keep pointers.
#
# Runtime: 66 ms, faster than 60.27%
# Memory Usage: 14.1 MB, less than 91.10%
class WithPrevPointer:
    def deleteNode(self, node: ListNode) -> None:
        prev = current = node
        while current.next:
            current.val = current.next.val
            prev = current
            current = current.next
        prev.next = None


# First update the value of the current pointer to that of the next
# node, then shift the current pointer forward, when we get to the end,
# set the next pointer of the current node to null.
#
# Time complexity: O(n) - We only visit nodes once from the given one
# to the end of the list.
# Space complexity: O(1) - We only keep pointers.
#
# Runtime: 66 ms, faster than 60.27%
# Memory Usage: 14.2 MB, less than 53.03%
class DoubleSkipForward:
    def deleteNode(self, node: ListNode) -> None:
        current = node
        current.val = current.next.val
        while current.next.next:
            current = current.next
            current.val = current.next.val
        current.next = None


# Since the problem does not ask to free memory, we can simply skip the
# next node in the list.
#
# Time complexity: O(1) - We update a pointer and a value in O(1).
# Space complexity: O(1) - Constant memory.
#
# Runtime: 82 ms, faster than 26.31%
# Memory Usage: 14.3 MB, less than 53.03%
class SkipNext:
    def deleteNode(self, node: ListNode) -> None:
        node.val, node.next = node.next.val, node.next.next


# It turns out that keeping a reference to the next node and deleting it
# after we update the given node is more efficient.
#
# Time complexity: O(1) - We update a pointer and a value in O(1).
# Space complexity: O(1) - Constant memory.
#
# Runtime: 64 ms, faster than 63.46%
# Memory Usage: 14.2 MB, less than 91.10%
class DeleteNext:
    def deleteNode(self, node: ListNode) -> None:
        next = node.next
        node.val, node.next = next.val, next.next
        del next


def test():
    executors = [
        WithPrevPointer,
        DoubleSkipForward,
        SkipNext,
        DeleteNext,
    ]
    tests = [
        [[4, 5, 1, 9], 5, [4, 1, 9]],
        [[4, 5, 1, 9], 1, [4, 5, 9]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                # Instantiate a linked list from the array.
                linked_list = LinkedList.fromList(t[0])
                # Pass the nth node of the list to the method.
                sol.deleteNode(linked_list.getFirstNodeByValue(t[1]))
                # Convert the result to a list to compare.
                result = linked_list.toList()
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
