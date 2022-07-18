# https://leetcode.com/problems/happy-number/


# Tags: Hash Table - Math - Two Pointers

import timeit
from typing import List


# Perform the operation while we don't detect a loop, using a set for n we have seen, or find the 'happy' result
#
# Time complexity: O(log(n)) - Calculating the next value needs iterating over each digit of the current number.
# Space complexity; O(1) - the set will store a max of 243 values. It would be O(log(n)) if we stored all numbers.
#
# Runtime: 42 ms, faster than 78.83% of Python3 online submissions for Happy Number.
# Memory Usage: 13.8 MB, less than 60.10% of Python3 online submissions for Happy Number.
class LoopAndSet:
    def isHappy(self, n: int) -> bool:
        seen = set()
        # While we don't go back to a number we have seen already or 1
        while n not in seen and n != 1:
            # Keep track of numbers we have seen already, only worry about n below the umbral.
            if n < 243:
                seen.add(n)
            s = 0
            # Iterate over the digits in the current n
            for d in map(int, str(n)):
                s += d**2

            n = s

        return n == 1


# Use Floyd's cycle detection algorithm
#
# Time complexity: O(log(n))
# Space complexity; O(1)
class Floyd:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit**2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1


# There is only one cycle possible, all series will end up in this cycle or leading to 1
# only check values against numbers in this particular cycle.
#
# Time complexity: O(log(n))
# Space complexity: O(1)
#
# Runtime: 48 ms, faster than 63.70% of Python3 online submissions for Happy Number.
# Memory Usage: 13.8 MB, less than 60.10% of Python3 online submissions for Happy Number.
class OnlyCycle:
    def isHappy(self, n: int) -> bool:
        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}
        while n not in cycle_members and n != 1:
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            n = total_sum
        return n == 1


def test():
    executors = [LoopAndSet, Floyd, OnlyCycle]
    tests = [[19, True], [2, False]]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.isHappy(t[0])
                exp = t[1]
                assert result == exp, f"\033[93m» {t[0]} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
