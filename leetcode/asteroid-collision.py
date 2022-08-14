# 735. Asteroid Collision
# 🟠 Medium
#
# https://leetcode.com/problems/asteroid-collision/
#
# Tags: Array - Stack

import timeit
from typing import List


# Use a stack to push the asteroids into. When we see a new left bound
# asteroid, and the last asteroid in the stack is right-bound, we pop
# from the stack until either the asteroid in top of the stack is
# traveling left, and/or this one has been destroyed.
#
# Time complexity: O(n) - We visit each element and decide to either
# push it onto the stack as it is or remove either this element and/or
# another one from the result. The complexity is bounded to O(2*n).
# Space complexity: O(n) - The stack could have every element on the
# input.
#
# Runtime: 172 ms, faster than 36.29%
# Memory Usage: 15.3 MB, less than 25.57%
class StackSolution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stable = []
        for asteroid in asteroids:
            # Iterate while we have a last asteroid traveling right and
            # the current asteroid is traveling left.
            # stable and asteroid < 0 and stable[-1] > 0
            while stable and asteroid < 0 < stable[-1]:
                # We have a collision situation, asteroid is traveling
                # left and the last stable asteroid is traveling right.
                # Get the mass of the current asteroid.
                ab = -asteroid
                # If they have the same mass, they are both destroyed
                # and we move on to check the next asteroid.
                if ab == stable[-1]:
                    stable.pop()
                    break
                # If this asteroid's mass is bigger than the last stable
                # asteroid's mass, the later is destroyed and we keep
                # checking the result of this asteroids trajectory with
                # the rest of the stable set of asteroids.
                if ab > stable[-1]:
                    stable.pop()
                    continue
                # If this asteroid's mass is smaller than the mass of
                # the last stable asteroid, this asteroid is destroyed
                # and we can check the next asteroid of the input.
                break
            # If we don't have any asteroids in the stack, the last one
            # is traveling left or both the current one and the last
            # one are traveling right, append this asteroid to the
            # stable list of asteroids.
            else:
                stable.append(asteroid)

        # We have processed all asteroids.
        return stable


def test():
    executors = [StackSolution]
    tests = [
        [[-2, -1, 1, 2], [-2, -1, 1, 2]],
        [[5, 10, -5], [5, 10]],
        [[8, -8], []],
        [[10, 2, -5], [10]],
        [[-5, 2], [-5, 2]],
        [[-5, 2, -3], [-5, -3]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.asteroidCollision(t[0])
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
