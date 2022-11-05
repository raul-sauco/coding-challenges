# 211. Design Add and Search Words Data Structure
# 🟠 Medium
#
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
#
# Tags: String - Depth-First Search - Design - Trie


import timeit
from collections import defaultdict


# Implement the word dictionary using plain hash maps to store the
# children of each node. Inserting is exactly the same as with the
# regular trie class and can be done in O(n), searching will need to
# branch out to all the nodes' children when the current character is a
# '.' wildcard and it could potentially take O(m*n) which is visiting
# each node in the trie, even though usually would be faster.
#
# Time complexity: O(m*n) - For searching strings with wildcards, it
# could potentially search the entire trie. O(n) for inserts, it will
# perform one O(1) operation per character.
# Space complexity: O(m*n) - Potentially, each character of each node
# inserted could make its own node, in average it will be less than that
# because words with common roots will share nodes.
#
# Runtime: 16919 ms, faster than 27.72%
# Memory Usage: 55.9 MB, less than 87.04%
class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        current = self.root
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        current["?"] = True

    def search(self, word: str) -> bool:
        def searchFromNode(index, node) -> bool:
            current = node
            for i in range(index, len(word)):
                w = word[i]
                # Handle wildcards
                if w == ".":
                    # Recursive call to all the children with the sliced word
                    for key, child in current.items():
                        if key != "?" and searchFromNode(i + 1, child):
                            return True
                    return False
                else:
                    if w not in current:
                        return False
                    current = current[w]
            return current.get("?", False)

        return searchFromNode(0, self.root)


# Definition for a trie node
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


# Easier to read version of the word dictionary that uses TriedNode as a
# node instead of a plain dictionary.
#
# Time complexity: O(m*n) - For searching strings with wildcards, it
# could potentially search the entire trie. O(n) for inserts, it will
# perform one O(1) operation per character.
# Space complexity: O(m*n) - Potentially, each character of each node
# inserted could make its own node, in average it will be less than that
# because words with common roots will share nodes.
#
# Runtime: 16930 ms, faster than 27.61%
# Memory Usage: 80 MB, less than 12.93%
class WDEasyRead:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        # Recursively add the nodes.
        for w in word:
            current = current.children[w]
        # Mark the last character of the word as the end of a word.
        current.isWord = True

    def search(self, word: str) -> bool:
        def dfs(node, word) -> bool:
            # If our query string is longer than this branch of the
            # exploration, return False.
            if node:
                # If we have exhausted the characters in the search
                # word, exit.
                # Return True if we are at a word, False otherwise.
                # False returns will be ignored by the caller.
                if len(word) == 0:
                    if node.isWord:
                        return True

                # If we have not exhausted all the characters.
                else:
                    # We still have characters to explore in word.
                    if word[0] == ".":
                        for n in node.children.values():
                            if dfs(n, word[1:]):
                                return True
                    else:
                        node = node.children.get(word[0])
                        if node and dfs(node, word[1:]):
                            return True

        res = dfs(self.root, word)  # True or None
        return res if res else False


def test():
    executors = [
        WordDictionary,
        WDEasyRead,
    ]
    tests = [
        [
            [
                "WordDictionary",
                "addWord",
                "addWord",
                "addWord",
                "search",
                "search",
                "search",
                "search",
            ],
            [
                [],
                ["bad"],
                ["dad"],
                ["mad"],
                ["pad"],
                ["bad"],
                [".ad"],
                ["b.."],
            ],
            [None, None, None, None, False, True, True, True],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                # The constructor does not take any parameters.
                sol = executor()
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    # All the methods take exactly one parameter.
                    result = getattr(sol, call)(t[1][i][0])
                    exp = t[2][i]
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
