# Waterfall Streams
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/waterfall-streams
#
# Tags: Arrays

import timeit


# Simulate the water flow through the matrix, when we hit an obstacle,
# try to flow left and right, discard flows that get interrupted.
#
# Time complexity: O(m*n^2) - Where m is the number of rows and n is the
# number of columns in the matrix, we iterate over all rows, for each
# row we visit all positions checking if they contain water, if they do,
# we may check n positions in the matrix until we find where the water
# will fall or decide that it gets stuck.
# Space complexity: O(n) - We store n values in memory.
class Solution:
    def waterfallStreams(self, array, source):
        rows, cols = len(array), len(array[0])
        dp = [0] * cols
        # All the water falls below the source.
        dp[source] = 100
        for row in range(1, rows):
            # The amount of water that each column will see through.
            buckets = [0] * cols
            for col, water in enumerate(dp):
                if water:
                    if array[row][col] == 0:
                        buckets[col] += water
                    else:
                        # Some water flows left.
                        for idx in range(col - 1, -1, -1):
                            # If there is a block in the previous row,
                            # the water will become trapped.
                            if array[row - 1][idx] == 1:
                                break
                            # If the water could flow here and it can
                            # fall into this bucket, it will.
                            if array[row][idx] == 0:
                                buckets[idx] += water / 2
                                break
                        # Some water flows right.
                        for idx in range(col + 1, cols):
                            # If there is a block in the previous row,
                            # the water will become trapped.
                            if array[row - 1][idx] == 1:
                                break
                            # If the water could flow here and it can
                            # fall into this bucket, it will.
                            if array[row][idx] == 0:
                                buckets[idx] += water / 2
                                break
            dp = buckets[::]
        return dp


def test():
    executors = [Solution]
    tests = [
        [[[0], [0], [0], [0], [0], [0], [0]], 0, [100]],
        [[[0], [0], [0], [1], [0], [0], [0]], 0, [0]],
        [
            [
                [0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0],
            ],
            3,
            [0, 0, 0, 25, 25, 0, 0],
        ],
        [
            [
                [0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 1],
                [0, 0, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0],
            ],
            6,
            [0, 0, 0, 0, 0, 0, 0],
        ],
        [
            [
                [0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 1],
                [0, 0, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
            ],
            3,
            [25, 6.25, 0, 0, 0, 6.25, 0],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.waterfallStreams(t[0], t[1])
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
