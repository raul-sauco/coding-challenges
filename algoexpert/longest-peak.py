# Longest Peak
# 🟠 Medium
#
# https://www.algoexpert.io/questions/longest-peak
#
# Tags: Array

import timeit


# Use states to determine in which state we are and which possible
# changes can happen.
#
# Time complexity: O(n) - Linear time.
# Space complexity: O(1) - Constant space.
class DFA:
    def longestPeak(self, array):
        if not array:
            return 0
        # Use a finite state machine, true is going up, false coming down.
        up = True
        # How many integers in the peak.
        count, res, last = 0, 0, array[0]
        for val in array:
            # Building the upward slope.
            if up:
                # An equal value breaks the streak without being a peak.
                if val == last:
                    count = 1
                    up = True
                elif val > last:
                    count += 1
                # If we already have an upward slope and have a peak.
                elif count > 1:
                    up = False
                    count += 1

            # We are on the downward slope.
            else:
                if val >= last:
                    # An greater or equal value completes the peak.
                    res = max(res, count)
                    count = 1 if val == last else 2
                    up = True
                else:
                    count += 1
            last = val
        if not up:
            res = max(res, count)
        return res if res >= 3 else 0


# Iterate over the array positions checking if they could be the peak of
# a section of length >= 3. When we find any position that could be a
# peak, we check left and right to see how many elements form the peak
# and return the length of the longest one found.
#
# Time complexity: O(n) - Linear time, positions will be assessed one or
# two times.
# Space complexity: O(1) - Constant space.
class PeakFinder:
    def longestPeak(self, array):
        i, res = 1, 0
        while i < len(array) - 1:
            if not array[i - 1] < array[i] > array[i + 1]:
                i += 1
                continue
            l, r = i - 1, i + 1
            while l > 0 and array[l - 1] < array[l]:
                l -= 1
            while r < len(array) - 1 and array[r] > array[r + 1]:
                r += 1
            res = max(res, r - l + 1)
            i += 1
        return res


def test():
    executors = [
        DFA,
        PeakFinder,
    ]
    tests = [
        [[], 0],
        [[1, 3, 2], 3],
        [[1, 2, 3, 4, 5, 1], 6],
        [[5, 4, 3, 2, 1, 2, 1], 3],
        [[5, 4, 3, 2, 1, 2, 10, 12], 0],
        [[1, 2, 3, 4, 5, 6, 10, 100, 1000], 0],
        [[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3], 6],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.longestPeak(t[0])
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
