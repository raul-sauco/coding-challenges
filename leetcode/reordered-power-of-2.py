# 869. Reordered Power of 2
# 🟠 Medium
#
# https://leetcode.com/problems/reordered-power-of-2/
#
# Tags: Math - Sorting - Coding - Enumeration

import timeit
from collections import Counter


# Have a dictionary of all powers of 2 smaller than 10^9 keyed by the
# number of digits that they have. Get all possible candidate powers of
# two getting the number of digits of the input. Count the different
# digit frequencies on both the input and each of the candidates, if any
# of them has the same frequency of the different digits, the input
# could be a reordering of that power of two, if the input does not have
# the same character frequency as any of the candidates, it cannot be a
# reordering of a power of two.
#
# Time complexity: O(1) - We are, in the worst case counting 9 digits
# once and a different 9 digits a max of 4 times.
# Space complexity: O(1) - Constant space.
#
# Runtime: 48 ms, faster than 73.80%
# Memory Usage: 13.9 MB, less than 64.17%
class HashTableCounter:
    def reorderedPowerOf2(self, n: int) -> bool:
        # A dictionary with all powers of 2 for each number of digits.
        pot = {
            1: [1, 2, 4, 8],
            2: [16, 32, 64],
            3: [128, 256, 512],
            4: [1024, 2048, 4096, 8192],
            5: [16384, 32768, 65536],
            6: [131072, 262144, 524288],
            7: [1048576, 2097152, 4194304, 8388608],
            8: [16777216, 33554432, 67108864],
            9: [134217728, 268435456, 536870912],
        }
        # Find all possible candidates, it needs to have the same
        # number of digits.
        n = str(n)
        candidates = pot[len(n)]
        freq_n = Counter(n)
        # For each candidate, check if the input could be a permutation.
        for candidate in candidates:
            freq = Counter(str(candidate))
            if freq == freq_n:
                return True
        # If the input could not be a reordering of any of the
        # candidates, return False.
        return False


# Similar idea to the previous solution but convert the input and the
# candidates to sorted strings and compare that.
#
# Time complexity: O(1) - We iterate over the number of digits of the
# input to convert them to string and them sorted, but the input length
# in < 10 digits, so constant time.
# Space complexity: O(1) - Constant space for the dictionary and the
# input converted to string.
#
# Runtime: 48 ms, faster than 73.80%
# Memory Usage: 13.9 MB, less than 64.17%
class HashTableSort:
    def reorderedPowerOf2(self, n: int) -> bool:
        # A dictionary with all powers of 2 for each number of digits
        # converted to sorted strings.
        pot = {
            1: ["1", "2", "4", "8"],
            2: ["16", "23", "46"],
            3: ["128", "256", "125"],
            4: ["0124", "0248", "0469", "1289"],
            5: ["13468", "23678", "35566"],
            6: ["011237", "122446", "224588"],
            7: ["0145678", "0122579", "0134449", "0368888"],
            8: ["11266777", "23334455", "01466788"],
            9: ["112234778", "234455668", "012356789"],
        }
        # Convert the input to a sorted string.
        n = "".join(sorted(str(n)))
        # The sorted input should be one of the sorted powers of two
        # of the same length.
        return n in pot[len(n)]


def test():
    executors = [
        HashTableCounter,
        HashTableSort,
    ]
    tests = [
        [1, True],
        [10, False],
        [124624, True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.reorderedPowerOf2(t[0])
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
