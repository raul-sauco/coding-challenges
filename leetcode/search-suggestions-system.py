# https://leetcode.com/problems/search-suggestions-system/


import bisect
import timeit
from typing import List

# Solution using bisect, easy to read and performant
#
# Runtime: 92 ms, faster than 90.74% of Python3 online submissions for Search Suggestions System.
# Memory Usage: 17.1 MB, less than 84.09 % of Python3 online submissions for Search Suggestions System.


class BisectSolution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""
        start = 0
        end = len(products)
        for i in range(len(searchWord)):
            prefix += searchWord[i]
            start = bisect.bisect_left(products, prefix, lo=start, hi=end)
            end = bisect.bisect_right(
                products, prefix + '\xff\xff\xff\xff', lo=start, hi=end)
            result.append(products[start:min(start + 3, end)])
        return result


# Solution using two pointers from neetcode.com
# Runtime: 97 ms, faster than 88.41% of Python3 online submissions for Search Suggestions System.
# Memory Usage: 17.1 MB, less than 84.12 % of Python3 online submissions for Search Suggestions System.
class NeetCodeSolution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        # Sort the products array O(n*log(n))
        products.sort()
        l, r = 0, len(products)-1
        # Simulate one complete search per each character of the search word
        for i in range(len(searchWord)):
            c = searchWord[i]
            # Move forward the left pointer while:
            # - There is still room between the start and end
            # - The word at position `left` is not shorter than searchWord
            # - The word does not match the search term
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            # Move back the right pointer while:
            # - There is still room between the start and end
            # - The word at position `right` is not shorter than searchWord
            # - The word does not match the search term
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1

            # Create a new empty result array
            res.append([])
            # Calculate the number of results remaining
            remain = r - l + 1
            # Iterate over the remaining words adding them to the result set. Limit to 3 if there are more results
            for j in range(min(3, remain)):
                res[-1].append(products[l + j])
        return res


# Solution using a trie and with code organized in different functions.
# Easy to read and maintain but not performant.
#
# Runtime: 919 ms, faster than 20.06% of Python3 online submissions for Search Suggestions System.
# Memory Usage: 22.8 MB, less than 12.51% of Python3 online submissions for Search Suggestions System.
class TrieSolution:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        current['?'] = True

    def exploreNode(self, node: dict, results, term: str) -> List[str]:
        if '?' in node:
            results.append(term)
            # If we have the required 3 terms, return them
        if len(results) == 3:
            return results
        keys = sorted(node.keys())
        for k in keys:
            if k != "?" and len(results) < 3:
                # term = term + k
                self.exploreNode(node[k], results, term + k)
        return results

    def fetchResults(self, prefix: str) -> List[str]:
        results = []
        current = self.root
        # First navigate the existing prefix
        for w in prefix:
            if w not in current:
                # The prefix is not in the trie.
                return []
            current = current[w]
        # Explore the branches starting with minimum weight
        return self.exploreNode(current, results, prefix)

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        for product in products:
            self.insert(product)
        results = []
        for i in range(len(searchWord)):
            batch = self.fetchResults(searchWord[:i+1])
            results.append(batch)
        return results


def test():
    tested = [
        {'executor': BisectSolution, 'title': 'Bisect Solution', },
        {'executor': NeetCodeSolution, 'title': 'NeetCode Solution', },
        {'executor': TrieSolution, 'title': 'Trie Solution', },
    ]
    tests = [
        {
            'products': ["mobile", "mouse", "moneypot", "monitor", "mousepad", "bar"],
            'searchWord': "mouse",
            'expected':[
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        },
        {
            'products': ["havana"],
            'searchWord': "havana",
            'expected':[["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]],
        },
        {
            'products': ["bags", "baggage", "banner", "box", "cloths"],
            'searchWord': "bags",
            'expected':[
                ["baggage", "bags", "banner"],
                ["baggage", "bags", "banner"],
                ["baggage", "bags"], ["bags"],
            ],
        },
        {
            'products': ["bags", "baggage", "banner", "box", "cloths"],
            'searchWord': "maniac",
            'expected':[[], [], [], [], [], []],
        },
    ]
    for e in tested:
        start = timeit.default_timer()
        for _ in range(100000):
            for t in tests:
                sol = e['executor']()
                result = sol.suggestedProducts(t['products'], t['searchWord'])
                expected = t["expected"]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
