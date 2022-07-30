# 621. Task Scheduler
# 🟠 Medium
#
# https://leetcode.com/problems/task-scheduler/
#
# Tags: Array - Hash Table  - Greedy - Sorting - Heap (Priority Queue)
# - Counting

import timeit
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush
from typing import List


# A first, brute-force, approach to solving the problem would be to
# simulate the CPU executing the tasks and count how many units of time
# are used up.
#
# Time complexity: O(n+log(27)) => O(n) - For each element m in the
# input, we pop from the heap in O(log(27)) => O(1) and add/remove from
# the pending dictionary in O(1), the max complexity comes from
# reordering the heap but it is still O(1) because the input can have
# a max of 27 unique tasks, the capital letters of the English
# alphabet, hence the heap can only grow to size 27.
# Space complexity: O(1) - The heap and dictionary both can grow to
# size k where k is the number of unique tasks in the input. Since the
# unique tasks number is limited by the number of capital letters in the
# English alphabet, 27, therefore O(1).
#
# Runtime: 1235 ms, faster than 12.84% of Python3 online submissions for
# Task Scheduler.
# Memory Usage: 14.3 MB, less than 90.02% of Python3 online submissions
# for Task Scheduler.
class HeapAndDictionary:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # If we don't have a cooldown period, we can execute 1 task per
        # time unit, we will use len(tasks) time units.
        if n == 0:
            return len(tasks)
        # Count the tasks.
        c = Counter(tasks)
        # Initialize the used-up time-units.
        # We will use the time_unit value as the index of when a task
        # was last executed to check if we can execute it again at
        # another point in time.
        time_cycle = 0
        # Create a list of size k. k = num unique tasks.
        available = [None] * len(c)
        for i, t in enumerate(c):
            # Add all the tasks to the list as tuples of (-count, id)
            available[i] = (-c[t], t)
        # Heapify the items. O(n)
        # Better than heappush for each in O(n*log(n))
        heapify(available)
        # Keep waiting tasks in a dictionary indexed by the time-unit in
        # which we can re-add them to the available tasks.
        # The value of each entry is a list of tasks we can perform.
        pending = defaultdict(list)
        # Execute tasks while we have available or pending tasks.
        while available or pending:
            time_cycle += 1
            # First add all pending tasks we can execute in this time
            # cycle to the available pool (heap).
            if time_cycle in pending:
                for task in pending[time_cycle]:
                    heappush(available, task)
                # Remove the entry from the dictionary.
                del pending[time_cycle]
            # If we have any tasks on the queue, execute them, otherwise
            # this is an idle cycle.
            if available:
                # Execute the task with the highest priority from the
                # available pool of tasks.
                task = heappop(available)
                # Mark the task as executed once. Since priorities are
                # negative due to the min heap, add 1 until we get to 0.
                task = (task[0] + 1, task[1])
                # If we have to execute the time more times.
                if task[0] < 0:
                    # Push it into the pending tasks. We know that the
                    # cooldown period n > 0, we cannot execute in the next
                    # cycle. We will have to skip n cycles.
                    pending[time_cycle + n + 1].append(task)
        # Return the number of cycles we have executed.
        return time_cycle


# Similar example to the previous solution, but use a deque instead of
# the dictionary to store pending tasks. Also optimize a bit the memory
# usage storing only the number of executions we have left without
# storing the task name.
#
# Time complexity: O(n) - We iterate over the array popping and pushing
# into the heap that has a max size of 27.
# Space complexity: O(1) - Both the queue and the heap are limited in
# size to 27.
#
# Runtime: 647 ms, faster than 73.09% of Python3 online submissions for
# Task Scheduler.
# Memory Usage: 14.5 MB, less than 39.44% of Python3 online submissions
# for Task Scheduler.
class HeapAndDeque:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # If we don't have a cooldown period, we can execute 1 task per
        # time unit, we will use len(tasks) time units.
        if n == 0:
            return len(tasks)
        # Count the tasks.
        c = Counter(tasks)
        # Initialize the used-up time-units.
        # We will use the time_unit value as the index of when a task
        # was last executed to check if we can execute it again at
        # another point in time.
        time_cycle = 0
        # Create a list of size k. k = num unique tasks.
        available = [-time for time in c.values()]
        # Heapify the items. O(n)
        # Better than heappush for each in O(n*log(n))
        heapify(available)
        # Keep waiting tasks in a dictionary indexed by the time-unit in
        # which we can re-add them to the available tasks.
        # The value of each entry is a list of tasks we can perform.
        pending = deque()
        # Execute tasks while we have available or pending tasks.
        while available or pending:
            time_cycle += 1
            # If we have any tasks on the queue, execute them, otherwise
            # this is an idle cycle.
            if available:
                # Execute the task with the highest priority from the
                # available pool of tasks.
                # Mark the task as executed once. Since priorities are
                # negative due to the min heap, add 1 until we get to 0.
                count = 1 + heappop(available)
                # If we have to execute the time more times.
                if count:
                    # Push it into the pending tasks.
                    pending.append((count, time_cycle + n))
            # If we have a task in the pending queue that could be
            # executed next cycle, pop it and append it to the heap.
            if pending and pending[0][1] == time_cycle:
                heappush(available, pending.popleft()[0])

        # Return the number of cycles we have executed.
        return time_cycle


# There is a more efficient solution that we can deduce looking at the
# possible ways to arrange the tasks in the intervals given by n.
# This solution is interesting because we can find a way to calculate
# the result, as opposed to computing it.
# There is a detailed explanation here:
#
# https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation
#
# Time complexity: O(n) - The counter iterates over the whole input.
# Space complexity: O(1) - Same as above, the counter size maxes out at
# 27.
#
# Runtime: 553 ms, faster than 84.44% of Python3 online submissions for
# Task Scheduler.
# Memory Usage: 14.4 MB, less than 39.44% of Python3 online submissions
# for Task Scheduler.
class Math:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = list(Counter(tasks).values())
        max_count = max(tasks_count)
        max_count_tasks = tasks_count.count(max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)


def test():
    executors = [HeapAndDictionary, HeapAndDeque, Math]
    tests = [
        [["D"], 0, 1],
        [["D", "D"], 8, 10],
        [["A", "A", "A", "B", "B", "B"], 2, 8],
        [["A", "A", "A", "B", "B", "B"], 0, 6],
        [["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1e4"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.leastInterval(t[0], t[1])
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
