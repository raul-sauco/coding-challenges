# 1834. Single-Threaded CPU
# 🟠 Medium
#
# https://leetcode.com/problems/single-threaded-cpu/
#
# Tags: Array - Sorting - Heap (Priority Queue)

import timeit
from heapq import heappop, heappush
from typing import List


# Sort the tasks by enqueue time then processing time, use a heap to
# efficiently pick the next task that we need to process when there are
# several candidates, use a variable to simulate the current time to
# determine which tasks are available.
#
# Time complexity: O(n*log(n)) - We need to sort the tasks, we also
# iterate over the tasks and pick one at O(log(n)) cost, if all tasks
# where available from the start, that would also be O(n*log(n)) cost.
# Space complexity: O(n) - The sorted tasks array has the same size as
# the input array, the heap could also reach the same size.
#
# Runtime 2026 ms Beats 88.53%
# Memory 63 MB Beats 33.28%
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sort the tasks by enqueue time then processing time.
        sorted_tasks = sorted(
            [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        )
        # The current time.
        current_time = sorted_tasks[0][0]
        # A min heap of available tasks.
        available = []
        # The resulting order in which the tasks are processed.
        res = []
        # The index of the next task that will became available.
        i = 0
        while available or i < len(tasks):
            # Push all tasks that are available by the current time.
            while i < len(tasks) and sorted_tasks[i][0] <= current_time:
                _, processing_time, task_id = sorted_tasks[i]
                heappush(available, (processing_time, task_id))
                i += 1
            # There may be a gap between the current time and the next
            # available task.
            if not available:
                current_time = sorted_tasks[i][0]
                continue
            # Choose the next task to process.
            processing_time, id = heappop(available)
            # Update the time up to when this task will be done.
            current_time += processing_time
            # Add this task to the result set.
            res.append(id)
        return res


def test():
    executors = [Solution]
    tests = [
        [[[1, 2], [2, 4], [3, 2], [4, 1]], [0, 2, 3, 1]],
        [[[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]], [4, 3, 2, 0, 1]],
        [
            [[5, 2], [7, 2], [9, 4], [6, 3], [5, 10], [1, 1]],
            [5, 0, 1, 3, 2, 4],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.getOrder(t[0])
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
