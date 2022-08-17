# 804. Unique Morse Code Words
# 🟢 Easy
#
# https://leetcode.com/problems/unique-morse-code-words/
#
# Tags: Array - Hash Table - String

import timeit
from string import ascii_lowercase
from typing import List

# A hashmap mapping each letter of the alphabet to its morse representation.
morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}

# Convert all words to morse using a hashmap of letter: morse, then add
# them to a set and return the length of the set.
#
# Time complexity: O(n) - We visit each character of the input.
# Space complexity: O(n) - The set may grow to the same size as the
# input array.
#
# Runtime: 42 ms, faster than 84.71%
# Memory Usage: 13.9 MB, less than 75.48%
class HashTable:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        representations = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        mappings = dict(zip(ascii_lowercase, representations))
        # Define a function that converts a word to morse.
        def toMorse(word: str) -> str:
            morse = [""] * len(word)
            for i, c in enumerate(word):
                morse[i] = mappings[c]
            return "".join(morse)

        # Set to store morse sequences that we have seen already.
        seen = set()
        # Iterate over all words converting them to morse and adding
        # them to a set of words we have seen.
        for word in words:
            seen.add(toMorse(word))
        # Return the number of different sequences obtained.
        return len(seen)


# We can improve the solution above using the unicode point of the
# character to determine the index of its conversion and set
# comprehension. Theoretically this would make the code more performant
# but it is not the case on the tests, maybe the call to ord() is slow.
#
# Time complexity: O(n) - We visit each character of the input.
# Space complexity: O(n) - The set may grow to the same size as the
# input array.
#
# Runtime: 55 ms, faster than 51.58%
# Memory Usage: 13.9 MB, less than 24.27%
class SetComprehension:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        representations = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        return len(
            {
                "".join(representations[ord(c) - ord("a")] for c in word)
                for word in words
            }
        )


def test():
    executors = [
        HashTable,
        SetComprehension,
    ]
    tests = [
        [["gin", "zen", "gig", "msg"], 2],
        [["a"], 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.uniqueMorseRepresentations(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
