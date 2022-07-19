# https://leetcode.com/problems/group-anagrams/

# Tags: Array - Hash Table - String - Sorting

import timeit
from typing import List


# Use the sorted strings as key for a hashmap that points to the insert position in the result list.
#
# Time complexity: O(n*m*log(m)) - n is the number of strings, m is the size of the strings.
# Space complexity: O(n) - we keep both a set and a list of the input size.
#
# Runtime: 155 ms, faster than 54.70% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.3 MB, less than 77.12% of Python3 online submissions for Group Anagrams.
class ListAndHashSet:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for s in strs:
            key = "".join(sorted(s))
            # If we have previously seen this anagram, add it to the anagram group
            if key in d:
                res[d[key]].append(s)
            else:
                res.append([s])
                d[key] = len(res) - 1
        return res


# Similar idea to above, but store the anagram groups in the dictionary and convert them to a list on the return.
#
# Time complexity: O(n*m*log(m)) - n is the number of strings, m is the size of the strings.
# Space complexity: O(n) - the hash set will grow to the size of the input matrix.
#
# Runtime: 146 ms, faster than 61.56% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.1 MB, less than 88.39% of Python3 online submissions for Group Anagrams.
class HashSet:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = "".join(sorted(s))
            # If we have previously seen this anagram, add it to the anagram group
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        return list(d.values())


def test():
    executors = [ListAndHashSet, HashSet]
    tests = [
        [
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ],
        [
            [""],
            [[""]],
        ],
        [
            ["a"],
            [["a"]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.groupAnagrams(t[0])
                exp = t[1]
                assert (
                    result.sort() == exp.sort()
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
