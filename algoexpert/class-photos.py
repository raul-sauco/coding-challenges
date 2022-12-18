# Class Photos
# 🟢 Easy
#
# https://www.algoexpert.io/questions/class-photos
#
# Tags: Array - Greedy

import timeit


# Sort both arrays, the taller student for each position should be in
# the same array, either blue or red.
#
# Time complexity: O(n*log(n)) - Sorting has the highest time complexity.
# Space complexity: O(n) - Sorting in python takes up to n/2.
class Solution:
    def classPhotos(self, redShirtHeights, blueShirtHeights):
        redShirtHeights.sort()
        blueShirtHeights.sort()
        if redShirtHeights[0] > blueShirtHeights[0]:
            taller, shorter = redShirtHeights, blueShirtHeights
        else:
            taller, shorter = blueShirtHeights, redShirtHeights
        return all([taller[i] - shorter[i] > 0 for i in range(len(taller))])
        # Optionally, we could use a loop.
        # for i in range(len(taller)):
        #     if shorter[i] >= taller[i]:
        #         return False
        # return True


def test():
    executors = [Solution]
    tests = [
        [[5, 8, 1, 3, 4], [6, 9, 2, 4, 5], True],
        [[7, 8, 1, 3, 4], [6, 9, 2, 4, 5], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.classPhotos(t[0], t[1])
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
