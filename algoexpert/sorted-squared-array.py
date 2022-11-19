# Sorted Squared Array
# 🟢 Easy
#
# https://www.algoexpert.io/questions/sorted-squared-array
#
# Tags: Array - Sorting

import timeit

# Even though the theoretical complexity of the second
# solution is better, the first one is faster, probably due to list
# comprehension being implemented in C.
# 10_000 calls.
# » Sorting             0.04455   seconds
# » Linear              0.06414   seconds

# Use list comprehension and the sorted function to obtain the square
# of all elements in the input and then sort them.
#
# Time complexity: O(n*log(n)) - Sorting has the highest complexity.
# Space complexity: O(n)
class Sorting:
    def sortedSquaredArray(self, array):
        return sorted([n**2 for n in array])


# Avoid the costly sorting step keeping a pointer to the start and
# another to the end of the input array and processing elements that
# will result in bigger squares before elements that will result in
# smaller squares, then adding them to the result array from the tail.
#
# Time complexity: O(n)
# Space complexity: O(n)
class Linear:
    def sortedSquaredArray(self, array):
        res = [None] * len(array)
        l, r = 0, len(array) - 1
        sqr_l, sqr_r = array[l] ** 2, array[r] ** 2
        for i in reversed(range(len(res))):
            if sqr_l > sqr_r:
                res[i] = sqr_l
                l += 1
                sqr_l = array[l] ** 2
            else:
                res[i] = sqr_r
                r -= 1
                sqr_r = array[r] ** 2
        return res


def test():
    executors = [
        Sorting,
        Linear,
    ]
    tests = [
        [[-5, -4, -3, -2, -1], [1, 4, 9, 16, 25]],
        [[-7, -3, 1, 9, 22, 30], [1, 9, 49, 81, 484, 900]],
        [[1, 2, 3, 5, 6, 8, 9], [1, 4, 9, 25, 36, 64, 81]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.sortedSquaredArray(t[0])
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
