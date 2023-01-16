# Topological Sort
# 🔴 Hard
#
# https://www.algoexpert.io/questions/topological-sort
#
# Tags: Famous Algorithms

import timeit
from collections import deque


# Implement a classical example of topological sort.
#
# Time complexity: O(j+d) - First we iterate over all the dependencies d
# to create the dictionaries, then we iterate over all jobs j, and in
# a nested loop again over all their dependencies (still d).
# Space complexity: O(j+d) - The dependents dictionary has size d, the
# dependencies dictionary only holds one integer per job.
class Solution:
    def topologicalSort(self, jobs, deps):
        # A dictionary of job: jobs that depend on it.
        dependents = {job: [] for job in jobs}
        # A dictionary of job: number of jobs it depends on.
        dependencies = {job: 0 for job in jobs}
        for depended, dependant in deps:
            dependents[depended].append(dependant)
            dependencies[dependant] += 1
        # Find all the jobs that do not have any dependencies and add them to a queue.
        available = deque(
            [job for job in dependencies.keys() if dependencies[job] == 0]
        )
        processed = []
        while available:
            # Pop the next job and add it to the processed jobs.
            job = available.popleft()
            processed.append(job)
            for dependent in dependents[job]:
                dependencies[dependent] -= 1
                if not dependencies[dependent]:
                    available.append(dependent)
        return processed if len(processed) == len(jobs) else []


def test():
    executors = [Solution]
    tests = [
        [[1, 2, 3, 4, 5], [], [1, 2, 3, 4, 5]],
        [[1, 2, 3, 4], [[1, 2], [1, 3], [4, 2], [4, 3], [2, 1]], []],
        [[1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]], [1, 4, 3, 2]],
        [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [
                [3, 1],
                [8, 1],
                [8, 7],
                [5, 7],
                [5, 2],
                [1, 4],
                [1, 6],
                [1, 2],
                [7, 6],
            ],
            [3, 5, 8, 1, 7, 4, 2, 6],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.topologicalSort(t[0], t[1])
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
