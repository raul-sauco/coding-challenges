# 692. Top K Frequent Words
# 🟠 Medium
#
# https://leetcode.com/problems/top-k-frequent-words/
#
# Tags: Hash Table - String - Trie - Sorting - Heap (Priority Queue) - Bucket Sort - Counting

import heapq
import timeit
from collections import Counter
from typing import List

# 1e4 calls:
# » Sort                0.07792   seconds
# » Heap                0.10584   seconds
# » Loop                0.10892   seconds

# Use Counter to get a dictionary of word frequencies, we can order them by frequency descending, then iterate over
# them, each time we find words that have the same frequency, we store them in an auxiliary list, when the next word
# has a lower frequency, we push the items in the auxiliary list into the result set sorted lexicographically.
# The outside loop is sorting the words by frequency decreasing, sorting the auxiliary list sorts words with the same
# frequency lexicographically.
#
# Time complexity: O(n+log(n)) - Sorting the counter by frequency, `counter.most_common()`
# Space complexity: O(n) - We store each item in memory, both in the counter dictionary and the result list.
#
# Runtime: 87 ms, faster than 53.03% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 14.1 MB, less than 27.16% of Python3 online submissions for Top K Frequent Words.
class Loop:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Get the frequencies.
        freq = Counter(words).most_common()
        # Prepare the result.
        result = []

        prev = ([freq[0][0]], freq[0][1])
        for current in freq[1:]:
            # If the previous top element and the current one had the same frequency, merge them.
            if current[1] == prev[1]:
                prev[0].append(current[0])
            # If the previous element and the current one had a different frequency, append the prev to the result.
            else:
                result += sorted(prev[0])
                # Reset the previous pointer.
                prev = ([current[0]], current[1])

            if len(result) > k:
                return result[:k]

        # Append the last element in the queue
        result += sorted(prev[0])

        return result[:k]


# We can rewrite the whole loop & conditional section above using the following lambda:
#
# key=lambda word: (-freq[word], word)
#
# Used inside the sorted() function, or the heapq.nsmallest() function, this lambda gets the keys in the
# frequencies dictionary and compares items based first on the frequency value `freq[word]` reversed, from
# more-frequent => less-frequent, then, when items have the same frequency, lexicographically.
#
# It is also possible to use the invert `~` operator to reverse sort by frequency: ~freq[word] but it turns
# out a bit slower, maybe because it reverses every bit of the frequency instead of only the most significant
# bit like `-` does.


# We can simplify the solution above sorting with a lambda that takes into account both requirements.
# For most people this should be the easiest to interpret solution and it is one of the top performers.
#
# Time complexity: O(n*log(n)) - The sorting step has the most complexity. There are some comments that
# say that this solution takes O(n*log(k)) but I don't see how that is possible because sorting is processing
# the whole list, we are only slicing after.
# Space complexity: O(n) - The dictionary could grow to the size of the input.
#
# Runtime: 51 ms, faster than 99.16% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 14 MB, less than 27.16% of Python3 online submissions for Top K Frequent Words.
class Sort:
    def topKFrequent(self, words, k):
        freq = Counter(words)
        return sorted(freq, key=lambda word: (-freq[word], word))[:k]

        # The same it is possible using list comprehension:
        # items = list(freq.items())
        # items.sort(key=lambda item: (-item[1], item[0]))
        # return [item[0] for item in items[0:k]]


# We can simplify even more the solution using a heap. Get the frequencies using Counter then use a heap to
# select the k top by frequency then lexicographically.
#
# Time complexity: O(n*log(k)) - We visit each word to get the frequencies, then heapify them in O(n) and get
# the k smallest in O(n*log(k)) time.
# Space complexity: O(n) - The frequencies dictionary.
#
# Runtime: 95 ms, faster than 40.83% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 13.9 MB, less than 64.86% of Python3 online submissions for Top K Frequent Words.
class Heap:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        return heapq.nsmallest(k, freq, key=lambda word: (-freq[word], word))
        # Use a heap, the line is equivalent to:
        # return sorted(freq, key=lambda word: (~freq[word], word))[:k]


def test():
    executors = [
        Sort,
        Heap,
        Loop,
    ]
    tests = [
        [["i", "love", "leetcode", "i", "love", "coding"], 3, ["i", "love", "coding"]],
        [["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]],
        [["love", "leetcode", "i", "love", "coding", "i"], 2, ["i", "love"]],
        [["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4, ["the", "is", "sunny", "day"]],
        [
            ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is", "is"],
            4,
            ["is", "the", "sunny", "day"],
        ],
        [
            ["the", "is", "day", "sunny", "the", "the", "is", "is", "sunny", "day", "day", "sunny"],
            4,
            ["day", "is", "sunny", "the"],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.topKFrequent(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
