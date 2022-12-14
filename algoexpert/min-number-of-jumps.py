# Min Number Of Jumps
# 🔴 Hard
#
# https://www.algoexpert.io/questions/min-number-of-jumps
#
# Tags: Array - Dynamic Programming

import timeit


# Use nested loops and an extra array of number of jumps required to
# reach a position. Visit all the indexes, and use the values in them to
# update the number of jumps required to reach all the positions that
# can be reached from the current index.
#
# Time complexity: O(n^2) - From each index we could end up visiting all
# other indexes.
# Space complexity: O(n) - We use len(array) worth of extra memory.
class BruteForce:
    def minNumberOfJumps(self, array):
        jumps = [float("inf")] * len(array)
        jumps[0] = 0
        for i in range(len(array)):
            for j in range(array[i]):
                idx = i + j + 1
                if i + j + 1 < len(array):
                    jumps[idx] = min(jumps[i] + 1, jumps[idx])
        return jumps[-1]


# Store only the maximum position we can reach at a given point, the
# number of steps we can take without making another jump and the number
# of jumps that we have taken already.
#
# Time complexity: O(n) - We visit each position once and do O(1) work.
# Space complexity: O(1) - We use constant extra memory.
class DP:
    def minNumberOfJumps(self, array):
        if len(array) == 1:
            return 0
        # Visit the first position, consuming one jump to move out.
        max_reach, steps_left, jumps = array[0], array[0], 1
        # We already "visited" the first position and we are trying to
        # reach the last position on the array, not the "position"
        # immediately after the array, iterate from i to len(array) - 1
        for i, val in enumerate(array[1:-1]):
            # Consume one step to get here.
            steps_left -= 1
            # The maximum index we can reach from this position.
            max_reach = max(max_reach, val + i)
            # If we have consumed all steps.
            if not steps_left:
                # We are forced to take a jump.
                jumps += 1
                # We are taking a jump, update the number of steps that
                # we have left until forced to take the next jump.
                steps_left = max_reach - i
        return jumps


def test():
    executors = [
        BruteForce,
        DP,
    ]
    tests = [
        [[1], 0],
        [[1, 1], 1],
        [[1, 1, 1], 2],
        [[3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3], 4],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minNumberOfJumps(t[0])
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
