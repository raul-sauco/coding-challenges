# 1461. Check If a String Contains All Binary Codes of Size K
# 🟠 Medium
#
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
#
# Tags: Hash Table - String - Bit Manipulation - Rolling Hash - Hash Function


import timeit


# Use a sliding window of size k to find all substrings of size k in s,
# add them to a set to ignore duplicates, then compare the number of
# substrings in s with the total possible number of codes of length k.
#
# Time complexity: O(n^2) - With n the length of the string. We iterate
# over len(s) - k+1 windows, for each we slice the string s at a cost n.
# Space complexity: O(n) - The set can grow to the size of the input.
#
# Runtime: 422 ms, faster than 96.90%
# Memory Usage: 27.2 MB, less than 91.11%
class CombinationSet:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Define a set to store all possible combinations of length k
        # that we can find in s.
        found = set()
        # Sliding window of size k over s saving all combinations found
        # into the set to ignore duplicates.
        for i in range(len(s) - k + 1):
            # Add the combination found to the set.
            found.add(s[i : i + k])
        # The total combinations that exist of length k is 2^k, check if
        # that is the number of combinations that we found in s, if
        # s contains fewer combinations, it does not contain all the
        # possible ones and we can return False.
        return len(found) == 1 << k


# Same as the previous solution but use set comprehension to find the
# existing sequences.
#
# Time complexity: O(n^2) - With n the length of the string. We iterate
# over len(s) - k+1 windows, for each we slice the string s at a cost n.
# Space complexity: O(n) - The set can grow to the size of the input.
#
# Runtime: 555 ms, faster than 78.00%
# Memory Usage: 51.3 MB, less than 41.19%
class SetComprehension:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[i - k : i] for i in range(k, len(s) + 1)}) == 1 << k


# Similar to the previous solution but use memoryview to avoid the O(n)
# cost of slicing the input string s in each iteration of the loop.
#
# Time complexity: O(n*k) - With n the length of the string s and k the
# cost of hashing substrings of length k to add them to the set O(1)?
# Space complexity: O(n) - The set can grow to the size of the input.
#
# Runtime: 422 ms, faster than 96.90%
# Memory Usage: 27.2 MB, less than 91.11%
class MemoryView:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Define a set to store all possible combinations of length k
        # that we can find in s.
        found = set()
        # Sliding window of size k over s saving all combinations found
        # into the set to ignore duplicates.
        # Use memory view to avoid O(s) slicing.
        mem_str = memoryview(bytes(s, encoding="utf8"))
        for i in range(len(s) - k + 1):
            # Add the combination found to the set.
            found.add(mem_str[i : i + k])
        # The total combinations that exist of length k is 2^k, check if
        # that is the number of combinations that we found in s, if
        # s contains fewer combinations, it does not contain all the
        # possible ones and we can return False.
        return len(found) == 1 << k


# Eliminate the need to hash the sequences found by using a list keyed
# by the actual binary sequence instead of a set.
#
# Time complexity: O(n) - The sliding window moves once for each len(s)
# -k+1. But this time, for each we save to the list in O(1).
# Space complexity: O(2^k) - The number of sequences == the length of
# the got list.
#
# Runtime: 755 ms, faster than 47.54%
# Memory Usage: 22.4 MB, less than 95.06%
class RollingHash:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # We need to find all the possible sequences of length k == 2^k.
        need = 1 << k
        # The equivalent of the found set in the previous solutions.
        got = [False] * need
        # The highest value sequence that we can have.
        all_one = need - 1
        # Initialize the rolling hash to all 0.
        hash_val = 0

        for i in range(len(s)):
            # Calculate hash for s[i-k+1:i+1] by adding s[i] to the
            # rolling hash.
            hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
            # Check only once the sliding window is of size k and only
            # register a new sequence when we haven't seen it before.
            if i >= k - 1 and got[hash_val] is False:
                # Mark the sequence as seen.
                got[hash_val] = True
                # We need to find one less sequence.
                need -= 1
                if need == 0:
                    return True
        # If we haven't found all the sequences needed, return false.
        return False


def test():
    executors = [
        CombinationSet,
        SetComprehension,
        MemoryView,
        RollingHash,
    ]
    tests = [
        ["00110110", 2, True],
        ["00110", 2, True],
        ["100", 2, False],
        ["0110", 2, False],
        ["0110", 1, True],
        ["00110110", 1, True],
        ["00110110", 4, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.hasAllCodes(t[0], t[1])
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
