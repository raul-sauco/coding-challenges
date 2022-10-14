# 876. Middle of the Linked List
# 🟢 Easy
#
# https://leetcode.com/problems/middle-of-the-linked-list/
#
# Tags: Linked List - Two Pointers

import timeit
from typing import Optional

from data import LinkedList, ListNode


# Use the fast&slow pointers technique, for each two moves of the fast
# pointer, we can move the slow pointer once.
#
# Time complexity: O(n) - We visit each node at most once.
# Space complexity: O(1) - Constant extra memory used.
#
# Runtime: 32 ms, faster than 91.11%
# Memory Usage: 13.8 MB, less than 95.69%
class Shuffle:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = fast = head
        shuffle = True
        while fast.next:
            # Always move the fast pointer.
            fast = fast.next
            # Only move the slow pointer every second time.
            if shuffle:
                slow = slow.next
            shuffle = not shuffle
        return slow


# Use the fast&slow pointers technique, for each two moves of the fast
# pointer, we can move the slow pointer once.
#
# Time complexity: O(n) - We visit each node at most once.
# Space complexity: O(1) - Constant extra memory used.
#
# Runtime: 29 ms, faster than 96.88%
# Memory Usage: 13.7 MB, less than 95.57%
class FastAndSlow:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head is guaranteed to not be null.
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


def test():
    executors = [
        Shuffle,
        FastAndSlow,
    ]
    tests = [
        [[1], [1]],
        [[1, 2], [2]],
        [[1, 2, 3], [2, 3]],
        [[1, 2, 3], [2, 3]],
        [[1, 2, 3, 4], [3, 4]],
        [[1, 2, 3, 4, 5], [3, 4, 5]],
        [[1, 2, 3, 4, 5, 6], [4, 5, 6]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                middle = sol.middleNode(head)
                result = LinkedList(middle).toList()
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
