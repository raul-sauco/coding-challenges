# 207. Course Schedule
# 🟠 Medium
#
# https://leetcode.com/problems/course-schedule/
#
# Tags: Depth-First Search - Breadth-First Search - Graph - Topological Sort

import timeit
from collections import defaultdict, deque
from typing import List


# Use Kahn's algorithm of topological sorting to obtain two dictionaries
# one with the course as the key and the indegree as the value, another
# also with the courses as key but with a list of other courses that
# depend on them, outdegree vertexes, as the value.
#
# Creating the dictionaries takes O(n) to iterate over the courses and
# O(1) to append entries to the dictionaries.
#
# Once we have that list, we create a queue containing all the courses
# that do not have any dependencies, the ones that don't have an entry
# in the indegree dictionary.
#
# On this step we also iterate over the input to check if the course is
# in the dictionary indegree. O(n)
#
# Then we start popping courses from the queue, for each course, we
# visit each of its dependents on the dependencies dictionary values,
# for each, we register that we have cleared one dependency, by
# subtracting one from its indegree. If the indegree has reached 0, we
# have cleared all dependencies, remove that course from the indegree
# dictionary and add it to the queue to be processed later.
#
# When we run out of courses to process in the queue, we are done. If
# there are any entries left in the indegree dictionary, it means that
# there is at least one course that we could not take, because we didn't
# manage to clear its dependencies, return False, otherwise, we took all
# the courses and we can return True.
#
# Time complexity: O(n+p) - The complexity comes from looping through
# all dependencies of the elements we pop from the queue. We have n
# nodes and a total of p elements in the dependencies list, where p is
# the number of edges in the graph.
# Space complexity: O(n+p) - The indegree dictionary and the queue have
# a max of O(n) size but, the dependencies dictionary will have a total
# of p elements between all the dependencies lists.
#
# Runtime: 110 ms, faster than 86.14%
# Memory Usage: 15.7 MB, less than 70.84%
class BFS:
    def canFinish(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        # Use a dictionary to store the indegree and the dependencies.
        indegree = defaultdict(int)
        dependencies = defaultdict(list)
        # Iterate over the prerequisites adding the data.
        for course, prereq in prerequisites:
            indegree[course] += 1
            dependencies[prereq].append(course)

        # Use a queue for courses that we can take at this point, they
        # either did not have any requirements or we have cleared them.
        # Add any courses that did not have any prerequisites to the
        # queue.
        queue = deque([c for c in range(numCourses) if c not in indegree])
        # While we can process courses from the queue of available ones.
        while queue:
            course = queue.popleft()
            # Visit all this course's dependencies removing one indegree.
            for dependent in dependencies[course]:
                indegree[dependent] -= 1
                # If we have taken all prerequisite courses, add this
                # course to the list of courses available to be taken.
                if indegree[dependent] == 0:
                    queue.append(dependent)
                    del indegree[dependent]
            # Remove this course from the dependencies dictionary.
            del dependencies[course]

        # Return true if we could take all the courses, false if not.
        return not indegree


# The depth-first search solution uses a dictionary of courses with
# their dependencies as values, and a set to detect cyclic dependencies.
# Iterate over all courses recursively checking if we can clear all
# their dependencies.
#
# Time complexity: O(n+p) - n: number of nodes, p: number of edges, we
# will visit a node or an edge a constant number of times maximum.
# Space complexity: O(n+p) - The dictionary will contain one entry per
# node, the sum of values in the lists will be equal to the number of
# edges in the graph.
#
# Runtime: 141 ms, faster than 64.02%
# Memory Usage: 17.1 MB, less than 40.01%
class DFS:
    def canFinish(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        # Dictionary course => list[prerequisites]
        prereqs = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            prereqs[c].append(p)
        # Set to detect cyclic dependencies while exploring course
        # dependencies.
        seen = set()
        # Recursive function to explore course dependencies.
        def dfs(course):
            # If we see a course that we have seen already along this
            # branch, we have found a cyclic dependency, it won't be
            # possible to complete all courses.
            if course in seen:
                return False
            # If this course does not have any dependencies, we can
            # "take" it now and mark it as cleared.
            if prereqs[course] == []:
                return True
            # If we are going to explore this courses dependencies, mark
            # this course as seen to detect cycles.
            seen.add(course)
            # Recursively check if we can clear this dependency.
            for prereq in prereqs[course]:
                # If we found one dependency that we could not clear, we
                # won't be able to clear this course either.
                if not dfs(prereq):
                    return False
            # Clear this course from the seen set before we move to
            # another sub-branch of the exploration.
            seen.remove(course)
            # If we have cleared all requirements, mark this course as
            # cleared to avoid recalculating if we can clear it. This
            # is equivalent to keeping a DP structure with the result
            # of exploring this branch of the DFS, but we can use the
            # original dictionary.
            prereqs[course] = []
            return True

        # Explore all possible courses in the input, if we have cleared
        # a course previously, we will get a result in O(1)
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        # If we can take all the courses, return True.
        return True


def test():
    executors = [BFS, DFS]
    tests = [
        [2, [[1, 0]], True],
        [2, [[1, 0], [0, 1]], False],
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
            False,
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
            True,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.canFinish(t[0], t[1])
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
