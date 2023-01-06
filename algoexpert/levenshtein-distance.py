# Levenshtein Distance
# 🟠 Medium
#
# https://www.algoexpert.io/questions/levenshtein-distance
#
# Tags: Dynamic Programming

import timeit


# Compute the changes that we will need to introduce for each
# combination of substrings of both input strings starting at the index
# 0, when the next characters match, the number of edits will be the
# same as without the last two characters that we added. When the
# two last characters do not match, the number of edits will be the
# same as the best between before we added one, or two, of the last
# characters, plus one for the edit needed because the current
# characters do not match.
#
# Time complexity: O(m*n) - Where m and n are the lengths of the input
# strings.
# Space complexity: O(min(m,n)) - Checking which string is longer lets
# us store only one row of extra memory containing the number of
# edits needed when we had one character less of the longer string.
class BottomUpDP:
    def levenshteinDistance(self, str1: str, str2: str) -> int:
        # Choose the shorter string's length for the dp array (m).
        short, long = str1, str2
        m, n = len(short), len(long)
        if m > n:
            short, long, m, n = long, short, n, m
        # The number of changes we need to make if we take the empty
        # string for str2.
        dp = [i for i in range(m + 1)]
        # Add one character of str2 per loop.
        for j in range(n):
            # Compute the substitutions with this prefix of str2.
            nxt = [j + 1] * (m + 1)
            # Iterate over the different prefixes of str1 computing the
            # number of substitutions to make both current prefixes the
            # same word.
            for i in range(m):
                if short[i] == long[j]:
                    # If the characters at the current indexes match,
                    # we only need to make the same changes as before
                    # adding both these characters.
                    nxt[i + 1] = dp[i]
                else:
                    # If the characters do not match, we can take the
                    # best option between removing either of them or
                    # both of them and add one more change.
                    nxt[i + 1] = min(dp[i], dp[i + 1], nxt[i]) + 1
            dp = nxt
        return dp[-1]


def test():
    executors = [BottomUpDP]
    tests = [
        ["", "", 0],
        ["", "abc", 3],
        ["abc", "abc", 0],
        ["abc", "yabd", 2],
        ["table", "bal", 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.levenshteinDistance(t[0], t[1])
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
