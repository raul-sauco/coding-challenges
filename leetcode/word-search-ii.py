# 212. Word Search II
# 🔴 Hard
#
# https://leetcode.com/problems/word-search-ii/
#
# Tags: Array - String - Backtracking - Trie - Matrix

import timeit
from typing import List

# 1 call with several tests including LeetCode's 62
# » TrieSolution        0.97636   seconds
# » OptimizedTrieSol    0.00227   seconds

# A fast trie implementation, not as readable as using TrieNodes but
# more performant.
class Trie:
    def __init__(self, words: List[str] = None):
        self.root = {"length": 0}
        for word in words:
            self.insert(word)

    def __len__(self) -> int:
        return self.root["length"]

    # Insert a word into this trie object.
    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {"length": 0}
            # There is more complete word under this node.
            current["length"] += 1
            current = current[c]
        current["length"] += 1
        current["?"] = True

    # Remove a word from this trie object.
    def remove(self, word: str) -> None:
        current = self.root
        current["length"] -= 1
        for i, c in enumerate(word):
            if c in current:
                current[c]["length"] -= 1
                if current[c]["length"] < 1:
                    current.pop(c)
                    break
                else:
                    current = current[c]
        # If we get to the word leaf but the trie node has children.
        if i == len(word) - 1 and "?" in current:
            current.pop("?")

    # Check if a given list of chars is in the trie, it returns 0 if
    # not found, 1 if found but not a full word and 2 if a full word.
    def contains(self, word: List[str]) -> int:
        current = self.root
        for c in word:
            if c not in current:
                return 0
            current = current[c]
        return 2 if "?" in current else 1


# Use a trie to do quick lookups of the words, since the words are max
# 10 characters long, looking up a word in the trie can be done in O(1).
# Iterate over all the positions in the matrix doing DFS starting at
# that position and moving to its neighbors while the words that we are
# constructing are prefixes found in the trie. When we find a word, add
# it to the result set. Using the trie to do prefix and word lookups
# should be all that is expected in an interview but adding the word
# removal is an optimization that could be discussed.
#
# Time complexity: O(m*n*(4*3^10)) - We iterate over all the positions
# on the board, for each, we start a search for any words that can be
# constructed from this position, the search will initially move to the
# four neighbors, then from there, as long as the characters added are
# found in the trie, the search will expand to the three neighbors of
# the new cell, since the cell we just came from cannot be visited again.
# So, from each position in the matrix, we will potentially do 4*3^10
# calls to DFS, since the max depth is equal to the length of the
# longest word in the trie and that is a max of 10. In theory that is
# still O(1) but it seems significant enough that is worth mentioning it
# on the time complexity.
# Space complexity: O(w*c) - The number of characters in all the words
# in the input, we store them all in the trie, and potentially also in
# the result set even though we would not consider that because it is
# used as the output. The call stack will have a max height of 10.
#
# On LeetCode, the obvious trie and DFS solution needs to be optimized
# to pass the tests and not give TLE, removing the words from the trie
# after finding them in the board is enough as of november 2022.
#
# Runtime: 6123 ms, faster than 20.52%
# Memory Usage: 16.3 MB, less than 58.84%
class TrieSolution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        NUM_ROWS, NUM_COLS = len(board), len(board[0])
        # Store the words found.
        res = set()
        # Initialize a Trie with the words in the input.
        trie = Trie(words)
        # Define a function that explores the board from a given start
        # position.
        def dfs(row: int, col: int, current: List[str]) -> None:
            current.append(board[row][col])
            board[row][col] = "."
            found = trie.contains(current)
            # If the current branch is not in the trie, not point on
            # exploring any further.
            if not found:
                board[row][col] = current.pop()
                return
            # If this is an exact match, add it to the result set.
            if found == 2:
                w = "".join(current)
                res.add(w)
                trie.remove(w)
            # The four directions where neighbors are found.
            dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for di, dj in dirs:
                i, j = row + di, col + dj
                if (
                    0 <= i < NUM_ROWS
                    and 0 <= j < NUM_COLS
                    and board[i][j] != "."
                ):
                    dfs(i, j, current)
            # Backtrack.
            board[row][col] = current.pop()

        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                dfs(i, j, [])
                # If at any point we find all the words,
                # return now.
                if len(res) == len(words):
                    return res
        return res


