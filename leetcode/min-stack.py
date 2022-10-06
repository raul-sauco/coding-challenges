# 155. Min Stack
# 🟠 Medium
#
# https://leetcode.com/problems/min-stack/
#
# Tags: Stack - Design

import timeit


# Use a list as the stack, each element of the stack is a tuple and
# holds the value and the current minimum, when we insert, update the
# minimum checking the insert value and the current minimum.
#
# Time complexity: O(1) - All methods run in O(1) or amortized O(1) for
# the push method, it will need to double the array size in O(n) each
# time it finds it full when trying to insert.
# Space complexity: O(n) - Where n is the number of insert operations,
# the stack will grow to that size.
#
# Runtime: 131 ms, faster than 33.6%
# Memory Usage: 18.3 MB, less than 28.40%
class MinStack:
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


# StackNode definition.
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


# Solution using a linked list, each element of the stack is a StackNode
# and holds the value, the current minimum and a link to the next
# element of the stack.
#
# Time complexity: O(1) - All methods run in O(1).
# Space complexity: O(n) - Where n is the number of insert operations,
# we will have n StackNodes in memory.
#
# Runtime: 110 ms, faster than 38.49%
# Memory Usage: 19.2 MB, less than 7.56%
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
    executors = [
        MinStack,
        MinStackLinkedList,
    ]
    tests = [
        [
            [
                "MinStack",
                "push",
                "push",
                "push",
                "getMin",
                "pop",
                "top",
                "getMin",
            ],
            [[], [-2], [0], [-3], [], [], [], []],
            [None, None, None, None, -3, None, 0, -2],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    if call == "push":
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
