# 1220. Count Vowels Permutation
# 🔴 Hard
#
# https://leetcode.com/problems/count-vowels-permutation/
#
# Tags: Dynamic Programming

import timeit

MOD = 10**9 + 7

# Let dp[i][j] be the number of strings of length i that ends with the
# j-th vowel, and we know that:
#
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
#
# That means that we can iterate over all the numbers smaller than n
# and, for each iteration, the number of vowel combinations that we
# can do for each vowel will be the sum of the possible combinations
# of the vowels that are allowed to go before it according to the rules.
#
# Time complexity: O(n) - We loop once for each value between 1..n
# Space complexity: O(1) - We use constant space.
#
# Runtime: 326 ms, faster than 75.50%
# Memory Usage: 14.2 MB, less than 68.69%
class DP:
    def countVowelPermutation(self, n: int) -> int:
        # Create the dp array and initialize it with the number of
        # possible ways to form 1 character long strings that finish in
        # the given vowel, 0 => a, 1 => e, 2 => i, 3 => o, 4 => u
        prev = [1] * 5
        # Initialize an array where we will put the computed values on
        # each iteration.
        curr = prev.copy()
        for _ in range(n - 1):
            # a can follow e, i, u
            curr[0] = prev[1] + prev[2] + prev[4]
            # e can follow a, i
            curr[1] = prev[0] + prev[2]
            # i can follow e, o
            curr[2] = prev[1] + prev[3]
            # o can follow i
            curr[3] = prev[2]
            # u can follow i, o
            curr[4] = prev[2] + prev[3]
            # Substitute the previous array for the new one.
            prev = curr.copy()

        # The result is the sum of the different ways to combine the
        # vowels.
        return sum(curr) % MOD


# Same solution as above but update all the values on one assignment.
#
# Time complexity: O(n) - We loop once for each value between 1..n
# Space complexity: O(1) - We use constant space.
#
# Runtime: 311 ms, faster than 77.53%
# Memory Usage: 14.1 MB, less than 80.85%
class DPSingleList:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % MOD


def test():
    executors = [
        DP,
        DPSingleList,
    ]
    tests = [
        [1, 5],
        [2, 10],
        [5, 68],
        [2345, 451992221],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.countVowelPermutation(t[0])
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
