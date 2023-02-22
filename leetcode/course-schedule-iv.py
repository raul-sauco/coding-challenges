# 1462. Course Schedule IV
# 🟠 Medium
#
# https://leetcode.com/problems/course-schedule-iv/
#
# Tags: Depth-First Search - Breadth-First Search - Graph - Topological Sort

import timeit
from typing import List


# Use topological sort to create an array where each entry i is a set
# with all the dependencies of the i-th course, direct and indirect ones,
# once we have that array, we can perform each query in O(1), given the
# constraints of the problem, it is better to use a bit more time
# building this data structure, even if the complexity of that is high,
# O(n^3+p) because we know that n <= 100 is a small value. After that
# the queries, of which we could have up to 10^4, can run in O(1).
#
# Time complexity: O(n^3 + p) - The last loop where we go along the
# topographical order processing nodes and creating the all_dependencies
# array has 3 nested loops all of which have an upper limit of n. The
# third loop is implicit, the copy of set elements from a dependency to
# the current node.
# Space complexity: O(n^2) - The arrays of size n have elements which
# in turn are sets of size n.
#
# Runtime 738 ms Beats 87.53%
# Memory 18.1 MB Beats 11.16%
class TopologicalSort:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        # Create two hashmaps with indegree and outdegree. O(n)
        direct_dependencies = [set() for _ in range(numCourses)]
        is_depended_on = [set() for _ in range(numCourses)]
        # Iterate over the prerequisites adding them to the hashmaps,
        # this will take O(p)
        for depended, dependent in prerequisites:
            direct_dependencies[dependent].add(depended)
            is_depended_on[depended].add(dependent)
        # Copy the dependencies, direct dependencies only has p
        # dependencies, this is also O(p)
        all_dependencies = [s.copy() for s in direct_dependencies]
        # Process courses that don't have any remaining dependencies. O(n)
        stack = [i for i in range(numCourses) if not direct_dependencies[i]]
        # Iterate over the courses on the stack, courses go on the stack
        # once we have processed oll their dependencies, this loop will
        # run a maximum of n times O(n)
        while stack:
            current = stack.pop()
            # Iterate over all courses that depend on this one at this
            # point, is_depended_on includes only direct dependencies
            # even though it is likely to be much smaller than n, that
            # is its upper bound. O(n)
            for dependent in is_depended_on[current]:
                # Union the indirect dependencies from this dependency.
                # A node could be dependent in all others, O(n)
                all_dependencies[dependent] |= all_dependencies[current]
                direct_dependencies[dependent].remove(current)
                # Once we have processed all dependencies, we can
                # process this course.
                if not direct_dependencies[dependent]:
                    stack.append(dependent)
        return [u in all_dependencies[v] for u, v in queries]


def test():
    executors = [TopologicalSort]
    tests = [
        [2, [], [[1, 0], [0, 1]], [False, False]],
        [2, [[1, 0]], [[0, 1], [1, 0]], [False, True]],
        [3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]], [True, True]],
        [
            5,
            [[3, 4], [2, 3], [1, 2], [0, 1]],
            [[0, 4], [4, 0], [1, 3], [3, 0]],
            [True, False, True, False],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.checkIfPrerequisite(t[0], t[1], t[2])
                exp = t[3]
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
