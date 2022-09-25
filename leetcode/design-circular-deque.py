# 641. Design Circular Deque
# 🟠 Medium
#
# https://leetcode.com/problems/design-circular-deque/
#
# Tags: Array - Linked List - Design - Queue

from __future__ import annotations

import timeit

from data import serializeLinkedList


# A doubly linked list node.
class DListNode:
    def __init__(
        self,
        prev: DListNode = None,
        next: DListNode = None,
        val: int = 0,
    ):
        self.prev = prev
        self.next = next
        self.val = val

    def __repr__(self):
        return f"DListNode({self.val})"


# Create a data structure that complies with the given requirements.
# One way to do it is to use a doubly linked list.
#
# Runtime: 187 ms, faster than 5.29%
# Memory Usage: 15 MB, less than 20.44%
class MyCircularDeque:
    def __init__(self, k: int):
        self.max_size = k
        self.current_size = 0
        self.back = None
        self.front = None

    # Insert to the front in O(1)
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        node = DListNode(val=value)
        if self.isEmpty():
            self.back = node
        else:
            self.front.prev = node
            node.next = self.front
        self.front = node
        self.current_size += 1
        return True

    # Insert to the back in O(1)
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        node = DListNode(val=value)
        if self.isEmpty():
            self.front = node
        else:
            self.back.next = node
            node.prev = self.back
        self.back = node
        self.current_size += 1
        return True

    # Delete from the front in O(1)
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.current_size == 1:
            self.back = self.front = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.current_size -= 1
        return True

    # Delete from the back in O(1)
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.current_size == 1:
            self.back = self.front = None
        else:
            self.back = self.back.prev
            self.back.next = None
        self.current_size -= 1
        return True

    # Get the element at the front of the queue in O(1)
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    # Get the element at the back of the queue in O(1)
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.back.val

    # Check if the queue is empty in O(1)
    def isEmpty(self) -> bool:
        return self.current_size == 0

    # Check if the queue is full in O(1)
    def isFull(self) -> bool:
        return self.current_size == self.max_size


def test():
    executors = [MyCircularDeque]
    tests = [
        [
            [
                "MyCircularDeque",
                "insertLast",
                "insertLast",
                "insertFront",
                "insertFront",
                "getRear",
                "isFull",
                "deleteLast",
                "insertFront",
                "getFront",
            ],
            [[3], [1], [2], [3], [4], [], [], [], [4], []],
            [None, True, True, True, False, 2, True, True, True, 4],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                # The capacity comes wrapped in an array, unwrap it.
                sol = executor(t[1][0][0])
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    # Only the enqueue call takes arguments
                    if call == "insertLast" or call == "insertFront":
                        result = getattr(sol, call)(t[1][i][0])
                    else:
                        result = getattr(sol, call)()
                    exp = t[2][i]
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
