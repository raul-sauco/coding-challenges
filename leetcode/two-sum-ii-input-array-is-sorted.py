# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Interesting solutions here:
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search).


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Recursive approach
        def ts(i: int, start: int, end: int, numbers: List[int], target: int):
            mid = start + (start-end)//2
            sum = numbers[i] + numbers[mid]
            if sum == target:
                return [i+1, mid+1]
            # Detect when we are running out of 'j's to try
            if end - start == 1:
                # Only two elements left, we haven't checked "end"
                if numbers[i] + numbers[end] == target:
                    return [i+1, end+1]
                # If end does not match, we have no match for the current i, move to the next one
                return ts(i+1, i+2, len(numbers)-1, numbers, target)
            if sum < target:
                return ts(i, mid, end, numbers, target)
            return ts(i, start, mid, numbers, target)

        # First call with 0, (1+len(numbers))/2
        return ts(0, 1, len(numbers)-1, numbers, target)

    # Best solution, On
    def twoSumWithTwoPointers(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1


def test():
    sol = Solution()
    tests = [
        {
            'input': [2, 7, 11, 15],
            'target': 9,
            'output': [1, 2],
        },
        {
            'input': [2, 3, 4],
            'target': 6,
            'output': [1, 3],
        },
        {
            'input': [-1, 0],
            'target': -1,
            'output': [1, 2],
        },
    ]
    for t in tests:
        print('')
        result = sol.twoSum(t['input'], t['target'])
        expected = t['output']
        assert result == expected, f'{expected} does not match {result}'


test()
