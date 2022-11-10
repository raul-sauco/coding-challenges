# Generate Document
# 🟢 Easy
#
# https://www.algoexpert.io/questions/generate-document
#
# Tags: String - Hash Table

import timeit
from collections import Counter


# Use two counters, frequencies needed and available, then make sure
# that we have, at least, as many available of each as we need.
#
# Time complexity: O(m + n) - Where m and n are the lengths of the input
# strings.
# Space complexity: O(c) - Where c is the number of unique characters
# between both input strings.
class Solution:
    def generateDocument(self, characters: str, document: str) -> bool:
        need, available = Counter(document), Counter(characters)
        return all(available[c] >= need[c] for c in need)


def test():
    executors = [Solution]
    tests = [
        ["A", "a", False],
        ["a", "a", True],
        ["Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!", True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.generateDocument(t[0], t[1])
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
