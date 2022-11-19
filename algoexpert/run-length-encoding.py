# Run-Length Encoding
# 🟢 Easy
#
# https://www.algoexpert.io/questions/run-length-encoding
#
# Tags: Strings

import timeit


# This is a template that can be used as the starting point of a
# solution with minimal changes.
class Solution:
    def runLengthEncoding(self, string):
        last_count, last_char, res = 1, string[0], []
        for c in string[1:]:
            if c == last_char:
                last_count += 1
                if last_count == 10:
                    # If we have more than 9 of the last, append 9.
                    res.append("9" + last_char)
                    last_count = 1
            else:
                # Context switch.
                res.append(str(last_count) + last_char)
                last_char = c
                last_count = 1
        # Push the leftover char.
        res.append(str(last_count) + last_char)
        return "".join(res)


def test():
    executors = [Solution]
    tests = [
        ["122333", "112233"],
        ["AAAAAAAAAAAAABBCCCCDD", "9A4A2B4C2D"],
        ["                          ", "9 9 8 "],
        [
            "        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "8 9a9a9a9a9a4a",
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.runLengthEncoding(t[0])
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
