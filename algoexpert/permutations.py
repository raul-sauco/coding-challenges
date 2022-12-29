# Permutations
# 🟠 Medium
#
# https://www.algoexpert.io/questions/permutations
#
# Tags: Recursion - Array

import timeit
from typing import List


# Use a recursive backtracking function that adds all of the available
# digits as the next element of a permutation one at a time.
#
# Time complexity: O(n!)
# Space complexity: O(n)
class FlagArray:
    def getPermutations(self, array: List[int]) -> List[List[int]]:
        if not array:
            return []
        # An array of flags of which digits have been used.
        used = [False] * len(array)
        # The result array.
        res = []
        # An array to store the current permutation being built.
        current = []
        # A backtrack function that iterates over all the digits in the
        # input adding them to the current set before calling itself.
        def backtrack():
            # Base case, we have a complete permutation.
            if len(current) == len(array):
                res.append(current[:])
            else:
                for i in range(len(array)):
                    if not used[i]:
                        current.append(array[i])
                        used[i] = True
                        backtrack()
                        used[i] = False
                        current.pop()

        backtrack()
        return res


# Similar to the previous solution but, if allowed to mutate the input
# array, we can use it to flag which elements we have used already.
#
# Time complexity: O(n!)
# Space complexity: O(n)
class InputArrayAsFlags:
    def getPermutations(self, array: List[int]) -> List[List[int]]:
        if not array:
            return []
        # The result array.
        res = []
        # An array to store the current permutation being built.
        current = []
        # A backtrack function that iterates over all the digits in the
        # input adding them to the current set before calling itself.
        def backtrack():
            # Base case, we have a complete permutation.
            if len(current) == len(array):
                res.append(current[:])
            else:
                for i in range(len(array)):
                    if not array[i] is None:
                        current.append(array[i])
                        array[i] = None
                        backtrack()
                        array[i] = current.pop()

        backtrack()
        return res


def test():
    executors = [
        FlagArray,
        InputArrayAsFlags,
    ]
    tests = [
        [
            [1, 2, 3],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.getPermutations(t[0])
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
