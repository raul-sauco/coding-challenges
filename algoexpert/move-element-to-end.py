# Move Element To End
# 🟠 Medium
#
# https://www.algoexpert.io/questions/move-element-to-end
#
# Tags: Array - Two Pointers

import timeit


# Use a read and an insert pointers, first make sure that the value
# under the insert pointer is not the target value, then check the read
# pointer and, if it holds the target value, swap them and slide both
# pointers.
#
# Time complexity: O(n) - We will visit each element once.
# Space complexity: O(1) - Constant extra memory.
class Solution:
    def moveElementToEnd(self, array, toMove):
        # Use two pointers, read and insert.
        read, insert = 0, len(array) - 1
        while read < insert:
            # If the value under the insert pointer is the
            # target, we don't want to insert there.
            if array[insert] == toMove:
                insert -= 1
                continue
            # Insert now points to a different value.
            # If read points to the target value, swap it with insert.
            if array[read] == toMove:
                array[read], array[insert] = array[insert], array[read]
                insert -= 1
            # Always slide the read pointer.
            read += 1
        return array


def test():
    executors = [Solution]
    tests = [
        [[], 8, []],
        [[3, 3, 3, 3, 3], 3, [3, 3, 3, 3, 3]],
        [[3, 1, 2, 4, 5], 3, [5, 1, 2, 4, 3]],
        [[2, 1, 2, 2, 2, 3, 4, 2], 2, [4, 1, 3, 2, 2, 2, 2, 2]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.moveElementToEnd(t[0], t[1])
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
