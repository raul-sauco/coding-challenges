# Task Assignment
# 🟠 Medium
#
# https://www.algoexpert.io/questions/task-assignment
#
# Tags: Array - Greedy - Sorting

import timeit
from collections import deque
from operator import itemgetter


# Sort the tasks on ascending order by cost, use a double ended queue
# to be able to pop from both ends, assign to each worker the next
# easiest and hardest job, that way we optimize the time that each
# worker needs and get the best overall runtime.
#
# Time complexity: O(n*log(n)) - Sorting the jobs has the highest cost.
# Space complexity: O(n) - The queue that contains the sorted jobs.
class UseQueue:
    def taskAssignment(self, k, tasks):
        # Sorted list of tasks and their indexes.
        q = deque(sorted([(tasks[i], i) for i in range(len(tasks))]))
        res = [None] * k
        for i in range(k):
            res[i] = (q.popleft()[1], q.pop()[1])
        return res


class UseIndexes:
    def taskAssignment(self, k, tasks):
        t = sorted(
            [(i, task) for i, task in enumerate(tasks)], key=itemgetter(1)
        )
        return [(t[i][0], t[-i - 1][0]) for i in range(k)]


def test():
    executors = [
        UseQueue,
        UseIndexes,
    ]
    tests = [
        [3, [1, 3, 5, 3, 1, 4], [(0, 2), (4, 5), (1, 3)]],
        [
            5,
            [3, 7, 5, 4, 4, 3, 6, 8, 3, 3],
            [(0, 7), (5, 1), (8, 6), (9, 2), (3, 4)],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.taskAssignment(t[0], t[1])
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
