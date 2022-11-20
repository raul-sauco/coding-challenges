# Right Smaller Than
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/right-smaller-than
#
# Tags: Binary Search Tree - Binary Indexed Tree

import timeit
from typing import List


# A specialized binary indexed tree that counts numbers equal or smaller
# than.
class BITree:
    def __init__(self, n: int):
        self.sums = [0] * (n + 1)

    def __repr__(self):
        return "BITree({})".format(self.sums)

    def update(self, idx: int) -> None:
        idx += 1
        while idx < len(self.sums):
            self.sums[idx] += 1
            idx += idx & -idx

    def countSmallerThan(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res += self.sums[idx]
            idx -= idx & -idx
        return res


class BitSol:
    def rightSmallerThan(self, array: List[int]) -> List[int]:
        # Create a dictionary of all unique values in the input array as
        # keys pointing to their position if they were an ordered set
        # with the smallest at 0 and the biggest at len(n) - 1.
        dict = {value: idx for idx, value in enumerate(sorted(set(array)))}
        # Initialize the binary indexed tree, and the results array,
        # to all 0s
        bi_tree, res = BITree(len(dict)), [0] * len(array)
        # Start at the back of nums and iterate over every position.
        for i in range(len(array) - 1, -1, -1):
            # Update the result set with the current sum of frequencies
            # in the tree at that point. The tree contains, for each
            # value, the sum of elements smaller than the current one.
            res[i] = bi_tree.countSmallerThan(dict[array[i]])
            # Update the sums on the binary indexed tree. This is a
            # special use case in which we always increment by 1 and we
            # are using the dictionary to translate between values and
            # indexes. The result is that increasing the value at the
            # index pointed to by the dictionary, we increase the
            # numbers equal or less than this value that we have seen up
            # to that moment. Since we are iterating from the back, we
            # can use that information to check how many values less than
            # the current one we have seen and update the result array.
            bi_tree.update(dict[array[i]])
        return res


# TODO: Add BST solution.


def test():
    executors = [
        BitSol,
    ]
    tests = [
        [[], []],
        [[1], [0]],
        [[8, 5, 11, -1, 3, 4, 2], [5, 4, 4, 0, 1, 1, 0]],
        [
            [991, -731, -882, 100, 280, -43, 432, 771, -581, 180, -382, -998],
            [11, 2, 1, 4, 5, 3, 4, 4, 1, 2, 1, 0],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.rightSmallerThan(t[0])
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
