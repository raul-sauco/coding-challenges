# caesar Cipher Encryptor
# 🟢 Easy
#
# https://www.algoexpert.io/questions/caesar-cipher-encryptor
#
# Tags: String

import timeit


# Easier to read version that uses a loop to iterate over the input and
# convert each character using the key.
#
# Time complexity: O(n) - We visit each character in the input once.
# Space complexity: O(n) - The array that we use to build the result.
class ForLoop:
    def caesarCipherEncryptor(self, string, key):
        res = []
        key %= 26
        for c in string:
            val = ord(c) + key
            if val > 122:
                val -= 26
            res.append(chr(val))
        return "".join(res)


# More idiomatic version that uses list comprehension.
#
# Time complexity: O(n) - We visit each character in the input once.
# Space complexity: O(n) - The array that we use to build the result.
class ListComprehension:
    def caesarCipherEncryptor(self, string, key):
        return "".join([chr(((ord(c) + key - 97) % 26) + 97) for c in string])


def test():
    executors = [
        ForLoop,
        ListComprehension,
    ]
    tests = [
        ["xyz", 2, "zab"],
        ["abc", 0, "abc"],
        ["abc", 26, "abc"],
        ["abc", 52, "abc"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.caesarCipherEncryptor(t[0], t[1])
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
