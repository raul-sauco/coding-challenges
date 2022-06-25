# https://leetcode.com/problems/min-stack/


# Solution using a list as the stack.
# Each element of the stack is a set and holds the value and the current minimum.
#
# Runtime: 172 ms, faster than 22.62% of Python3 online submissions for Min Stack.
# Memory Usage: 18.5 MB, less than 13.03 % of Python3 online submissions for Min Stack.
from typing import Optional


class MinStackList:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        m = min(self.stack[-1][1], val) if self.stack else val
        self.stack.append((val, m))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Solution using a linked list.
# Each element of the stack is a StackNode and holds the value, the current minimum and a
# link to the next element of the stack.
#
# Runtime: 110 ms, faster than 38.49% of Python3 online submissions for Min Stack.
# Memory Usage: 19.2 MB, less than 7.56 % of Python3 online submissions for Min Stack.

class StackNode:
    def __init__(self, val: int, previous=None):
        self.val = val
        self.previous = previous
        self.current_min = min(val, previous.current_min) if previous else val

    def getMin(self):
        return self.current_min

    def getPrevious(self):
        return self.previous

    def getVal(self):
        return self.val


class MinStackLinkedList:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        self.head = StackNode(val, self.head)

    def pop(self) -> None:
        self.head = self.head.getPrevious()

    def top(self) -> int:
        return self.head.getVal()

    def getMin(self) -> int:
        return self.head.getMin()


def test():
    ms = MinStackList()
    ms = MinStackLinkedList()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2


test()
