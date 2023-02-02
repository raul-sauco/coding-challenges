# Linked List Palindrome
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/linked-list-palindrome
#
# Tags: Linked List

import timeit

from utils.linked_list import LinkedList


# Get the length of the list, then traverse to its middle node, or the
# middle point between two nodes for lists with an even number of nodes,
# reversing the first half of the list, then simultaneously traverse the
# tail of the list and the reversed front checking that the node values
# are the same.
#
# Time complexity: O(n) - We traverse the list twice at most, for each
# node, we do O(1) work.
# Space complexity: O(1) - We only store and manipulate pointers.
class Solution:
    def linkedListPalindrome(self, head):
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
            if prev.value != next.value:
                return False
            # Move one node away from the middle
            prev = prev.next
            next = next.next
        return True


def test():
    executors = [Solution]
    tests = [
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
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result = sol.linkedListPalindrome(head)
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
