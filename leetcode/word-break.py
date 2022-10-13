# 139. Word Break
# 🟠 Medium
#
# https://leetcode.com/problems/word-break/
#
# Tags: Hash Table - String - Dynamic Programming - Trie - Memoization

import timeit
from heapq import heappop, heappush
from typing import List

# 1 call
# » GreedyTrie          0.00092   seconds
# » DP                  0.00116   seconds

# Trie implementation.
class Trie:
    def __init__(self, wordList: List[int] = None):
        self.size = 0
        self.root = {}
        for word in wordList:
            self.insert(word)

    def __repr__(self):
        return f"Trie({self.size})"

    def insert(self, word: str) -> None:
        self.size += 1
        current = self.root
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        current["?"] = True

    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            if w not in current:
                return False
            current = current[w]
        return current.get("?", False)

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for w in prefix:
            if w not in current:
                return False
            current = current[w]
        return True


# Use a trie as a dictionary, and a max heap to keep positions where
# we know that we could start the next word. Start from the next
# position in the heap checking which words from the dictionary match
# starting from there, record the starting positions right after the
# index of matching words in the heap.
#
# Time complexity: O(n^3) - The worst case would be where for each
# position, we can almost build to the end but then fail and have to
# start again from the next position.
#
# Runtime: 54 ms, faster than 75.12%
# Memory Usage: 15.1 MB, less than 5.85%
class GreedyTrie:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create the trie and insert words into it.
        trie = Trie(wordDict)
        # Keep the next position that we want to explore in a heap.
        # At the start, we only want to explore position 0.
        heap = [0]
        # Keep a mask of positions that we have explored.
        mask = 1 << len(s) | 1
        # Iterate over the positions in s marking the end of strings.
        while heap:
            # Use a max heap to greedily explore the positions with
            # higher indexes first.
            i = -heappop(heap)
            for j in range(i, len(s)):
                w = s[i : j + 1]
                if trie.search(w):
                    # If s[i:j] is a word in the dictionary, try to
                    # find words starting at i or return true if we
                    # have gone over the whole input.
                    if j == len(s) - 1:
                        return True
                    # Avoid recomputing from positions that we have
                    # seen already.
                    if not 1 << j + 1 & mask:
                        mask |= 1 << (j + 1)
                        heappush(heap, -(j + 1))
                # If the current word is not a prefix in the trie,
                # adding new characters won't help.
                elif not trie.startsWith(w):
                    break
        return False


# A very elegant solution, without the need for a trie structure, uses
# bottom-up dynamic programming. We start at the first index 0 from
# there, start checking all indexes to see if there is any word that can
# be formed these two indexes, if there is, we mark it as reachable and
# move to the next index i.
#
# Time complexity: O(n^3) - For each position, we check every previous
# index and, for each, slice the string j:i at O(n).
# Space complexity: O(n) - The lookup set, and the dp array all grow in
# size linearly with the input size.
#
# Runtime: 87 ms, faster than 22.71%
# Memory Usage: 13.8 MB, less than 99.64%
class DP:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lookup = set(wordDict)
        dp = [True] + ([False] * len(s))
        for i in range(1, len(s) + 1):
            # dp[i] = any(dp[j] and s[j:i] in word_set for j in range(i))
            for j in range(i):
                # If we could construct the word up to j-1 and we find
                # the word j-1:i in the lookup, we can construct up to
                # here as well.
                if dp[j] and s[j:i] in lookup:
                    dp[i] = True
                    break
        return dp[-1]


def test():
    executors = [
        GreedyTrie,
        DP,
    ]
    tests = [
        ["h", ["a", "b"], False],
        ["h", ["a", "b", "h"], True],
        ["leetcode", ["leet", "code"], True],
        ["applepenapple", ["apple", "pen"], True],
        ["catsandog", ["cats", "dog", "sand", "and", "cat"], False],
        [
            "acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb",
            [
                "abbcbda",
                "cbdaaa",
                "b",
                "dadaaad",
                "dccbbbc",
                "dccadd",
                "ccbdbc",
                "bbca",
                "bacbcdd",
                "a",
                "bacb",
                "cbc",
                "adc",
                "c",
                "cbdbcad",
                "cdbab",
                "db",
                "abbcdbd",
                "bcb",
                "bbdab",
                "aa",
                "bcadb",
                "bacbcb",
                "ca",
                "dbdabdb",
                "ccd",
                "acbb",
                "bdc",
                "acbccd",
                "d",
                "cccdcda",
                "dcbd",
                "cbccacd",
                "ac",
                "cca",
                "aaddc",
                "dccac",
                "ccdc",
                "bbbbcda",
                "ba",
                "adbcadb",
                "dca",
                "abd",
                "bdbb",
                "ddadbad",
                "badb",
                "ab",
                "aaaaa",
                "acba",
                "abbb",
            ],
            True,
        ],
        [
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
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
            False,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.wordBreak(t[0], t[1])
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
