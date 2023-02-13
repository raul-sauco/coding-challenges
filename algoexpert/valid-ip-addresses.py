# Valid IP Addresses
# 🟠 Medium
#
# https://www.algoexpert.io/questions/valid-ip-addresses
#
# Tags: String

import timeit
from typing import List


# An iterative solution, have 3 nested loops that compute the index
# before which we want to insert the dots, if the resulting bytes are
# valid, it adds the result to the solution.
#
# Time complexity: O(1) - There are three nested loops any of which can
# tries 3 different values that is O(3^3) which simplifies to O(1).
# Space complexity: O(2^n) - With the right input, we could have 2^n
# number of valid IP addresses that we store in res.
class Solution:
    def validIPAddresses(self, string: str) -> List[str]:
        # Base case, we cannot build any IPs.
        if string[0] == 0:
            return []
        res = []
        limit = 255
        for i in range(1, 4):
            byte1 = string[:i]
            if int(byte1) > limit or (byte1[0] == "0" and len(byte1) > 1):
                break
            for j in range(i + 1, i + 4):
                if j > len(string) - 2:
                    break
                byte2 = string[i:j]
                if int(byte2) > limit or (byte2[0] == "0" and len(byte2) > 1):
                    break
                for k in range(j + 1, j + 4):
                    if not (len(string) - 4 < k < len(string)):
                        continue
                    byte3 = string[j:k]
                    if int(byte3) > limit or (
                        byte3[0] == "0" and len(byte3) > 1
                    ):
                        continue
                    byte4 = string[k:]
                    if int(byte4) > limit or (
                        byte4[0] == "0" and len(byte4) > 1
                    ):
                        continue
                    res.append(".".join([byte1, byte2, byte3, byte4]))
        return res


def test():
    executors = [Solution]
    tests = [
        [
            "1921680",
            [
                "1.9.216.80",
                "1.92.16.80",
                "1.92.168.0",
                "19.2.16.80",
                "19.2.168.0",
                "19.21.6.80",
                "19.21.68.0",
                "19.216.8.0",
                "192.1.6.80",
                "192.1.68.0",
                "192.16.8.0",
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.validIPAddresses(t[0])
                exp = t[1]
                assert sorted(result) == sorted(exp), (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
