# 225. Implement Stack using Queues
# 🟢 Easy
#
# https://leetcode.com/problems/implement-stack-using-queues/
#
# Tags: Stack - Design - Queue

import timeit
from collections import deque


# Runtime: 36 ms, faster than 82.04%
# Memory Usage: 16.24 MB, less than 92.36%
class MyStack:
    def __init__(self):
        self.q = deque()
        self.t = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self.t = x

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.t = self.q[0]
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.t

    def empty(self) -> bool:
        return len(self.q) == 0


def test():
    executors = [MyStack]
    tests = [
        [
            [1, 2, None, None, None],
            ["push", "push", "top", "pop", "empty"],
            [None, None, 2, 2, False],
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
