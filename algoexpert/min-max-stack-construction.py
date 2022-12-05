# Min Max Stack Construction
# 🟠 Medium
#
# https://www.algoexpert.io/questions/min-max-stack-construction
#
# Tags: Array - Stack - Design

import timeit


# Use a stack of tuples that store the current minimum and maximum
# values as elements are inserted.
class MinMaxStack:
    def __init__(self):
        # A stack of tuples (value, current_max, current_min)
        self.stack = []

    # O(1)
    def peek(self):
        if self.stack:
            return self.stack[-1][0]
        return None

    # O(1)
    def pop(self):
        if self.stack:
            return self.stack.pop()[0]
        return None

    # O(1)
    def push(self, number):
        if not self.stack:
            self.stack.append((number, number, number))
        else:
            self.stack.append(
                (
                    number,
                    max(number, self.stack[-1][1]),
                    min(number, self.stack[-1][2]),
                )
            )

    # O(1)
    def getMin(self):
        if self.stack:
            return self.stack[-1][2]
        return None

    # O(1)
    def getMax(self):
        if self.stack:
            return self.stack[-1][1]
        return None


def test():
    executors = [
        MinMaxStack,
    ]
    tests = [
        [
            [
                "MinMaxStack",
                "push",
                "getMin",
                "getMax",
                "peek",
                "push",
                "getMin",
                "getMax",
                "peek",
                "push",
                "getMin",
                "getMax",
                "peek",
                "pop",
                "pop",
                "getMin",
                "getMax",
                "peek",
            ],
            [
                [],
                [5],
                [],
                [],
                [],
                [7],
                [],
                [],
                [],
                [2],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
            ],
            [None, None, 5, 5, 5, None, 5, 7, 7, None, 2, 7, 2, 2, 7, 5, 5, 5],
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
