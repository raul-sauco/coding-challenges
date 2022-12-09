# Reverse Words In String
# 🟠 Medium
#
# https://www.algoexpert.io/questions/reverse-words-in-string
#
# Tags: String

import timeit


# Read words or groups of spaces and append them to a stack, then pop
# from the stack to reverse the order of groups.
#
# Time complexity: O(n) - Each character is visited 3 times.
# Space complexity: O(n) - All characters are stored in the stack.
class Solution:
    def reverseWordsInString(self, string: str) -> str:
        # Push entire words or space sequences into a stack.
        stack, reading_word, word = [], False, []
        for c in string:
            if (reading_word and c == " ") or (not reading_word and c != " "):
                reading_word = not reading_word
                stack.append("".join(word))
                word = [c]
            else:
                word.append(c)
        stack.append("".join(word))
        # return "".join([w for w in reversed(stack)])
        # Reverse the stack without using reversed.
        l, r = 0, len(stack) - 1
        while l < r:
            stack[l], stack[r] = stack[r], stack[l]
            l, r = l + 1, r - 1
        return "".join([w for w in stack])


def test():
    executors = [Solution]
    tests = [
        [" ", " "],
        ["        ", "        "],
        ["test        ", "        test"],
        ["words, separated, by, commas", "commas by, separated, words,"],
        ["AlgoExpert is the best!", "best! the is AlgoExpert"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.reverseWordsInString(t[0])
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
