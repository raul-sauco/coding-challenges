# https://leetcode.com/problems/reverse-bits/

# Tags: Divide and Conquer - Bit Manipulation

import timeit

# 1e4 calls
# » Iterative           0.14332   seconds
# » BuiltInFn           0.01705   seconds
# » BuiltInFnZFill      0.01512   seconds

# Use div and mod to obtain the reversed bits of the input then use bit shifting to construct the
# output int.
#
# Time complexity: O(1) - size of n is fixed to 32. We could also see it as O(log(len(n)))
# Space complexity: O(1) - a 32 position list
#
# Runtime: 65 ms, faster than 17.08% of Python3 online submissions for Reverse Bits.
# Memory Usage: 13.8 MB, less than 49.51% of Python3 online submissions for Reverse Bits.
class Iterative:
    def reverseBits(self, n: int) -> int:
        bits = []

        # Get the reversed bits of the input
        while n:
            n, rem = divmod(n, 2)
            bits.append(rem)

        # Pad the input to the required 32 bits
        while len(bits) < 32:
            bits.append(0)

        # bits = bits[::-1] if we needed to reverse
        # Convert back to int
        # https://stackoverflow.com/a/12461400/2557030
        out = 0
        for bit in bits:
            out = (out << 1) | bit

        return out


# Runtime: 41 ms, faster than 76.36% of Python3 online submissions for Reverse Bits.
# Memory Usage: 13.8 MB, less than 49.51% of Python3 online submissions for Reverse Bits.
class BuiltInFn:
    def reverseBits(self, n: int) -> int:
        return int("{0:032b}".format(n)[::-1], 2)
        # bits = "{0:032b}".format(n)
        # bits = bits[::-1]
        # return int(bits, 2)


# Runtime: 52 ms, faster than 47.00% of Python3 online submissions for Reverse Bits.
# Memory Usage: 13.8 MB, less than 49.51% of Python3 online submissions for Reverse Bits.
class BuiltInFnZFill:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)
        # https://stackoverflow.com/a/10322018/2557030
        # bits = bin(n)[2:].zfill(32)
        # bits = str(bits)[::-1]
        # return int(bits, 2)


def test():
    executors = [Iterative, BuiltInFn, BuiltInFnZFill]
    tests = [
        [0, 0],
        [1, 2147483648],
        [
            43261596,  # 00000010100101000001111010011100
            964176192,  # 00111001011110000010100101000000
        ],
        [
            4294967293,  # 11111111111111111111111111111101
            3221225471,  # 10111111111111111111111111111111
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.reverseBits(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
