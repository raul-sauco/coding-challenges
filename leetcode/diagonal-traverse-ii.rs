// 1424. Diagonal Traverse II
// 🟠 Medium
//
// https://leetcode.com/problems/diagonal-traverse-ii/
//
// Tags: Array - Sorting - Heap (Priority Queue)

use std::collections::VecDeque;

struct Solution;
impl Solution {
    /// If we reverse the rows in the input and add them one by one popping the first element and
    /// adding it to the result before we add it to a rotative queue that points to the row from
    /// which the next element needs to come, we can keep popping the last element of the vector at
    /// which that queue points and adding them to the result.
    ///
    /// Time complexity: O(m*n) - We visit each element in the input once.
    /// Space complexity: O(m*n) - We make a local copy of the input 2D vector.
    ///
    /// Runtime 36 ms Beats 75%
    /// Memory 5.54 MB Beats 100%
    pub fn find_diagonal_order(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let mut nums = nums
            .into_iter()
            .map(|mut v| {
                v.reverse();
                v
            })
            .collect::<Vec<_>>();
        // A vector with the indexes of the next vector from nums from which we have to pop.
        let mut idxs: VecDeque<usize> = VecDeque::new();
        // A pointer to the next vector in nums that we have not used yet.
        let mut next_idx = 0;
        let mut res = vec![];
        while next_idx < n || !idxs.is_empty() {
            if next_idx < n {
                // Each row is guaranteed to have, at least, one element.
                res.push(nums[next_idx].pop().unwrap());
            }
            // Now pop from all rows that are not empty.
            for _ in 0..idxs.len() {
                let i = idxs.pop_front().unwrap();
                res.push(nums[i].pop().unwrap());
                if !nums[i].is_empty() {
                    idxs.push_back(i);
                }
            }
            if next_idx < n {
                if !nums[next_idx].is_empty() {
                    idxs.push_front(next_idx);
                }
                next_idx += 1;
            }
        }
        res
    }

    /// Use a BFS approach, start at the top-left corner, when we visit a cell, add its neighbors
    /// to the queue and its value to the result. Simpler approach than the previous one.
    ///
    /// Time complexity: O(m*n) - We visit each element in the input once.
    /// Space complexity: O(√n) - The queue can grow to the size of one diagonal.
    ///
    /// Runtime 28 ms Beats 100%
    /// Memory 5.54 MB Beats 100%
    pub fn find_diagonal_order_bfs(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len() - 1;
        let mut q = VecDeque::from([(0, 0)]);
        let mut res = vec![];
        while let Some((row, col)) = q.pop_front() {
            res.push(nums[row][col]);
            if col == 0 && row < n {
                q.push_back((row + 1, 0));
            }
            if col + 1 < nums[row].len() {
                q.push_back((row, col + 1));
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]],
            vec![1, 4, 2, 7, 5, 3, 8, 6, 9],
        ),
        (
            vec![
                vec![1, 2, 3, 4, 5],
                vec![6, 7],
                vec![8],
                vec![9, 10, 11],
                vec![12, 13, 14, 15, 16],
            ],
            vec![1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::find_diagonal_order(t.0.clone()), t.1);
        assert_eq!(Solution::find_diagonal_order_bfs(t.0.clone()), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
