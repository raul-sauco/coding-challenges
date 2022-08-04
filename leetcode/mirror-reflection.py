# 858. Mirror Reflection
# 🟠 Medium
#
# https://leetcode.com/problems/mirror-reflection/
#
# Tags: Math - Geometry

import timeit


# We can simulate the beam traveling through the box.
#
# Time complexity: ?
#
# Runtime: 58 ms, faster than 23.76%
# Memory Usage: 13.9 MB, less than 63.37%
class Simulate:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Base case, the beam hits 0
        if not q:
            return 0
        # The beam will travel q vertical units for each p horizontal
        # ones. Lets call the beam's head position x,y.
        x, y = 0, 0
        # Flag, is the beam going up or down
        up = True
        while True:
            # Move the x position back and forth.
            x = p if not x else 0
            # Move the y position
            if up:
                y += q
                # Check if we have gone out of bounds.
                if y > p:
                    # If we have gone past the top, travel down an equal
                    # distance.
                    y = 2 * p - y
                    up = False
            else:
                y -= q
                # Check if we have gone out of bounds.
                if y < 0:
                    y = -y
                    up = True

            # Check if we hit any of the sensors.
            if x == p and y == 0:
                return 0
            elif x == p and y == p:
                return 1
            elif x == 0 and y == p:
                return 2


# We can divide p and q repeatedly by 2 until one of them is uneven,
# then determine which sensor the beam will hit first based on which and
# how many of them are even/odd.
#
# both uneven, i.e. 2,2 => sensor 1
# p uneven, q even i.e. 3,2 => sensor 0
# p even, q uneven i.e. 4,3 => sensor 2
#
# Time complexity: O(log(n)) - worst case p and q would be a small
# uneven number at a great power of 2.
# Space complexity: O(1)
#
# Runtime: 36 ms, faster than 86.14%
# Memory Usage: 13.9 MB, less than 16.83%
class Calculate:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p /= 2
            q /= 2
        # At least one of p,q is uneven.
        if p % 2 == 1 and q % 2 == 1:
            return 1
        elif p % 2 == 1:
            return 0
        return 2
        # The conditional return can be simplified to
        # return 1 - p % 2 + q % 2


# There is an interesting bit manipulation evolution of the math
# solution here:
#
# https://leetcode.com/problems/mirror-reflection/discuss/141773/C%2B%2BJavaPython-1-line-without-using-any-package-or
#
# Time complexity; O(1)? - bit manipulation and comparisons.
# Space complexity: O(1)
#
# Runtime: 34 ms, faster than 90.10%
# Memory Usage: 13.8 MB, less than 63.37%
#
# What the code in this solution is doing is getting the last bit that
# is set (1) on both p and q using (p & -p) and (q & - q), then
# comparing the results.
#
# (p & -p) gives the highest power of 2 by which p is evenly divisible.
# https://stackoverflow.com/a/15395424/2557030
#
# This is equivalent to dividing by 2 until one, or both, of the results
# is not even. When we divide by 2 we shift bits to the right, in this
# case until the least significant bit is 1 and we have an uneven
# number. With the bit-compare solution, we use the (p & -p) trick to
# get a value comprised only of the least significant not-zero bit of
# both numbers, if both are the same, they would have been both uneven
# after the loop, otherwise we check which one would have become uneven
# sooner, the one that results in the smaller least significant non-zero
# bit.
#
# (p & -p) >= (q & -q)
# will be true if p would yield an uneven number sooner, or at the same
# time as q
#
# (p & -p) > (q & -q)
# will be true if p would yield an uneven number sooner than q
#
# If q would yield uneven before p:
# False + False => 0
#
# If p and q would yield uneven numbers at the same time:
# True + False => 1
#
# If p would yield an uneven number earlier than q:
# True + True => 2
#
# Credits to the explanation on why (p & -p) works:
# https://stackoverflow.com/a/15395548/2557030
class BitCompare:
    def mirrorReflection(self, p: int, q: int) -> int:
        return ((p & -p) >= (q & -q)) + ((p & -p) > (q & -q))


def test():
    executors = [Simulate, Calculate]
    tests = [
        [2, 1, 2],
        [3, 1, 1],
        [7, 0, 0],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.mirrorReflection(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {i} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
