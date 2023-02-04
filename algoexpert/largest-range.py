# Largest Range
# 🔴 Hard
#
# https://www.algoexpert.io/questions/largest-range
#
# Tags: Array - Hashmap - Two Pointers

import timeit


# The obvious solution would be to sort the input and remove duplicates,
# then iterate over the sorted input counting the length of contiguous
# sequences.
#
# Time complexity: O(n*log(n)) - Sorting has the highest complexity.
# Space complexity: O(n) - Sorting in Python takes up to n/2 memory.
class SortingSolution:
    def largestRange(self, array):
        # Write your code here.
        array = sorted(set(array))
        res = [array[0], array[0]]
        current = [array[0], array[0]]
        for i in range(1, len(array)):
            if array[i] == array[i - 1] + 1:
                current[1] = array[i]
            else:
                if current[1] - current[0] > res[1] - res[0]:
                    res = current
                current = [array[i], array[i]]
        if current[1] - current[0] > res[1] - res[0]:
            res = current
        return res


# We can use a hash set and a two pointer approach, create a set of all
# numbers in the input, then start iterating over all the contiguous
# ranges that we can find removing them from the set, to do it, first we
# pop one value from the set and use two pointers to travel left and
# right until we arrive at a gap in the contiguous values, when we have
# computed the current range, check if it is the largest that we have
# seen and move onto the next.
#
# Time complexity: O(n) - We iterate twice over all elements in the
# input doing constant work. If we knew the max value of any element in
# the input, we could improve the algorithm using an array instead of
# the hashmap, saving the cost of hashing.
# Space complexity: O(n) - The hashmap.
class LinearSolution:
    def largestRange(self, array):
        # Register numbers that we have.
        have = {num for num in array}
        res = [array[0], array[0]]
        # Iterate while we haven't visited all ranges.
        while have:
            # Pop any random element and visit all the contiguous
            # elements removing them from the set.
            num = have.pop()
            # Initialize two pointers.
            l = r = num
            # Move left while that value was in the input.
            while l - 1 in have:
                l -= 1
                have.remove(l)
            # Move right while that value was in the input.
            while r + 1 in have:
                r += 1
                have.remove(r)
            # If this range is greater than the previous best, update it.
            if r - l > res[1] - res[0]:
                res = [l, r]
        return res


def test():
    executors = [
        SortingSolution,
        LinearSolution,
    ]
    tests = [
        [[1, 1, 1, 3, 4], [3, 4]],
        [[8, 4, 2, 10, 3, 6, 7, 9, 1], [6, 10]],
        [
            [
                19,
                -1,
                18,
                17,
                2,
                10,
                3,
                12,
                5,
                16,
                4,
                11,
                8,
                7,
                6,
                15,
                12,
                12,
                2,
                1,
                6,
                13,
                14,
            ],
            [10, 19],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.largestRange(t[0])
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
