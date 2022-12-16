# 232. Implement Queue using Stacks
# 🟢 Easy
#
# https://leetcode.com/problems/implement-queue-using-stacks/
#
# Tags: Stack - Design - Queue

import timeit


# Runtime: 40 ms, faster than 76.97%
# Memory Usage: 13.9 MB, less than 98.86%
class MyQueue:
    # The problem asks to implement a FIFO queue using two stacks and
    # only pushing/popping from the end, no index and/or front access.
    def __init__(self):
        self.write_stack = []
        self.read_stack = []

    # Push in O(1) to the first stack.
    def push(self, x: int) -> None:
        self.write_stack.append(x)

    # The pop method uses a call to the peek method to transfer all
    # elements from the write stack to the read stack, then pops the
    # element at the top.
    # Worst case O(n) - amortized O(1).
    def pop(self) -> int:
        self.peek()
        return self.read_stack.pop()

    # The peek method transfers all elements from the write stack to the
    # read stack and then reads the top one.
    # Worst case O(n) - amortized O(1).
    def peek(self) -> int:
        if not self.read_stack:
            while self.write_stack:
                self.read_stack.append(self.write_stack.pop())
        return self.read_stack[-1]

    # Empty checks whether there are any elements in either of the
    # stacks O(1)
    def empty(self) -> bool:
        return not self.write_stack and not self.read_stack


def test():
    executors = [MyQueue]
    tests = [
        [
            [1, 2, None, None, None],
            ["push", "push", "peek", "pop", "empty"],
            [None, None, 1, 1, False],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                for i, call in enumerate(t[1]):
                    if call == "push":
                        result = getattr(sol, call)(t[0][i])
                    else:
                        result = getattr(sol, call)()
                    exp = t[2][i]
                    assert result == exp, (
                        f"\033[93m» {result} <> {exp}\033[91m for "
                        + f"test {n} using \033[1m{executor.__name__}"
                    )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
