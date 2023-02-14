# Non-Attacking Queens
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/non-attacking-queens
#
# Tags: Recursion

import timeit


# We know that we need to place a queen in each row, and each queen also
# needs to go in its own column and diagonals, if we try to place queens
# in rows by order, and keep three sets to determine in O(1) which
# columns and diagonals are free and which ones are under attack, we
# can quickly find paths that will not lead to a result and abandon
# them. To determine which paths we have explored already, and which
# ones we haven't we can use the row/column values and a backtracking
# function.
#
# Time complexity: O(n!) - Though in reality the number of operation
# will be much better than that.
# Space complexity: O(n) - We store 2*n elements in the diagonal sets
# and n elements in the columns set.
class Solution:
    def nonAttackingQueens(self, n: int) -> int:
        # Define a function that finds a suitable position to place a
        # queen in a given row.
        def placeQueen(row: int) -> int:
            # Base case, we have completed the board by placing one
            # queen in each row.
            if row == n:
                return 1
            # The number of valid placements starting from this state.
            valid = 0
            for col in range(n):
                # Check if placing a queen in this column is a valid
                # placement.
                if (
                    col in free_columns
                    and col - row in neg
                    and col + row in pos
                ):
                    # Place a queen in this position.
                    free_columns.remove(col)
                    neg.remove(col - row)
                    pos.remove(col + row)
                    valid += placeQueen(row + 1)
                    # Backtrack
                    pos.add(col + row)
                    neg.add(col - row)
                    free_columns.add(col)
            return valid

        # Create sets of free diagonals.
        # The positive diagonal goes from 0 to 2*n-2.
        pos = set([x for x in range(2 * n - 1)])
        # The negative diagonal goes from -n+ 1 to n-1.
        neg = set([x for x in range(-n + 1, n)])
        # The free columns.
        free_columns = set([x for x in range(n)])
        return placeQueen(0)


def test():
    executors = [Solution]
    tests = [
        [1, 1],
        [2, 0],
        [4, 2],
        [8, 92],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.nonAttackingQueens(t[0])
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
