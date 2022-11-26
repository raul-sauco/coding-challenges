# 1235. Maximum Profit in Job Scheduling
# 🔴 Hard
#
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
#
# Tags: Array - Binary Search - Dynamic Programming - Sorting

import timeit
from bisect import bisect_left, bisect_right
from functools import cache
from operator import itemgetter
from typing import List


# The brute force solution first creates a list of jobs sorted by start
# time, then a depth-first recursive function explores the different
# branches resulting from choosing to schedule or skip the jobs.
#
# Time complexity: O(2^n) - On each level the recursive tree splits into
# two branches.
# Space complexity: O(n) - The call stack can grow to a height of n.
#
# This solution fails with TLE even when using memoization.
class BruteForce:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # Merge all job data into one list of tuples sorted by start.
        jobs = sorted(zip(startTime, endTime, profit))
        # Recursive function that chooses to schedule or not the next
        # job on the sorted list.
        def scheduler(i: int, next_start: int) -> int:
            # Base case, no jobs left.
            if i == len(jobs):
                return 0
            # The max profit choosing to schedule this job.
            use = 0
            if jobs[i][0] >= next_start:
                # If we can schedule this job, the profit will be this
                # jobs profit plus the max we can obtain from the rest
                # of jobs.
                use = jobs[i][2] + scheduler(i + 1, jobs[i][1])
            # If we choose not to use this job, move to the next one.
            skip = scheduler(i + 1, next_start)
            return max(use, skip)

        return scheduler(0, 0)


# Improve the previous solution by using binary search to find the next
# job that could be scheduled when we choose to schedule the current job
# instead of skipping it. We store the best result for each index on the
# job array.
#
# Time complexity: O(n*log(n)) - We compute the max starting at each
# index only one time, for each, we search the next job that can be
# scheduled using binary search, O(log(n)).
# Space complexity: O(n) - Boh the cached results and the call stack
# will grow to the same size as the number of jobs in the input.
#
# Runtime: 596 ms, faster than 92.10%
# Memory Usage: 46.7 MB, less than 23.98%
class Memoization:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # Merge all job data into one list of tuples sorted by start.
        jobs = sorted(zip(startTime, endTime, profit))
        # Recursive function that chooses to schedule or not the next
        # possible job and returns the max profit obtained from there.
        @cache
        def scheduler(i: int) -> int:
            # Base case, no jobs left.
            if i == len(jobs):
                return 0
            # The max profit choosing to schedule this job is the profit
            # from this job plus the maximum profit with the rest of the
            # jobs, the next job we can choose to explore needs to have
            # a start time after the end time of this job.
            use = jobs[i][2] + scheduler(bisect_left(jobs, (jobs[i][1],)))
            # If we choose not to use this job, move to the next one.
            skip = scheduler(i + 1)
            return max(use, skip)

        return scheduler(0)


# Use the same idea as on the memoization solution but reverse it to
# compute the maximum profit up to a given point in time starting from
# the jobs that we can schedule first. We sort the input jobs by end
# time, then iterate over them saving the maximum profit that we can
# make up to a given time t, if we can improve on the current maximum
# profit by scheduling this new job, we schedule it by recording the new
# maximum profit and the current job end time on the dp array. Since
# we are iterating over the jobs based on end time, we are guaranteed to
# have a sorted dp array, that lets us use binary search to find the
# last job we can keep if we decide to use the current one.
#
# Time complexity: O(n*log(n)) - We iterate over all jobs, for each, we
# do binary search on the dp array to find the maximum profit before the
# start time of this job.
# Space complexity: O(n) - The dp array could grow to the size of the
# input.
#
# Runtime: 541 ms, faster than 98.19%
# Memory Usage: 27.1 MB, less than 72.92%
class BottomUpDP:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # Merge all job data into one list of tuples sorted by end time.
        jobs = sorted(zip(startTime, endTime, profit), key=itemgetter(1))
        # At time 0 we can make at most 0 profit.
        dp = [(0, 0)]
        # Iterate over the jobs choosing wether to schedule them or skip
        # them based on how they would affect the maximum profit.
        for start, end, p in jobs:
            # If we decided to use this job, what would be the max
            # profit before we start this job? Index of dp before the
            # start of this job.
            i = bisect_right(dp, (start + 1,)) - 1
            # If we can improve the current max profit by scheduling
            # this job, do it.
            if dp[i][1] + p > dp[-1][1]:
                dp.append((end, dp[i][1] + p))
        return dp[-1][1]


def test():
    executors = [
        BruteForce,
        Memoization,
        BottomUpDP,
    ]
    tests = [
        [[1, 1, 1], [2, 3, 4], [5, 6, 4], 6],
        [[1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120],
        [[1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.jobScheduling(t[0], t[1], t[2])
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
