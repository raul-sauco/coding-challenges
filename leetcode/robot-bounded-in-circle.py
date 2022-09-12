# 1041. Robot Bounded In Circle
# 🟠 Medium
#
# https://leetcode.com/problems/robot-bounded-in-circle/
#
# Tags: Math - String - Simulation

import timeit


# Simulate the robot movements, at the end of each set of instructions,
# check if the distance keeps increasing. We only have four directions
# of movement that are possible, after each set of iterations, check if
# the robot is back at the origin, if it is, it is bounded, if after 4
# sets of instructions the robot is not back at the origin, it is not
# bounded by a circle. The explanation is that, if we look at the vector
# formed by executing all the instructions, the consecutive vectors
# formed by successive executions can only have an angle of 0, 90 or 180
# degrees with each other.
#
# Time complexity: O(n) - Where n is the number of instructions, we
# execute at most 4 times all the instructions.
# Space complexity: O(1) - Constant space.
#
# Runtime: 32 ms, faster than 92.50%
# Memory Usage: 14 MB, less than 21.81%
class Run4Times:
    def isRobotBounded(self, instructions: str) -> bool:
        # We start at the origin and facing north. Dir = (0, 1)
        pos, dir = (0, 0), (0, 1)
        # Run as many loops as there are possible angles between
        # full instructions vectors.
        for _ in range(4):
            # Run a full loop of instructions.
            for instruction in instructions:
                if instruction == "G":
                    pos = (pos[0] + dir[0], pos[1] + dir[1])
                elif instruction == "L":
                    dir = (-dir[1], dir[0])
                else:
                    dir = (dir[1], -dir[0])
            # We have run a full set of instructions.
            if pos == (0, 0):
                return True
        # If we do 4 loops and don't go back to the origin, we will
        # keep moving away.
        return False


# A quicker way to arrive at the same result is to run the instructions
# one time and check if the robot has either gone back to the origin or
# it is facing in a different direction. If the robot is facing in a
# different direction, the next vector will start at that angle, 90, 180
# or 270 degrees from the original, and it will eventually go back to
# the origin.
#
# Time complexity: O(n) - Where n is the number of instructions.
# Space complexity: O(1) - Constant space.
#
# Runtime: 59 ms, faster than 21.85%
# Memory Usage: 13.9 MB, less than 21.81%
class Run1Time:
    def isRobotBounded(self, instructions: str) -> bool:
        # We start at the origin and facing north. Dir = (0, 1)
        pos, dir = (0, 0), (0, 1)
        # Go through the instructions once.
        for instruction in instructions:
            if instruction == "G":
                pos = (pos[0] + dir[0], pos[1] + dir[1])
            elif instruction == "L":
                dir = (-dir[1], dir[0])
            else:
                dir = (dir[1], -dir[0])
        # If we are back at the origin, or facing in any other direction
        # than north, the robot is bounded by a circle.
        return pos == (0, 0) or dir != (0, 1)


def test():
    executors = [
        Run4Times,
        Run1Time,
    ]
    tests = [
        ["RLLGLRRRRGGRRRGLLRRR", True],
        ["GLRLGLLGLGRGLGL", True],
        ["LLGRL", True],
        ["GGLLGG", True],
        ["GG", False],
        ["GL", True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isRobotBounded(t[0])
                exp = t[1]
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
