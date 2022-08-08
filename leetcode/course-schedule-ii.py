# 210. Course Schedule II
# 🟠 Medium
#
# https://leetcode.com/problems/course-schedule-ii/
#
# Tags: Depth-First Search - Breath-First Search - Graph - Topological Sort

import timeit
from collections import defaultdict, deque
from typing import List


# The problem is just asking for the topological sorting of the
# dependencies graph. This is similar to Course Schedule I but, instead
# of returning if it is possible to complete all the courses, we add
# them to a list as we order them and return it.
#
# Time complexity: O(n+p) - We iterate over the courses in O(n) to
# create the dictionaries, then iterate again over them as we are
# popping them from the queue and check all their dependencies, if we
# call p the number of edges in the graph, we will iterate over n + p.
# Space complexity: O(n+p) - We store nodes and edges in the
# dependencies dictionary.
#
# Runtime: 125 ms, faster than 77.63%
# Memory Usage: 15.6 MB, less than 61.66%
class Solution:
    def findOrder(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        # Store indegree and dependencies in a dictionary each.
        indegree = defaultdict(int)
        dependencies = defaultdict(list)
        # Create an empty array to store the sorted courses.
        result = []
        # Iterate over the courses adding their dependencies to the
        # dictionaries.
        for course, prereq in prerequisites:
            indegree[course] += 1
            dependencies[prereq].append(course)

        # Create a queue to process courses and add all courses that do
        # not have any dependencies to start over with.
        queue = deque([c for c in range(numCourses) if c not in indegree])

        # Start processing courses from the queue.
        while queue:
            # Course is a digit in the range [0..len(numCourses) - 1]
            course = queue.popleft()
            result.append(course)

            # Processing this course means that we are "taking" this
            # course, remove it from the prerequisites of any dependent
            # courses. We do that by simply subtracting 1 to the
            # indegree.
            for dependent_course in dependencies[course]:
                indegree[dependent_course] -= 1
                # If we have completed all the courses dependencies,
                # we can take this course now, add it to the queue.
                if indegree[dependent_course] == 0:
                    queue.append(dependent_course)
                    del indegree[dependent_course]

            # Remove this entry from the dependencies dictionary, this
            # is not necessary, but, since it is O(1), why not!
            del dependencies[course]

        # If we could not clear all the dependencies, return an empty
        # array
        if indegree:
            return []
        return result


def test():
    executors = [Solution]
    tests = [
        [2, [[1, 0]], [0, 1]],
        [4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3]],
        [1, [], [0]],
        [2, [[1, 0]], [0, 1]],
        [2, [[1, 0], [0, 1]], []],
        [
            20,
            [
                [0, 10],
                [3, 18],
                [5, 5],
                [6, 11],
                [11, 14],
                [13, 1],
                [15, 1],
                [17, 4],
            ],
            [],
        ],
        [
            20,
            [
                [13, 1],
                [0, 10],
                [5, 3],
                [17, 4],
                [6, 11],
                [11, 14],
                [14, 5],
                [3, 18],
                [15, 1],
            ],
            [
                1,
                2,
                4,
                7,
                8,
                9,
                10,
                12,
                16,
                18,
                19,
                13,
                15,
                17,
                0,
                3,
                5,
                14,
                11,
                6,
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.findOrder(t[0], t[1])
                exp = t[2]
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
