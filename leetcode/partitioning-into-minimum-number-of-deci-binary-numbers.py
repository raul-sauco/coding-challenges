# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/


import timeit


# Runtime: 107 ms, faster than 61.41% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
# Memory Usage: 14.6 MB, less than 83.98 % of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
class Max:
    def minPartitions(self, n: str) -> int:
        return max(n)


# We need as many '1's as the largest single digit in the input
#
# Runtime: 394 ms, faster than 14.17% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
# Memory Usage: 16.3 MB, less than 7.08 % of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
class ListComprehension:
    def minPartitions(self, n: str) -> int:
        return max([int(i) for i in n])


def test():
    executor = [
        {'executor': Max, 'title': 'Max', },
        {'executor': ListComprehension, 'title': 'ListComprehension', },
    ]
    tests = [
        ["32", 3],
        ["82734", 8],
        ["27346209830709182346", 9],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = e['executor']()
                result = int(sol.minPartitions(t[0]))
                expected = t[1]
                assert result == expected, f'{result} != {expected} for {t[0]} using {e["title"]} solution'
        used = str(round(timeit.default_timer() - start, 5))
        result = "{0:20}{1:10}{2:10}".format(e['title'], used, "seconds")
        print(f"\033[92m» {result}\033[0m")


test()
