# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map = {rest: idx for idx, rest in enumerate(list1)}
        results = []
        min_idx_sum = float('inf')
        for i, el in enumerate(list2):
            # O1
            if el in hash_map:
                # Store the common element with the sum of its indexes in both lists
                rate = i + hash_map[el]
                if rate < min_idx_sum:
                    min_idx_sum = rate
                    # Replace list with a new list with only this item
                    results = [el]
                elif rate == min_idx_sum:
                    results.append(el)

        return results

    # Nice way of constructing the dictionaries
    # https://leetcode.com/problems/minimum-index-sum-of-two-lists/discuss/534789/Python3-148ms-94.77-Hashmap
    def findRestaurantAlt(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {restaurant: i for i, restaurant in enumerate(list1)}
        dic2 = {restaurant: dic1[restaurant]+i for i,
                restaurant in enumerate(list2) if restaurant in dic1}

        MIN = float('inf')
        res = []

        for key, val in dic2.items():
            if val < MIN:
                res = [key]
                MIN = val
            elif val == MIN:
                res.append(key)

        return res


tests = [
    [["Shogun", "Tapioca Express", "Burger King", "KFC"], [
        "Plaza", "The Grill at Torres Pines", "Hungry Hunter Steakhouse", "Shogun"], ["Shogun"]],
    [["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"], ["Shogun"]],
    [['th', ' '], ['ht', 'next', 'grc', ' ', 'record'], [' ']],
]


def test():
    sol = Solution()
    for t in tests:
        result = sol.findRestaurant(t[0], t[1])
        assert result == t[2], f'{result} != {t[2]}'
        result_alt = sol.findRestaurantAlt(t[0], t[1])
        assert result_alt == t[2],  f'{result_alt} != {t[2]}'


test()
