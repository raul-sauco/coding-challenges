# 49. Group Anagrams
# 🟠 Medium
#
# https://leetcode.com/problems/group-anagrams/
#
# Tags: Array - Hash Table - String - Sorting


import timeit
from collections import defaultdict
from typing import List


# Use the sorted strings as key for a hashmap that points to the insert
# position in the result list.
#
# Time complexity: O(n*m*log(m)) - n is the number of strings, m is the
# size of the strings.
# Space complexity: O(n) - We keep both a set and a list of the same
# size as the input.
#
# Runtime: 155 ms, faster than 54.70%
# Memory Usage: 17.3 MB, less than 77.12%
class ListAndHashSet:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for s in strs:
            key = "".join(sorted(s))
            # If we have previously seen this anagram, add it to the
            # anagram group.
            if key in d:
                res[d[key]].append(s)
            else:
                res.append([s])
                d[key] = len(res) - 1
        return res


# Similar idea to above, but store the anagram groups in the dictionary
# and convert them to a list on the return.
#
# Time complexity: O(n*m*log(m)) - n is the number of strings, m is the
# size of the strings.
# Space complexity: O(n) - the hash set will grow to the size of the
# input matrix.
#
# Runtime: 146 ms, faster than 61.56%
# Memory Usage: 17.1 MB, less than 88.39%
class HashSet:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = "".join(sorted(s))
            # If we have previously seen this anagram, add it to the
            # anagram group.
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        return list(d.values())


# Similar to the previous solution but use a defaultdict(list) to avoid
# having to check if the entry exists.
#
# Time complexity: O(n*m*log(m)) - n is the number of strings, m is the
# size of the strings.
# Space complexity: O(n) - the hash set will grow to the size of the
# input matrix.
#
# Runtime: 229 ms, faster than 44.05%
# Memory Usage: 17.3 MB, less than 80.07%
class UseDefaultDict:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups["".join(sorted(s))].append(s)
        return list(groups.values())


def test():
    executors = [
        ListAndHashSet,
        HashSet,
        UseDefaultDict,
    ]
    tests = [
        [[""], [[""]]],
        [["a"], [["a"]]],
        [
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.groupAnagrams(t[0])
                exp = t[1]
                # We can return the result in any order. Sort to compare.
                result = sorted(map(sorted, result))
                exp.sort()
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
