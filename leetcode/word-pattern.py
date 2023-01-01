# 290. Word Pattern
# 🟢 Easy
#
# https://leetcode.com/problems/word-pattern/
#
# Tags: Hash Table - String

import timeit


# We need to make sure that there is a direct correlation between
# characters in the pattern and words in s, we can use a dictionary
# mapping them, when we see a new character, we check that its matching
# word has not been seen and add it to both the set of seen words and
# the dictionary mapping characters to words. If ever we see a new
# character but we have seen the word, or the mappings between character
# and word do not match, we can return False.
#
# Time complexity: O(n) - Where n is the number of characters in s, the
# split function needs to visit all characters in s to find the
# delimiters, after that the algorithm runs in O(m) where m is the
# number of characters in pattern/words in s, if these are different,
# the algorithm exits quickly.
# Space complexity: O(n) - The dictionary of character: word will grow
# to hold all characters in the input.
#
# Runtime 25 ms Beats 97.22%
# Memory 13.8 MB Beats 74.33%
class DictAndSet:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        words_iter = iter(s.split())
        # A set of words that we have seen already.
        values = set()
        for c in pattern:
            if c not in d:
                # If the key is new, the value needs to also be new.
                val = next(words_iter)
                if val in values:
                    return False
                # Add the new entry.
                values.add(val)
                d[c] = val
            elif d[c] != next(words_iter):
                return False
        return True


# TODO Check the shorter solutions in the comments section.


def test():
    executors = [
        DictAndSet,
    ]
    tests = [
        ["aaa", "aa aa aa aa", False],
        ["abba", "dog cat cat dog", True],
        ["aaaa", "dog cat cat dog", False],
        ["abba", "dog dog dog dog", False],
        ["abba", "dog cat cat fish", False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.wordPattern(t[0], t[1])
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
