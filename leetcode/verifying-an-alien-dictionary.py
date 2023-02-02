# 953. Verifying an Alien Dictionary
# 🟢 Easy
#
# https://leetcode.com/problems/verifying-an-alien-dictionary/
#
# Tags: Array - Hash Table - String

import timeit
from typing import List


# Create a hashmap with the characters pointing to the ordinal value,
# then iterate over the words in the input using the hashmap to check
# the words one character at a time until we find a tie-breaker.
#
# Time complexity: O(m+n) - Where m is the number of characters in order
# and it is limited to 26, we iterate over them to create the o dict.
# n is the combined number of characters in words, we could iterate over
# all of them depending on the input. Equivalent to O(n) because m <= 26
# Space complexity: O(m) ~ O(1) - The dictionary takes m space with
# m <= 26.
#
# Runtime 43 ms Beats 50.46%
# Memory 13.7 MB Beats 99.16%
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Construct a hashmap to quickly check a characters order.
        o = {c: i for i, c in enumerate(order)}
        # Iterate over the words checking if they are in order.
        for idx in range(1, len(words)):
            word, prev = words[idx], words[idx - 1]
            # First check that characters in the same position match.
            for i in range(min(len(prev), len(word))):
                # If one character has an order less than, this words
                # are ordered correctly, move to the next pair.
                if o[prev[i]] < o[word[i]]:
                    break
                # If one character has an order higher than, this words
                # are not ordered correctly, we can return False.
                if o[prev[i]] > o[word[i]]:
                    return False
                # Characters were the same up to the end of their common
                # length, check that the word to the left is shorter.
            else:
                # Characters up to i match, check that .
                if len(prev) > len(word):
                    return False
        return True


def test():
    executors = [Solution]
    tests = [
        [["", "a"], "abcdefghijklmnopqrstuvwxyz", True],
        [["apap", "app"], "abcdefghijklmnopqrstuvwxyz", True],
        [["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False],
        [["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True],
        [["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False],
        [
            [
                "zirqhpfscx",
                "zrmvtxgelh",
                "vokopzrtc",
                "nugfyso",
                "rzdmvyf",
                "vhvqzkfqis",
                "dvbkppw",
                "ttfwryy",
                "dodpbbkp",
                "akycwwcdog",
            ],
            "khjzlicrmunogwbpqdetasyfvx",
            False,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isAlienSorted(t[0], t[1])
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
