# https://leetcode.com/problems/n-queens-ii/

from helpers import BColors


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0         # Store the number of matches
        cols = set()    # Store the columns that have a queen
        d_pos = set()   # Positive diagonals that have a queen row+col
        d_neg = set()   # Negative diagonals that have a queen row-col

        def s(row):
            # If we are past the last (zero indexed) row, we have a solution
            if row == n:
                self.res += 1
                return

            # For each column
            for col in range(n):
                # Check if we can place the queen
                if col in cols or row+col in d_pos or row-col in d_neg:
                    # If the column or one of the diagonals is taken, skip the placement
                    continue

                # The placement is valid, "place" a queen in the current row/col
                cols.add(col)
                d_pos.add(row+col)
                d_neg.add(row-col)

                # Recursive call, used positions have been updated
                s(row+1)

                # Backtrack (Restore data structures for next iteration of the loop)
                cols.remove(col)
                d_pos.remove(row+col)
                d_neg.remove(row-col)

        # Call the recursive function
        s(0)

        return self.res
        # return [1, 0, 0, 2, 10, 4, 40, 92, 352][n-1]


solutions = {
    1: 1,
    2: 0,
    3: 0,
    4: 2,
    5: 10,
    6: 4,
    7: 40,
    8: 92,
    9: 352,
}


def test():
    sol = Solution()
    for n in range(1, 10):
        assert sol.totalNQueens(
            n) == solutions[n], f'\n{BColors.bold}{BColors.fail}» Expected {solutions[n]} not equal to {sol.totalNQueens(n)} for n: {n}{BColors.end_dc}'


# for _ in range(1000):
test()

print(
    f'\n{BColors.bold}{BColors.ok_green}» All tests passed!{BColors.end_dc}\n')
