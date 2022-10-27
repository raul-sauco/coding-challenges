# 127. Word Ladder
# 🔴 Hard
#
# https://leetcode.com/problems/word-ladder/
#
# Tags: Hash Table - String - Breath-First Search

import timeit
from collections import defaultdict, deque
from typing import List

# 1 call with 5000 word dictionary and 20 steps between start and end.
# » Naive               2.08446   seconds
# » Matches             0.02905   seconds

# Naively we can perform breath first search using begin word as the
# start and traveling one level at a time until we find the end word or
# arrive at a level with no words. A level consists on all words that
# we have not visited before and are 1 character away from any word in
# the previous level.
#
# Time complexity: O(n^2) - Where n is the number of words in the word
# dictionary, we need to check each word against all others to find
# its neighbors.
# Space complexity: O(n) - The available set starts at size n.
#
# This solution fails with Time Limit Exceeded.
class Naive:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        # Construct a set of the words that are available.
        available = set(wordList)
        # Store the words that we can arrive to in a queue.
        q = deque([beginWord])
        # Store the number of transformations.
        level = 0
        # Define a function that returns whether two words are connected.
        # For our purpose, being connected means that the words differ
        # only in one position.
        def areConnected(a: str, b: str) -> bool:
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        while q:
            # Increase the level count.
            level += 1
            # Process the next level.
            for _ in range(len(q)):
                current = q.popleft()
                # Check if we have our target word.
                if current == endWord:
                    return level
                # Enqueue this node's neighbors.
                for word in set(available):
                    if areConnected(current, word):
                        available.remove(word)
                        q.append(word)
        # If we exhaust the queue we cannot build the target.
        return 0


# Preprocess the words to obtain a dictionary of word variations, in
# which each variation has a character substituted by a wildcard, to
# the words that could generate these variations. Then use the same
# logic as in the previous solution but, instead of iterating over all
# the words trying to find the ones that are one character away from the
# current one, use its possible variations to obtain its neighbors in
# O(1), max 10 variations O(1) access to the list of words that could
# produce these variations.
#
# Time complexity: O(n) - We could still visit all the words in the
# dictionary, but this time we only do O(1) work for each.
# Space complexity: O(n) - The dictionary can grow to length(beginWord)
# times length(wordList) in which len(beginWord) is max 10.
#
# Runtime: 231 ms, faster than 80.18%
# Memory Usage: 17.5 MB, less than 48.28%
class Matches:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        # Define a function that produces all variations of a word
        # replacing one of its characters with a wildcard.
        def getVariants(word: str) -> List[str]:
            w = "."
            res = []
            for i in range(len(word)):
                chars = []
                for j in range(len(word)):
                    chars.append(word[j] if i != j else w)
                res.append("".join(chars))
            return res

        # Define a helper function that returns a list of that word's
        # neighbors.
        def getNeighbors(word: str) -> List[str]:
            neighbors = []
            for variant in getVariants(word):
                for neighbor in d[variant]:
                    if neighbor not in seen:
                        neighbors.append(neighbor)
            return neighbors

        # Construct a dictionary of variations: words.
        d = defaultdict(list)
        contains_end_word = False
        for word in wordList + [beginWord]:
            if word == endWord:
                contains_end_word = True
            for variant in getVariants(word):
                d[variant].append(word)
        if not contains_end_word:
            return 0
        # Store words we have already visited.
        seen = set([beginWord])
        # Store the words that we can arrive to in a queue.
        q = deque([beginWord])
        # Store the number of transformations.
        level = 0
        while q:
            # Increase the level count.
            level += 1
            # Process the next level.
            for _ in range(len(q)):
                current = q.popleft()
                # Check if we have our target word.
                if current == endWord:
                    return level
                # Enqueue this node's neighbors if we haven't seen them
                # before.
                neighbors = getNeighbors(current)
                while neighbors:
                    # Get neighbors checks that neighbors have not been
                    # seen before.
                    neighbor = neighbors.pop()
                    seen.add(neighbor)
                    q.append(neighbor)
        # If we exhaust the queue we cannot build the target.
        return 0


def test():
    executors = [
        Naive,
        Matches,
    ]
    tests = [
        ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5],
        ["hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.ladderLength(t[0], t[1], t[2])
                exp = t[3]
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
