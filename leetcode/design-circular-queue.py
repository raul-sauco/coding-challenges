# 622. Design Circular Queue
# 🟠 Medium
#
# https://leetcode.com/problems/design-circular-queue/
#
# Tags: Array - Linked List - Design - Queue

from __future__ import annotations

import timeit


# A doubly linked list node.
class DListNode:
    def __init__(
        self,
        next: DListNode = None,
        val: int = 0,
    ):
        self.next = next
        self.val = val

    def __repr__(self):
        return f"DListNode({self.val})"


# Create a data structure that complies with the given requirements.
#
# Runtime: 80 ms, faster than 82.83%
# Memory Usage: 14.7 MB, less than 21.40%
class MyCircularQueue:
    def __init__(self, k: int):
        self.max_size = k
        self.current_size = 0
        self.back = None
        self.front = None

    # Enqueue works in O(1) - returns False if there is no room for the
    # new node.
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # Create a new node
        node = DListNode(val=value)
        if self.isEmpty():
            # Create a node and link it to itself.
            # Linking the node to itself simplifies inserting later.
            self.front = node
        else:
            # Update the back pointers.
            self.back.next = node
        # Always link to back
        self.back = node
        # Always increase the size.
        self.current_size += 1
        return True

    # Removes the element at the front in O(1) - returns false if the
    # queue is empty.
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # Special case, this is the only element.
        if self.current_size == 1:
            self.current_size = 0
            self.back = None
            self.front = None
            return True
        # Get the next node from the front, it could be self.back.
        self.front = self.front.next
        self.current_size -= 1
        return True

    # Get the element at the front of the queue in O(1)
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    # Get the element at the back of the queue in O(1)
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.back.val

    # Check if the queue is empty in O(1)
    def isEmpty(self) -> bool:
        return self.current_size == 0

    # Check if the queue is full in O(1)
    def isFull(self) -> bool:
        return self.current_size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()pass


def test():
    executors = [MyCircularQueue]
    tests = [
        [
            [
                "MyCircularQueue",
                "enQueue",
                "enQueue",
                "enQueue",
                "enQueue",
                "Rear",
                "isFull",
                "deQueue",
                "enQueue",
                "Rear",
            ],
            [[3], [1], [2], [3], [4], [], [], [], [4], []],
            [None, True, True, True, False, 3, True, True, True, 4],
        ],
        [
            [
                "MyCircularQueue",
                "enQueue",
                "enQueue",
                "deQueue",
                "enQueue",
                "deQueue",
                "enQueue",
                "deQueue",
                "enQueue",
                "deQueue",
                "Front",
            ],
            [[2], [1], [2], [], [3], [], [3], [], [3], [], []],
            [None, True, True, True, True, True, True, True, True, True, 3],
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
                    if call == "enQueue":
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
