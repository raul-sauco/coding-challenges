# 838. Push Dominoes
# 🟠 Medium
#
# https://leetcode.com/problems/push-dominoes/
#
# Tags: Two Pointers - String - Dynamic Programming

import timeit
from collections import deque

# 1000 calls
# » TwoPointers         0.01016   seconds
# » BFS                 0.01630   seconds
# » DP                  0.02575   seconds

# Iterate over the dominoes checking the current value. When we find a
# "L" or "R" value, handle that portion of the string. We keep a pointer
# to the leftmost value that has been processed. When the iterator finds
# a "L" value, it will check the value under the leftmost pointer, if it
# is a "R" it will use a shrinking window to push left dominoes to the
# right and right dominoes to the left until the pushes cancel each
# other in the middle. If a neutral "." is under the left pointer, then
# all the dominoes left of the iterator get pushed to the left. Once we
# process that section, we update the left pointer. When the iterator
# finds a "R" value, it checks the element under the left pointer, if
# it finds a "R", it updates all values between the pointers to "R" and
# adjusts the left pointer. If it finds a ".", it will adjust the
# pointer without updating any values.
#
# Time complexity: O(n) - Any value is visited at most twice.
# Space complexity: O(n) - The input is cast to a list to work with the
# values, then parsed to string to return the expected format.
#
# Runtime: 478 ms, faster than 61.69%
# Memory Usage: 15.8 MB, less than 83.88%
class TwoPointers:
    def pushDominoes(self, dominoes: str) -> str:
        # Make a mutable copy of the input.
        dom = list(dominoes)
        # Initialize a left pointer.
        l = 0
        # Iterate over the positions.
        for i in range(len(dom)):
            if dom[i] == ".":
                continue
            # Check what happens when we push that section to the left.
            if dom[i] == "L":
                # If the left domino was not pushed.
                if dom[l] == ".":
                    # If the leftmost domino was not pushed, they all
                    # fall to the left.
                    for j in range(l, i):
                        dom[j] = "L"
                else:
                    # The left domino is a "R" two pointers.
                    r = i
                    while l < r:
                        dom[l] = "R"
                        dom[r] = "L"
                        l += 1
                        r -= 1
                        # Central dominoes in uneven length chains do
                        # not get pushed.
                # Adjust the left pointer to the start of the next
                # sequence
                l = i + 1
            else:
                # Current domino is an "R"
                if dom[l] == "R":
                    for j in range(l, i):
                        dom[j] = "R"
                # Else do nothing, there was no right push.
                # Adjust the left pointer to the current "R"
                l = i
        # If the last right pushed didn't find a left pushed domino,
        # push all the dominoes to the right.
        if l < len(dominoes) and dominoes[l] == "R":
            for j in range(l + 1, len(dominoes)):
                dom[j] = "R"
        return "".join(dom)


# The dynamic programming solution stores the forces of the left and
# right pushes and adds them to decide if a domino falls right, left, or
# stands on its own.
#
# Time complexity: O(n) - We visit each domino twice.
# Space complexity: O(n) - The pushes array has the same length as the
# input string.
#
# Runtime: 430 ms, faster than 70.56%
# Memory Usage: 19.8 MB, less than 34.11%
class DP:
    def pushDominoes(self, dominoes: str) -> str:
        # Store the force of the pushes received by a single domino.
        push = [0] * len(dominoes)
        # Current push values.
        lp = rp = 0
        # Iterate over start and end simultaneously.
        for i in range(len(dominoes)):
            # Update the left and right pointers.
            l, r = i, -i - 1
            # Compute the right push from the left.
            # If the position contains an "R" reset to max push.
            if dominoes[l] == "R":
                rp = len(dominoes)
            # If the position contains an "L" reset to no push.
            elif dominoes[l] == "L":
                rp = 0
            # Otherwise, if there was a current push, reduce by 1.
            elif dominoes[l] == "." and rp > 0:
                rp -= 1
            # Add the computed push to the cumulative.
            push[l] += rp
            # Compute the left push from the right.
            # If the position contains an "L" reset to max push.
            if dominoes[r] == "L":
                lp = len(dominoes)
            # If the position contains an "R" reset to no push.
            elif dominoes[r] == "R":
                lp = 0
            # Otherwise, if there was a current push, reduce by 1.
            elif dominoes[r] == "." and lp > 0:
                lp -= 1
            # Subtract (left push) the computed push from the cumulative.
            push[r] -= lp
        # Iterate over the cumulative array, for each position, return
        # the value of where the domino fell.
        return "".join("." if p == 0 else "L" if p < 0 else "R" for p in push)


# This is a neat idea that I saw in the NeetCode YouTube channel at:
#
#
# We can look at the time, seconds they call them in the description, as
# the levels of a BFS algorithm, each second, nodes that are falling
# right or left get processed, we compute how they will affect their
# neighbors, and any neighbor that is caused to fall is added to the
# queue to be processed as part of the next level.
#
# Time complexity: O(n) - We iterate over all the nodes initially, to
# find which nodes we need to process. Once we start processing nodes,
# we visit each one a maximum of one time.
# Space complexity: O(n) - The queue that we use to process nodes, and
# the list that we use to store intermediate states, take, or can take
# up to, O(n)
#
# Runtime: 444 ms, faster than 68.93%
# Memory Usage: 18.4 MB, less than 53.04%
class BFS:
    def pushDominoes(self, dominoes: str) -> str:
        # Cast to a list to have a mutable data structure.
        dom = list(dominoes)
        # Create a double ended queue populated with the indices of all
        # nodes that are initially pushed.
        q = deque([i for i in range(len(dominoes)) if dominoes[i] != "."])
        # Keep processing nodes while we have moving dominoes.
        while q:
            # Process nodes left to right.
            idx = q.popleft()
            # This is the most complex case, we need to check if it will
            # push the node next to it.
            if dom[idx] == "R":
                # If the next domino is standing, check the one after.
                if idx + 1 < len(dom) and dom[idx + 1] == ".":
                    # If the one after is falling left, they will
                    # balance each other.
                    if idx + 2 < len(dom) and dom[idx + 2] == "L":
                        q.popleft()
                    # If the one after is not falling left, the next
                    # domino will be pushed right.
                    else:
                        q.append(idx + 1)
                        dom[idx + 1] = "R"
            # The left case is easier because we already handled the
            # contiguous R <=> L case.
            elif dom[idx] == "L" and idx > 0 and dom[idx - 1] == ".":
                dom[idx - 1] = "L"
                q.append(idx - 1)
        return "".join(dom)


def test():
    executors = [
        TwoPointers,
        DP,
        BFS,
    ]
    tests = [
        [".", "."],
        ["R", "R"],
        ["L", "L"],
        [".L", "LL"],
        ["R.", "RR"],
        [".R", ".R"],
        ["L.", "L."],
        ["RR.L", "RR.L"],
        ["....", "...."],
        ["..L.", "LLL."],
        ["..R.", "..RR"],
        ["RRRRRRL...", "RRRRRRL..."],
        [".L.R...LR.....", "LL.RR.LLRRRRRR"],
        ["...R...LR.....", "...RR.LLRRRRRR"],
        [".L.R...LR..L..", "LL.RR.LLRRLL.."],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.pushDominoes(t[0])
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
