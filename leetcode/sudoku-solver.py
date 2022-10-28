# 37. Sudoku Solver
# 🔴 Hard
#
# https://leetcode.com/problems/sudoku-solver/
#
# Tags: Array - Backtracking - Matrix

import timeit
from collections import defaultdict
from typing import List, Union


# Keep a record of all cells that do not have a value yet and try to
# assign them a value, first we try to find cells that only have a
# unique value that can be assigned to them, if there are none, we take
# a guess and recursively invoke the solve function with the new board,
# if we ever arrive at a state where the board cannot be solved, we
# return false and the calling function will try the next guess.
#
# Time complexity: O(9^81) - On the worst case, we will need to try all
# possible guesses in each of the 81 positions. In theory this is O(1)
# but in reality is a pretty big number. Average complexity will be much
# better than that, in an easy board it will just make one call to place
# per each empty cell.
# Space complexity: O(81^3) - The call stack may end up being 81 levels
# deep, for each level we copy the matrix of 81 elements and we
# regenerate a series of data structures, like the rows, cols, boxes and
# cells dictionaries, the biggest of which is the cells dictionary that
# can grow to O(81*9) 81 entries of a max length 9.
#
# Runtime: 40 ms, faster than 99.87%
# Memory Usage: 14.3 MB, less than 5.72%
class Solution:
    def solve(self, board: List[List[str]]) -> Union[bool, List[List[str]]]:
        # Make the solver scalable.
        N = len(board)
        # Make a copy of the board.
        res = [["."] * N for _ in range(N)]
        # Store all possible values that a cell can take.
        cells = {
            (i, j): {str(k + 1) for k in range(N)}
            for i in range(N)
            for j in range(N)
        }
        # Map cells to the boxes they belong to.
        boxes = defaultdict(list)
        for i in range(N):
            for j in range(N):
                boxes[(i // 3, j // 3)].append((i, j))

        def canPlace(row: int, col: int, val: int) -> bool:
            # Remove the value from all the cells in the row.
            for j in range(N):
                if res[row][j] == val:
                    return False
            # Remove the value from all the cells in the col.
            for i in range(N):
                if res[i][col] == val:
                    return False
            # Remove the value from all the cells in the box.
            box = boxes[(row // 3, col // 3)]
            for cell in box:
                if res[cell[0]][cell[1]] == val:
                    return False
            return True

        # Define a function that fills a cell with a value.
        def place(row: int, col: int, val: int) -> bool:
            # Remove the value from all the cells in the row.
            for j in range(N):
                if (row, j) in cells:
                    cells[(row, j)].discard(val)
            # Remove the value from all the cells in the col.
            for i in range(N):
                if (i, col) in cells:
                    cells[(i, col)].discard(val)
            # Remove the value from all the cells in the box.
            box = boxes[(row // 3, col // 3)]
            for cell in box:
                if cell in cells:
                    cells[cell].discard(val)
            # Pop the key from the cells dictionary.
            del cells[(row, col)]
            # Place the value on the result matrix.
            res[row][col] = val

        # Define a function that removes a value from a cell.
        # This function undoes the changes that place with the same
        # parameters would have made.
        def remove(row: int, col: int, val: int) -> None:
            # Remove the value from the board.
            res[row][col] = "."
            # Add the cell to the dictionary if not there.
            if (row, col) not in cells:
                cells[(row, col)] = set()
            # Add the value to all the existing cells in the box.
            for cell in boxes[(row // 3, col // 3)]:
                if cell in cells:
                    cells[cell].add(val)
            # Add the value to all the cells in the col.
            for i in range(N):
                if (i, col) in cells:
                    cells[(i, col)].add(val)
            # Add the value to all the cells in the row.
            for j in range(N):
                if (row, j) in cells:
                    cells[(row, j)].add(val)

        # Mark the values we have.
        for row in range(len(board)):
            for col, val in enumerate(board[row]):
                # If the cell already has a number.
                if val != ".":
                    place(row, col, val)

        # Try to place the next value.
        while cells:
            # If we have a cell that hasn't been filled yet but has run
            # out of options, we have gone down a wrong path, backtrack.
            cant_solve = [pos for pos in cells.keys() if not cells[pos]]
            if cant_solve:
                return False
            # If we can place any value unequivocally, place it.
            single_options = [
                pos for pos in cells.keys() if len(cells[pos]) == 1
            ]
            if single_options:
                cell = single_options.pop()
                val = cells[cell].pop()
                if not canPlace(cell[0], cell[1], val):
                    return False
                place(cell[0], cell[1], val)
                continue
            # Start taking guesses, pick one of the cells that have less
            # possible digits.
            for i in range(2, 10):
                c = [pos for pos in cells.keys() if len(cells[pos]) == i]
                # If there is any cell with this number of options.
                if c:
                    cell = c.pop()
                    guesses = set(cells[cell])
                    for guess in guesses:
                        # Try this guess.
                        place(cell[0], cell[1], guess)
                        # Try to solve this version of the board.
                        sol = self.solve(res)
                        # If sol is not False, we have a solution.
                        if sol:
                            return sol
                        # Else, backtrack.
                        remove(cell[0], cell[1], guess)
                    # If one of the guesses did not work, the
                    # current state will not lead to a solution, in a
                    # valid board, one of the guesses should always
                    # be one of the valid results and we will never
                    # arrive at this line.
                    return False

        return res

    # Define a function that calls the helper solve function and copies
    # the result matrix into the input as requested by the LeetCode
    # testing platform.
    def solveSudoku(
        self, board: List[List[str]]
    ) -> Union[bool, List[List[str]]]:
        res = self.solve(board)
        # Copy the result into the input board for LeetCode testing.
        # for row in range(len(board)):
        #     board[row] = res[row][:]
        # For local testing, return the result.
        return res


def test():
    executors = [Solution]
    tests = [
        [
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            [
                ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
            ],
        ],
        [
            [
                ["9", "8", ".", "7", ".", ".", "6", ".", "."],
                ["7", ".", ".", "5", ".", ".", "9", "4", "."],
                [".", ".", ".", ".", "6", ".", ".", ".", "."],
                ["4", "7", ".", ".", ".", "3", ".", ".", "."],
                [".", "2", ".", ".", ".", "5", ".", ".", "."],
                [".", ".", "9", "6", ".", ".", "4", ".", "."],
                ["2", ".", ".", ".", "5", ".", ".", "1", "."],
                [".", "9", ".", "8", ".", ".", "2", ".", "."],
                [".", ".", "8", ".", ".", ".", ".", ".", "6"],
            ],
            [
                ["9", "8", "4", "7", "3", "1", "6", "2", "5"],
                ["7", "1", "6", "5", "2", "8", "9", "4", "3"],
                ["5", "3", "2", "4", "6", "9", "1", "8", "7"],
                ["4", "7", "1", "9", "8", "3", "5", "6", "2"],
                ["6", "2", "3", "1", "4", "5", "7", "9", "8"],
                ["8", "5", "9", "6", "7", "2", "4", "3", "1"],
                ["2", "6", "7", "3", "5", "4", "8", "1", "9"],
                ["3", "9", "5", "8", "1", "6", "2", "7", "4"],
                ["1", "4", "8", "2", "9", "7", "3", "5", "6"],
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.solveSudoku(t[0])
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
