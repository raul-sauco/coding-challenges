# 79. Word Search
# 🟠 Medium
#
# https://leetcode.com/problems/word-search/
#
# Tags: Array - Backtracking - Matrix

# 1 call
# » BacktrackTLE        0.66216   seconds
# » Backtrack           9e-05     seconds

import timeit
from collections import Counter
from itertools import chain
from typing import List, Set, Tuple


# We can use depth first search, traverse the graph looking for the
# first character in the search word. When we find it, we call a
# function that recursively starts checking its neighbors for the next
# characters of the word. If any of the sequences matches the input,
# we return true.
#
# Time complexity: O(4^(m*n)) - O(n) For the initial matrix traversal,
# then O(4^(m*n)) if all paths matched the input like in example 4.
# Space complexity: O(m*n) - The number of calls in the call stack is
# limited to the size of the matrix.
#
# This solution fails with Time Limit Exceeded even though the logic is
# similar to other solutions that pass. This could be due to the extra
# CPU time needed to hash set keys and create tuple objects.
class BacktrackTLE:
    def exist(self, board: List[List[str]], word: str) -> bool:
        NUM_ROWS, NUM_COLS = len(board), len(board[0])
        # Define a recursive function that explores the board, using DFS
        # from a starting point trying to match the input word.
        def matchesSuffix(pos: Tuple[int], used: Set[Tuple[int]]) -> bool:
            # Base case, we have constructed the word.
            if len(used) == len(word):
                return True
            dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
            # Explore the 4 available directions.
            for x, y in dirs:
                i, j = x + pos[0], y + pos[1]
                target = (i, j)
                if (
                    0 <= i < NUM_ROWS
                    and 0 <= j < NUM_COLS
                    and target not in used
                    and board[i][j] == word[len(used)]
                ):
                    used.add(target)
                    if matchesSuffix(target, used):
                        return True
                    # Backtrack
                    used.remove(target)

        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                if board[i][j] == word[0]:
                    # If we can construct the word from this position,
                    # return True immediately.
                    if matchesSuffix((i, j), {(i, j)}):
                        return True
        # If we could not construct the word from any position
        return False


# This solution uses the same logic as the previous one but, instead of
# using a set to check which characters we have visited, it updates the
# values on the board. Instead of passing tuples, it uses the row and
# column indices.
#
# Time complexity: O(4^(m*n)) - O(n) For the initial matrix traversal,
# then O(4^(m*n)) if all paths matched the input like in example 4.
# Space complexity: O(m*n) - The number of calls in the call stack is
# limited to the size of the matrix.
#
# Runtime: 3703 ms Beats 90.10%
# Memory: 14 MB Beats 50.84%
#
# We can improve runtime even better considering that the tests are
# designed to lead to high recursion when starting from one end or the
# other, if we check which end will lead to more recursion and start
# from the other, we can have a 20x performance gain.
#
# Runtime: 47 ms Beats 99.48%
# Memory: 14 MB Beats 50.84%
class Backtrack:
    def exist(self, board: List[List[str]], word: str) -> bool:
        NUM_ROWS, NUM_COLS = len(board), len(board[0])
        # Count character frequencies in the board and word.
        word_dict = Counter(word)
        board_dict = Counter(chain.from_iterable(board))
        # If we don't have enough characters in the board, we can return
        # false immediately.
        if any(count > board_dict[char] for char, count in word_dict.items()):
            return False
        # The LeetCode test cases seem designed to lead to very deep
        # recursion and high O complexity when starting from one end
        # or the other of the word, if we check which end will lead to
        # more recursion, and choose to start from the other, we can
        # optimize the code.
        if word_dict[word[0]] > word_dict[word[-1]]:
            word = word[::-1]
        # Define a recursive function that explores the board, using DFS
        # from a starting point trying to match the input word.
        def matchesSuffix(r: int, c: int, pos: int) -> bool:
            # Base case, we have constructed the word.
            if pos == len(word) - 1:
                return True
            dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
            # Explore the 4 available directions.
            for y, x in dirs:
                i, j = y + r, x + c
                if (
                    0 <= i < NUM_ROWS
                    and 0 <= j < NUM_COLS
                    and board[i][j] == word[pos + 1]
                ):
                    # Save the current value to backtrack.
                    tmp = board[i][j]
                    board[i][j] = "."
                    if matchesSuffix(i, j, pos + 1):
                        return True
                    # Backtrack
                    board[i][j] = tmp
            # If none of the directions returned a result.
            return False

        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if board[r][c] == word[0]:
                    # Save the current value to backtrack.
                    tmp = board[r][c]
                    board[r][c] = "."
                    # If we can construct the word from this position,
                    # return True immediately.
                    if matchesSuffix(r, c, 0):
                        return True
                    # Backtrack
                    board[r][c] = tmp
        # If we could not construct the word from any position
        return False


def test():
    executors = [
        BacktrackTLE,
        Backtrack,
    ]
    tests = [
        [
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCCED",
            True,
        ],
        [
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "SEE",
            True,
        ],
        [
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCB",
            False,
        ],
        [
            [
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "B"],
                ["A", "A", "A", "A", "B", "A"],
            ],
            "AAAAAAAAAAAAABB",
            False,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                # Some of the solutions mutate the matrix.
                matrix_copy = [row[:] for row in t[0]]
                result = sol.exist(matrix_copy, t[1])
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
