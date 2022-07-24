# 299. Bulls and Cows
# 🟠 Medium
#
# https://leetcode.com/problems/bulls-and-cows/
#
# Tags: Hash Table - String - Counting

import timeit
from collections import Counter, defaultdict


# Iterate over the length of the input strings checking if the characters match. If they match, add to the "bulls"
# if they don't match, store them in one of two dictionaries, seen in the guess or seen in the secret.
# Loop through one of the dictionaries checking which characters, and in which frequency, are also in the other
# dictionary. For each match in character, add 1 to the cow count.
#
# Time complexity: O(n) - We iterate over the input once, then once over the dictionary of non-matched digits.
# Space complexity: O(n) - The dictionary could grow to size n.
#
# Runtime: 71 ms, faster than 39.09% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 13.8 MB, less than 98.91% of Python3 online submissions for Bulls and Cows.
class LoopCheck:
    def getHint(self, secret: str, guess: str) -> str:
        # Store the count of both types of matches
        bulls, cows, ds, dg = 0, 0, defaultdict(int), defaultdict(int)
        # Iterate over the characters in guess and secret checking if they match.
        for i, c in enumerate(secret):
            if c == guess[i]:
                bulls += 1
            else:
                # Update the dictionaries with the characters at this position.
                ds[c] += 1
                dg[guess[i]] += 1

        # Compare the dictionaries.
        for c in dg:
            if c in ds:
                while dg[c] and ds[c]:
                    cows += 1
                    dg[c] -= 1
                    ds[c] -= 1

        return f"{bulls}A{cows}B"


# Similar to the above solution but, instead of checking matches with a nested loop, we use the fact that the
# default dictionary will return 0 for non-existing indexes and check the matches using the min() function.
#
# Time complexity: O(n) - We iterate over the input once, then once over the dictionary of non-matched digits.
# Space complexity: O(n) - The dictionary could grow to size n.
#
# Runtime: 50 ms, faster than 78.05% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 13.9 MB, less than 31.00% of Python3 online submissions for Bulls and Cows.
class MinCheck:
    def getHint(self, secret: str, guess: str) -> str:
        # Store the count of both types of matches
        bulls, cows, ds, dg = 0, 0, defaultdict(int), defaultdict(int)
        # Iterate over the characters in guess and secret checking if they match.
        for i, c in enumerate(secret):
            if c == guess[i]:
                bulls += 1
            else:
                # Update the dictionaries with the characters at this position.
                ds[c] += 1
                dg[guess[i]] += 1

        # Compare the dictionaries.
        for c in dg:
            cows += min(dg[c], ds[c])

        return f"{bulls}A{cows}B"


# When some tasks can be performed by built-in functions, they tend to be more performant, even though the theoretical
# work load is bigger. For example, using counter and sum, we iterate more times over the inputs but, the fact that
# the code being called is C, makes the solution faster.
#
# Time complexity: O(n) - We iterate over the input once, then once over the dictionary of non-matched digits.
# Space complexity: O(n) - The dictionary could grow to size n.
#
# Runtime: 33 ms, faster than 99.13% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 13.8 MB, less than 78.40% of Python3 online submissions for Bulls and Cows.
class BuiltInFn:
    def getHint(self, secret: str, guess: str) -> str:
        # Use Counter to create two dictionaries, like in the previous solutions.
        dict_secret, dict_guess = Counter(secret), Counter(guess)
        # Use zip to find bulls, positions where the digit in secret and guess are the same.
        bulls = sum(i == j for i, j in zip(secret, guess))
        # We have bulls, cows are matches in the dictionaries minus bulls.
        return "%sA%sB" % (bulls, sum((dict_secret & dict_guess).values()) - bulls)


def test():
    executors = [LoopCheck, MinCheck, BuiltInFn]
    tests = [
        ["1807", "7810", "1A3B"],
        ["1123", "0111", "1A1B"],
        ["112233445566778899123456789", "223344556677889912345678911", "0A27B"],
        ["112233445566778899123456789", "122334455667788991234567891", "9A18B"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1e4"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.getHint(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
