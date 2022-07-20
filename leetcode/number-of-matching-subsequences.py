# https://leetcode.com/problems/number-of-matching-subsequences/

# Tags: Hash Table - String - Trie - Sorting

import timeit
from collections import defaultdict
from functools import lru_cache
from typing import List


# Create a dictionary of subsequences to check indexed by their first character. Iterate over the characters in s
# checking for matches in the dictionary in O(1), for all subsequences that start with the given character,
# when 1 character long, count them as a match, otherwise remove the first character and reinsert them into the
# dictionary.
#
# Time complexity: O(n*m) n is the length of s and m the length of the longest word.
# Space complexity: O(m) we keep a dictionary with all the subsequences in memory.
#
# Runtime: 1041 ms, faster than 34.28% of Python3 online submissions for Number of Matching Subsequences.
# Memory Usage: 15.7 MB, less than 36.92% of Python3 online submissions for Number of Matching Subsequences.
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Create a dictionary to fetch sequences by their first character in O(1) then insert all words
        wd = defaultdict(list)
        for w in words:
            wd[w[0]].append(w)

        count = 0
        # Iterate over all characters in s and shorten the sequences where the first character matches the current c
        for c in s:
            # Fetch the items that match the current character and remove the key from the dictionary
            matches = wd[c]
            del wd[c]

            for match in matches:
                if len(match) == 1:
                    count += 1
                else:
                    remaining = match[1:]
                    wd[remaining[0]].append(remaining)

        return count


# Since the maximum size of both inputs, s and words, it is the same at 5 * 10^4, we can iterate over the
# words and, for each word and each character, use the find() function to check if we can find it on the
# input string. If found, try to find the next character in word starting at the index of string where we
# found the previous character.
#
# Time complexity: O(m*n) - where m is the number of individual characters in words and n is the size of s.
# The average complexity will be better because the algorithm returns quickly when the subsequences are not in s.
# Space complexity: O(log(n)) - The sum function will store one boolean value for each input word.
#
# Runtime: 355 ms, faster than 97.03% of Python3 online submissions for Number of Matching Subsequences.
# Memory Usage: 15.4 MB, less than 98.31% of Python3 online submissions for Number of Matching Subsequences.
class BuiltInFn:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def checkWord(word: str):
            start = 0
            for ch in word:
                start = s.find(ch, start) + 1
                if not start:
                    return False
            return True

        return sum(checkWord(w) for w in words)


def test():
    executors = [Solution, BuiltInFn]
    tests = [
        [
            "rwpddkvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvjubjgloeofnpjqlkdsqvruvabjrikfwronbrdyyjnakstqjac",
            [
                "wpddkvbnn",
                "lnagtva",
                "kvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvju",
                "rwpddkvbnnugln",
                "gloeofnpjqlkdsqvruvabjrikfwronbrdyyj",
                "vbgeinupkvgmgxeaaiuiyojmoqkahwvbpwugdainxciedbdkos",
                "mspuhbykmmumtveoighlcgpcapzczomshiblnvhjzqjlfkpina",
                "rgmliajkiknongrofpugfgajedxicdhxinzjakwnifvxwlokip",
                "fhepktaipapyrbylskxddypwmuuxyoivcewzrdwwlrlhqwzikq",
                "qatithxifaaiwyszlkgoljzkkweqkjjzvymedvclfxwcezqebx",
            ],
            5,
        ],
        ["abcde", ["a", "bb", "acd", "ace"], 3],
        ["dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"], 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1e4"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numMatchingSubseq(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