# There are a couple of optimizations that we can do once we see the
# particular tests that LeetCode is using. The tests lead to high
# recursion by having boards with high frequencies of one character and
# words with multiple instances of that character at the beginning, for
# example a board with almost all "a" and a high number of words like
# "aaaaaaaaab". Once we know that, we can improve the solution to
# perform better in the tests with a couple of optimizations. The first
# is by creating a lookup set of all the two character combinations
# found in the board and discarding any words that have a two character
# sequence not in the lookup.
# The second is by reversing all words in which we detect a high
# frequency of one character at the beginning. I think that this
# optimizations are very specific for this particular tests and not
# general enough to be very useful in a real world or interview set up,
# but it was an interesting case of optimization.
#
# Time and space complexity are the same as the previous solution even
# though the runtime is hundreds of times faster.
#
# Runtime: 53 ms, faster than 99.89%
# Memory Usage: 14.5 MB, less than 97.86%
class OptimizedTrieSol:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        NUM_ROWS, NUM_COLS = len(board), len(board[0])
        # Remove words for which one of their two letter combinations
        # cannot be found in the board.
        seq_two = set()
        candidates = []
        reversed_words = set()
        # Find all sequences of two characters in the board. Only right
        # and down.
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS - 1):
                seq_two.add(board[i][j] + board[i][j + 1])
        for j in range(NUM_COLS):
            for i in range(NUM_ROWS - 1):
                seq_two.add(board[i][j] + board[i + 1][j])
        # Iterate over the words checking if they could be in the board.
        for word in words:
            in_board = True
            for i in range(len(word) - 1):
                # For each sequence of two characters in the word, check
                # if that sequence or its inverse are in the board.
                if (
                    word[i : i + 2] not in seq_two
                    and word[i + 1] + word[i] not in seq_two
                ):
                    in_board = False
                    break
            if not in_board:
                continue
            # Reverse words with the same character in the first
            # four positions.
            if word[:4] == word[0] * 4:
                word = word[::-1]
                reversed_words.add(word)
            candidates.append(word)

        NUM_ROWS, NUM_COLS = len(board), len(board[0])
        # Store the words found.
        res = set()
        # Initialize a Trie with the words in the input that could be in
        # the board potentially, the candidates, some of them may have
        # been reversed to make finding them more efficient.
        trie = Trie(candidates)
        # Define a function that explores the board from a given start
        # position.
        def dfs(row: int, col: int, current: List[str]) -> None:
            current.append(board[row][col])
            board[row][col] = "."
            found = trie.contains(current)
            # If the current branch is not in the trie, not point on
            # exploring any further.
            if not found:
                board[row][col] = current.pop()
                return
            # If this is an exact match, add it to the result set.
            if found == 2:
                w = "".join(current)
                if w in reversed_words:
                    res.add(w[::-1])
                    reversed_words.remove(w)
                else:
                    res.add(w)
                trie.remove(w)
            # The four directions where neighbors are found.
            dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for di, dj in dirs:
                i, j = row + di, col + dj
                if (
                    0 <= i < NUM_ROWS
                    and 0 <= j < NUM_COLS
                    and board[i][j] != "."
                ):
                    dfs(i, j, current)
            # Backtrack.
            board[row][col] = current.pop()

        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                dfs(i, j, [])
        return res


def test():
    executors = [
        TrieSolution,
        OptimizedTrieSol,
    ]
    tests = [
        [[["a"]], ["a"], ["a"]],
        [[["a", "a"]], ["aaa"], []],
        [[["a", "b"], ["c", "d"]], ["abcb"], []],
        [
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain", "hklf", "hf"],
            ["oath", "eat", "hklf", "hf"],
        ],
        [
            [
                ["c", "a", "t", "i"],
                ["i", "a", "n", "o"],
                ["l", "p", "p", "a"],
            ],
            ["app", "application"],
            ["app", "application"],
        ],
        [
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            ["eat", "oath"],
        ],
        [
            [
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ],
            [
                "a",
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
            ],
            [
                "a",
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findWords(t[0], t[1])
                exp = set(t[2])
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
