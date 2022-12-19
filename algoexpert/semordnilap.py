# Semordnilap
# 🟢 Easy
#
# https://www.algoexpert.io/questions/semordnilap
#
# Tags: String - Hash Set

import timeit


# This problem can be seen as a variation of two sum, we can use the
# same approach, iterate over the input checking if the reverse of the
# current word has been seen, if yes, add it to the result set,
# otherwise, add it to the set of words that we have seen. We could
# remove a word from the set to clean up after we find its match,
# depends on if we want the code to run faster or to be cleaner.
#
# Time complexity: O(n) - Where n is the number of characters in the
# input.
# Space complexity: O(n) - The set of seen words can grow to the size of
# the input.
class Solution:
    def semordnilap(self, words):
        res, seen = [], set()
        for word in words:
            rev = word[::-1]
            if rev in seen:
                res.append([word, rev])
            else:
                seen.add(word)
        return res


def test():
    executors = [Solution]
    tests = [
        [[], []],
        [["aaa", "bbbb"], []],
        [["dog", "god"], [["god", "dog"]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.semordnilap(t[0])
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
