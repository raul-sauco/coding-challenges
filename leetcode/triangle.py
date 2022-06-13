# https://leetcode.com/problems/triangle/


from typing import List


class Solution:
    # Reverse solution reads better
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for y in range(len(triangle) - 2, -1, -1):
            for x in range(y+1):
                triangle[y][x] += min(triangle[y+1][x], triangle[y+1][x+1])
        return triangle[0][0]

    def minimumTotalWithExtraArray(self, triangle: List[List[int]]) -> int:
        sums = [0]*(len(triangle)+1)

        for row in triangle[::-1]:
            for i in range(len(row)):
                sums[i] = min(sums[i], sums[i+1]) + row[i]

        return sums[0]

    def minimumTotalTopToBottom(self, triangle: List[List[int]]) -> int:
        # Create an array to hold the solutions and initialize it with the top vertex
        sums = [triangle[0][0]]

        for row in range(1, len(triangle)):
            for idx, el in enumerate(triangle[row]):
                if idx == 0:
                    # Store the value of columns for the current row
                    prev = sums[idx]
                    # It can only be the sum of the previous idx[0] elements
                    sums[idx] += el
                elif idx == len(sums):
                    # It can only be the sum of the current and the last element of previous sum
                    sums.append(el + prev)
                else:
                    p = prev
                    prev = sums[idx]
                    # Choose the shortest path to get to this node between the two possible ones
                    sums[idx] = el + min(p, sums[idx])

        return min(sums)


def test():
    s = Solution()
    assert s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert s.minimumTotal([[-1]]) == -1
    assert s.minimumTotal([[-10]]) == -10
    assert s.minimumTotal([[-1], [2, 3]]) == 1


test()
