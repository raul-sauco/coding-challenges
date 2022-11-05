# 208. Implement Trie (Prefix Tree)
# 🟠 Medium
#
# https://leetcode.com/problems/implement-trie-prefix-tree/
#
# Tags: Hash Table - String - Design - Trie

import timeit
from collections import defaultdict

# 10e4 calls.
# » Trie                0.00228   seconds
# » UseTrieNode         0.00384   seconds

# Create a class that directly implements all the required methods, the
# class internally uses dictionaries to store and find each node
# children, including the root.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input word. All methods have the same complexity, for each character
# in the input, we do a dictionary access in O(1).
# Space complexity: O(m*n) - Where m is the number of words and n the
# average number of characters per word, each character could take space
# in the trie, even though often that will not be the case because
# characters shared between words will only take space once.
#
# Runtime: 144 ms, faster than 96.10%
# Memory Usage: 27.5 MB, less than 92.13%
class Trie:
    def __init__(self):
        self.root = {}

    # O(n) - Where n is the number of characters.
    def insert(self, word: str) -> None:
        current = self.root
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        current["?"] = True

    # O(n) - Where n is the number of characters.
    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            if w not in current:
                return False
            current = current[w]
        return current.get("?", False)

    # O(n) - Where n is the number of characters.
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for w in prefix:
            if w not in current:
                return False
            current = current[w]
        return True


# Definition for a trie node
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


# Create a class that uses TrieNode to provide the functionality
# required, the Trie class has a root TrieNode. The usage is similar to
# the dictionary implementation but it results in more readable and
# maintainable code.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input word. All methods have the same complexity, for each character
# in the input, we do a dictionary access in O(1).
# Space complexity: O(m*n) - Where m is the number of words and n the
# average number of characters per word, each character could take space
# in the trie, even though often that will not be the case because
# characters shared between words will only take space once.
#
# Runtime: 446 ms, faster than 28.62%
# Memory Usage: 31.9 MB, less than 23.72%
class UseTrieNode:
    def __init__(self):
        self.root = TrieNode()

    # O(n) - Where n is the number of characters.
    def insert(self, word: str) -> None:
        current = self.root
        for w in word:
            # Default dict will create the entry if not found.
            current = current.children[w]
        current.isWord = True

    # O(n) - Where n is the number of characters.
    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            if w not in current.children:
                return False
            current = current.children[w]
        return current.isWord

    # O(n) - Where n is the number of characters.
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for w in prefix:
            if w not in current.children:
                return False
            current = current.children[w]
        return True


def test():
    executors = [
        Trie,
        UseTrieNode,
    ]
    tests = [
        [
            [
                "Trie",
                "insert",
                "search",
                "search",
                "startsWith",
                "insert",
                "search",
            ],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True],
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
