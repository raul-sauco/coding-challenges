# 649. Dota2 Senate
# 🟠 Medium
#
# https://leetcode.com/problems/dota2-senate/
#
# Tags: String - Greedy - Queue

import timeit
from collections import Counter, deque


# Use two queues, one for each group of senators, store their index in
# the queues, for each vote, check who is the next senator that has the
# right to vote, that senator will greedily ban the first senator in the
# other group that can vote, then will move themselves to the end of its
# group's queue.
#
# Time complexity: O(n) - The maximum number of times the senators can
# vote, which is the same as the number of times the while loop will
# run, is equal to the number of senators, each round half the senators
# get to vote and remove half of the remaining ones.
# Space complexity: O(n) - The size of the queues.
#
# Runtime 72 ms Beats 45.87%
# Memory 16.8 MB Beats 5.50%
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d, r = deque(), deque()
        for i, member in enumerate(senate):
            if member == "D":
                d.append(i)
            else:
                r.append(i)
        # Each senator will ban the first senator of the opposite party
        # that can vote to prevent them from voting.
        next_idx = 0
        while d and r:
            # Reset the index for the next round.
            if next_idx > d[0] and next_idx > r[0]:
                next_idx = 0
            if next_idx > d[0]:
                d.popleft()
                r.append(r.popleft())
                next_idx = r[-1] + 1
                continue
            if next_idx > r[0]:
                r.popleft()
                d.append(d.popleft())
                next_idx = d[-1] + 1
                continue
            # Both indexes have not voted this round yet.
            if d[0] < r[0]:
                r.popleft()
                d.append(d.popleft())
                next_idx = d[-1] + 1
            else:
                d.popleft()
                r.append(r.popleft())
                next_idx = r[-1] + 1

        return "Dire" if d else "Radiant"


# Use a single queue, keep track of the number of banned senators from
# each group. Pop the next senator in the queue, if it belongs to a
# group that has banned senators, remove it from the queue and continue,
# otherwise, add it to the back of the queue and increase the number of
# banned senators from the opposing group.
#
# Time complexity: O(n) - The maximum number of times the senators can
# vote, which is the same as the number of times the while loop will
# run, is equal to the number of senators, each round half the senators
# get to vote and remove half of the remaining ones.
# Space complexity: O(n) - The size of the queue.
#
# Runtime 70 ms Beats 48.62%
# Memory 16.4 MB Beats 11.62%
class Solution2:
    def predictPartyVictory(self, senate: str) -> str:
        cd, cr = 0, 0
        for s in senate:
            if s == "D":
                cd += 1
            else:
                cr += 1
        q = deque(senate)
        bd, br = 0, 0
        while cd and cr:
            s = q.popleft()
            if s == "D":
                # Was this senator banned by a previous one?
                if bd > 0:
                    bd -= 1
                    cd -= 1
                    continue
                # If not banned, move it to the end and ban a Radiant.
                q.append(s)
                br += 1
            else:
                if br > 0:
                    br -= 1
                    cr -= 1
                    continue
                q.append(s)
                bd += 1

        return "Dire" if cd else "Radiant"


# Use a single queue, keep track of the number of banned senators from
# each group. Pop the next senator in the queue, if it belongs to a
# group that has banned senators, remove it from the queue and continue,
# otherwise, add it to the back of the queue and increase the number of
# banned senators from the opposing group.
#
# Time complexity: O(n) - The maximum number of times the senators can
# vote, which is the same as the number of times the while loop will
# run, is equal to the number of senators, each round half the senators
# get to vote and remove half of the remaining ones.
# Space complexity: O(n) - The size of the queue.
#
# Runtime 87 ms Beats 33.64%
# Memory 16.4 MB Beats 11.62%
class Solution3:
    def predictPartyVictory(self, senate: str) -> str:
        c, q = Counter(senate), deque(senate)
        b = {"R": 0, "D": 0}
        while c["D"] and c["R"]:
            s = q.popleft()
            if b[s] > 0:
                b[s] -= 1
                c[s] -= 1
            else:
                q.append(s)
                b["D" if s == "R" else "R"] += 1
        return "Dire" if c["D"] else "Radiant"


def test():
    executors = [
        Solution,
        Solution2,
        Solution3,
    ]
    tests = [
        ["DR", "Dire"],
        ["RDD", "Dire"],
        ["RD", "Radiant"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.predictPartyVictory(t[0])
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
