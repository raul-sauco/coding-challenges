# 151. Reverse Words in a String
# 🟠 Medium
#
# https://leetcode.com/problems/problem-name/
#
# Tags: Two Pointers - String

import timeit


# Use a deterministic finite automaton (DFA). Iterate over all the
# positions in the input string checking the character at that position
# while keeping track of the current state. States can be: "reading a
# word" and "skipping blanks". If we are reading the characters of a
# word and find a blank, we append the word to the result array and
# reset the current word to an empty array.
#
# Time complexity: O(n) - We iterate over all the characters in the
# input array several times, to read them, to build the word and to
# build the result.
# Space complexity: O(n) - We store all characters in the words array.
#
# Runtime: 33 ms, faster than 95.34%
# Memory Usage: 14 MB, less than 78.97%
class DFA:
    def reverseWords(self, s: str) -> str:
        words = []
        # 0 => reading blanks, 1 => building word
        state, word = 0, []
        for c in s:
            # We are reading a word.
            if state:
                if c == " ":
                    words.append("".join(word))
                    word = []
                    state = 0
                else:
                    word.append(c)
            elif c != " ":
                state = 1
                word.append(c)
        if word:
            words.append("".join(word))
        return " ".join(words[::-1])


# Python has built-in functions that make this problem quite trivial, it
# would be good to, at least, be aware of them and mention them in an
# interview, even when also providing the other solution.
#
# Time complexity: O(n) - Each of the built-in functions still need to
# read the entire string.
# Space complexity: O(n) - The entire input is loaded into memory to
# manipulate.
#
# Runtime: 37 ms, faster than 90.50%
# Memory Usage: 14 MB, less than 48.44%
class BuiltInFn:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


def test():
    executors = [
        DFA,
        BuiltInFn,
    ]
    tests = [
        ["  hello world  ", "world hello"],
        ["the sky is blue", "blue is sky the"],
        ["a good   example", "example good a"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.reverseWords(t[0])
                exp = t[1]
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
