# 659. Split Array into Consecutive Subsequences
# 🟠 Medium
#
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
#
# Tags: Array - Hash Table - Greedy - Heap (Priority Queue)

import timeit
from collections import Counter, defaultdict
from typing import List


# Keep two dictionaries, one with the elements that we haven't placed
# into a sequence yet, another weth the end of sequences that we have
# built already, and can append to. Iterate over the input, first
# trying to place the elements into an existing sequence, then, if not
# possible, trying to build a sequence with the element that we are
# visiting and the two next ones. If both these are not possible, we
# cannot use the current element in any sequence and we can return
# false.
#
# Time complexity: O(n) - We visit each element once and decide where to
# place it or return false.
# Space complexity: O(n) - The counter and the dictionary will grow
# linearly with the size of the input.
#
# Runtime: 567 ms, faster than 91.07%
# Memory Usage: 15.4 MB, less than 25.22%
class Greedy:
    def isPossible(self, nums: List[int]) -> bool:
        # Get a count of elements that are available to us and need to
        # be placed in sequences.
        freq = Counter(nums)
        end = defaultdict(int)
        # Iterate over the input ot greedily start building sequences of
        # length >= 3.
        for num in nums:
            # Check if we have already used this element to build a
            # sequence with a previous element. In that case continue.
            if not freq[num]:
                continue
            # We have to place this element, we will either succeed or
            # fail and return false, in either case, we can subtract 1
            # to the count of this number.
            freq[num] -= 1
            # If we can append this element to the end of an existing
            # sequence, do it and adjust the key on the "end of
            # sequences" dictionary.
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            # If we could not append the current element to the end of
            # an existing sequence, check if it is possible to create
            # a sequence with this element and the following 2, they
            # need to be consecutive integers.
            elif freq[num + 1] and freq[num + 2]:
                # If we can create a new sequence, update both
                # dictionaries by removing the next two integers from
                # the frequency list.
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                # And creating a new entry in the sequences dictionary
                # with the last element as the key.
                end[num + 2] += 1
            # If we cannot place the element into an existing sequence
            # or create a new sequence of length 3, return false now.
            else:
                return False
        # If we could place all elements into a sequence, return true.
        return True


# We can optimize the previous solution checking the minimum number of
# sequences we will have to obtain, equal to the frequency of the most
# frequent element in the input. If we don't have enough elements to
# split into that many sequences of minimum 3, we can return false.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(n) - The counter and the dictionary.
#
# I expected the optimization to make the code faster, instead it runs
# slower in the tests but uses less memory, which was unexpected.
#
# Runtime: 989 ms, faster than 28.37%
# Memory Usage: 15.2 MB, less than 95.45%
class OptimizedGreedy:
    def isPossible(self, nums: List[int]) -> bool:
        # We need a minimum of k sequences where k is the frequency of
        # the most frequent element.
        count = Counter(nums)
        min_sequences = count.most_common(1)[0][1]
        # If we don't have enough elements to form min_sequences of 3
        # return False already.
        if len(nums) / min_sequences < 3:
            return False
        # Greedily start building sequences of min_sequence length.
        end = defaultdict(int)
        for num in nums:
            if not count[num]:
                continue
            count[num] -= 1
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            elif count[num + 1] and count[num + 2]:
                count[num + 1] -= 1
                count[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False
        return True


def test():
    executors = [
        Greedy,
        OptimizedGreedy,
    ]
    tests = [
        [[1, 2, 3, 3, 4, 5], True],
        [[1, 2, 3, 3, 4, 4, 5, 5], True],
        [[1, 2, 3, 4, 4, 5], False],
        [[1, 2, 3, 4, 4, 5, 6, 8, 9, 10], True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.isPossible(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
