# https://leetcode.com/problems/maximum-units-on-a-truck/


import timeit
from typing import List

# Runtime: 238 ms, faster than 50.64% of Python3 online submissions for Maximum Units on a Truck.
# Memory Usage: 14.4 MB, less than 83.07 % of Python3 online submissions for Maximum Units on a Truck.


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort by units per box to maximize the units of the boxes we pick
        boxTypes.sort(key=lambda x: (x[1]), reverse=True)
        remaining_space, units_loaded = truckSize, 0
        for boxes_of_type, units_per_box in boxTypes:
            # Add as many as possible of the current type
            can_load = min(boxes_of_type, remaining_space)
            remaining_space -= can_load
            units_loaded += can_load * units_per_box
            if remaining_space == 0:
                break
        return units_loaded


def test():
    executor = [
        {'executor': Solution, 'title': 'Solution', },
    ]
    tests = [
        [[[1, 3], [2, 2], [3, 1]], 4, 8],
        [[[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for t in tests:
                sol = e['executor']()
                result = sol.maximumUnits(t[0], t[1])
                expected = t[2]
                assert result == expected, f'{result} != {expected} for {t[0]}:{t[1]} using {e["title"]} solution'
        used = str(round(timeit.default_timer() - start, 5))
        result = "{0:20}{1:10}{2:10}".format(e['title'], used, "seconds")
        print(f"\033[92m» {result}\033[0m")


test()
