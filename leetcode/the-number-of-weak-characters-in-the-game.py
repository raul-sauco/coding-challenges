# 1996. The Number of Weak Characters in the Game
# 🟠 Medium
#
# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
#
# Tags: Array - Stack - Greedy - Sorting - Monotonic Stack

import timeit
from typing import List

# The brute force solution would iterate over the entire array and, for
# each element, it would check the rest of the elements checking how
# many of them are weaker. O(n^2)

# If we sort the characters in decreasing order of their attack property,
# and then iterate over the sorted input keeping track of the highest
# defense value that we have seen for each attack value, we can then
# iterate over the characters and compare them with the best defense
# value of each attack value higher than theirs. Any character that has
# a lower defense value will be a weak character.
#
# Time complexity: O(n*log(n)) - The highest cost comes from sorting,
# then we can iterate the array in O(n).
# Space complexity: O(m) - Where m is the number of different attack
# values in the input.
#
# Runtime: 3805 ms, faster than 34.62%
# Memory Usage: 66.7 MB, less than 90.86%
class MonotonicStack:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Sort the input by the attack value. O(n*log(n)).
        properties.sort(reverse=True)
        # Store the strong characters in a monotonic stack, we only want
        # to keep the strongest defense value for each representation of
        # the attack values.
        stack = [properties[0]]
        # Store the number of weak characters.
        weak = 0
        # Iterate over the rest of the input comparing characters with
        # the top of the stack.
        for attack, defense in properties[1:]:
            last = stack[-1]
            # If we have moved to the next attack value:
            if attack < last[0]:
                # If defense is also smaller.
                if defense < last[1]:
                    weak += 1
                # This is the strongest defense for its attack level.
                elif defense > last[1]:
                    stack.append([attack, defense])
                # Same defense value as the last, ignore it.
            # Attack values are the same, go up the stack trying to find
            # a character with both values higher.
            else:
                for idx in range(len(stack) - 1, -1, -1):
                    # Explore this strong candidate's values.
                    candidate = stack[idx]
                    # If the current character is weaker than this
                    # candidate, no need to keep exploring.
                    if candidate[0] > attack and candidate[1] > defense:
                        weak += 1
                        break
        # Return the number of weak characters.
        return weak


# TODO: Redo this problem, easier to read and understand solutions exist.


def test():
    executors = [MonotonicStack]
    tests = [
        [[[2, 2], [3, 3]], 1],
        [[[5, 5], [6, 3], [3, 6]], 0],
        [[[1, 5], [10, 4], [4, 3]], 1],
        [[[1, 1], [2, 1], [2, 2], [1, 2]], 1],
        [[[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]], 2],
        [[[2, 5], [2, 4], [1, 1], [2, 1], [2, 2], [1, 2], [2, 3]], 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numberOfWeakCharacters(t[0])
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
