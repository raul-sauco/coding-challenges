# Disk Stacking
# 🔴 Hard
#
# https://www.algoexpert.io/questions/disk-stacking
#
# Tags: Dynamic Programming

import timeit


# Start by sorting the disks, then iterate over the disks in an outer
# loop, for each disk, iterate over all other disks checking if we could
# add the second disk below the first one, if we can, we check if using
# this combination gives the highest height we can obtain while using
# the second disk. We keep a variable with the highest "tower" that we
# have been able to build and the index of the last disk we added, for
# each disk, if we get a better combination, we save both the new max
# height we can have when having this disk as the bottom of the tower,
# and the disk that we would have above it. Once we have processed all
# disk combinations, we get the tallest combination by starting at the
# tallest bottom disk and following the indexes back towards the top of
# the tower.
#
# Time complexity: O(n^2) - For each disk, we compute the result of
# adding it above every other disk.
# Space complexity: O(n) - We have 2 arrays that are both size n.
class Solution:
    def diskStacking(self, disks):
        # Sort the disks, smaller disks first. O(n*log(n))
        disks.sort()
        # The tallest height we have seen and the index of the bottom
        # disk at this height.
        max_height = (0, 0)
        # The height of the tallest column under which we can currently
        # place this disk 0 makes it the top disk.
        dp = [0] * len(disks)
        # An array of disks pointing to the disk above them.
        above = [None] * len(disks)
        # Outer loop runs n times.
        for i, top in enumerate(disks):
            column_height = dp[i] + top[2]
            # Is this this at the bottom of the tallest tower?
            if column_height > max_height[0]:
                max_height = (column_height, i)
            # Iterate over all disks after the current one checking if
            # they are big enough to be placed below this one.
            # Inner loop runs n^2 times. O(n^2).
            for j in range(i + 1, len(disks)):
                bottom = disks[j]
                # If we could place this disk under top.
                if (
                    bottom[0] > top[0]
                    and bottom[1] > top[1]
                    and bottom[2] > top[2]
                ):
                    # Can we maximize the height placing top above bottom?
                    if column_height > dp[j]:
                        dp[j] = column_height
                        above[j] = i
        # Reconstruct the path backwards.
        idx = max_height[1]
        res = []
        while idx is not None:
            res.append(disks[idx])
            idx = above[idx]
        return res[::-1]


def test():
    executors = [Solution]
    tests = [
        [
            [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]],
            [[2, 1, 2], [3, 2, 3], [4, 4, 5]],
        ],
        [
            [
                [3, 3, 4],
                [2, 1, 2],
                [3, 2, 3],
                [2, 2, 8],
                [2, 3, 4],
                [5, 5, 6],
                [1, 2, 1],
                [4, 4, 5],
                [1, 1, 4],
                [2, 2, 3],
            ],
            [[2, 2, 3], [3, 3, 4], [4, 4, 5], [5, 5, 6]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.diskStacking(t[0])
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
