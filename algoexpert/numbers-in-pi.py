# Numbers In Pi
# 🔴 Hard
#
# https://www.algoexpert.io/questions/numbers-in-pi
#
# Tags: Dynamic Programming

import timeit


# Use a recursive function that takes in the index of the next character
# that we are assessing, and the string prefix that we have built so far,
# then it checks if the string resulting of adding the current character
# is one of the numbers in the input, if yes, it branches into two, one
# branch checks the result of choosing to make a cut after the current
# digit and one branch chooses to keep building the current string, the
# function returns the best result between both branches.
#
# Time complexity: O(n*m) - Where n is the number of characters in pi
# and m is the size of the numbers array, we iterate over each number
# in pi inside the branch function, and we can split into m calls to
# branches.
# Space complexity: O(n+m) - The call stack can have a max height of n,
# the numbers set has one entry per element in numbers.
class Solution:
    def numbersInPi(self, pi, numbers):
        num_set = {num for num in numbers}
        n = len(pi)
        calls = [0]
        # A function that adds the character at idx to the current
        # string that is being built and checks if it is one of the
        # numbers in the input, if it is, it branches into cutting and
        # not cutting right after the number, returning the minimum
        # number of cuts between both options.
        def branch(idx: int, current: str, cuts: int) -> int:
            calls[0] += 1
            # We have gone past the end, not a valid combo.
            if idx == n:
                return float("inf")
            current += pi[idx]
            # The current value matches
            if current in num_set:
                if idx == n - 1:
                    return cuts
                return min(
                    branch(idx + 1, current, cuts),
                    branch(idx + 1, "", cuts + 1),
                )
            # Current is not in num set.
            return branch(idx + 1, current, cuts)

        # Initial call
        res = branch(0, "", 0)
        if res == float("inf"):
            return -1
        return res


def test():
    executors = [Solution]
    tests = [
        [
            "3141592653589793238462643383279",
            [
                "314159265358979323846",
                "26433",
                "8",
                "3279",
                "314159265",
                "35897932384626433832",
                "79",
            ],
            2,
        ],
        [
            "3141592653589793238462643383279",
            [
                "31415926535879323846",
                "26433",
                "8",
                "3279",
                "314159265",
                "35897932384626433832",
                "49",
            ],
            -1,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numbersInPi(t[0], t[1])
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
