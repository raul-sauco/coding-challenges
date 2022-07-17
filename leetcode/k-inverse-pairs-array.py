# https://leetcode.com/problems/k-inverse-pairs-array/

# Tags: Dynamic Programming


import timeit


# We can see that the number of ways to invert pairs will be equal to the number of ways
# to invert pairs for n-1 and each value of k up to n-1
#
# The obvious solution is bottom-up tabulation, but we can first look at memoization
#
# Time complexity: O(nk min(n,k)) we call kInversePairs for each position, each calls costs min(n,k)
# since already computed values will not be recalculated
# Space complexity: O(nk) for the memo
#
# Time limit exceeded
class Memoization:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # Create the memo if it does not exist
        if not hasattr(self, "memo"):
            self.memo = [[None for _ in range(k + 1)] for _ in range(n + 1)]
            # Base cases
            self.memo[0][0] = 0
            for j in range(1, n + 1):
                self.memo[j][0] = 1

        # If the value is found, do not recalculate
        if self.memo[n][k] is not None:
            return self.memo[n][k]

        # Calculate the sum of previous n and k [0..n-1]
        result = 0
        i = n - 1
        for j in range(min(k, i) + 1):
            result += self.kInversePairs(i, k - j)

        self.memo[n][k] = result
        return result % MOD


# We can calculate the results bottom-up
#
# Time complexity: O(n*k*min(n-1, k))
# Space complexity: O(n*k)
#
# Time limit exceeded
class Tabulation:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # Create a matrix to store the results
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    for p in range(min(j, i - 1) + 1):
                        # Sum the previous results for n-1 and p in 0 min(j, i-1)
                        dp[i][j] = dp[i][j] + dp[i - 1][j - p]

        # We could save each result with % MOD but it is quicker to do it once and python will not overflow
        return dp[n][k] % MOD


# Optimize the previous solution using only one array to store results for the last value of n
#
# Time complexity: O(n*k) for each n iterates twice over k
# Space complexity: O(1) it only stores one array of size k+1
#
# Runtime: 551 ms, faster than 70.00% of Python3 online submissions for K Inverse Pairs Array.
# Memory Usage: 14.2 MB, less than 72.50% of Python3 online submissions for K Inverse Pairs Array.
class OptTabulation:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [1] + [0] * k
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                dp[j] += dp[j - 1]
            for j in range(k, 0, -1):
                dp[j] -= j - i >= 0 and dp[j - i]
        return dp[k] % (10**9 + 7)


def test():
    executors = [
        Memoization,
        Tabulation,
        OptTabulation,
    ]
    tests = [
        [5, 4, 20],
        [3, 0, 1],
        [3, 1, 2],
        [1, 0, 1],
        [1, 1, 0],
        [90, 90, 547544970],
        # [1000, 1000, 663677020],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.kInversePairs(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
