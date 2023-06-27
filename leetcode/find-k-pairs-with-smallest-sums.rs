// 373. Find K Pairs with Smallest Sums
// 🟠 Medium
//
// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
//
// Tags: Array - Heap (Priority Queue)

use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    /// View the problem as a matrix with sorted rows and columns, keep a pool
    /// of possible candidates, stored as a priority queue, from which we will
    /// pick the next value with the smallest sum. Every time we pick a pair,
    /// we need to add the two possible pairs that could have the next smallest
    /// sum to the pool, in our matrix, that can only be the element to the
    /// right, or the one below.
    ///
    /// Time complexity: O(k*log(k)) - We will pop a maximum of k elements from
    /// the heap, for each pop, we will push two elements.
    /// Space complexity: O(k) - The heap can grow to a max size of 2*k items.
    ///
    /// Runtime 35 ms Beats 100%
    /// Memory 4 MB Beats 100%
    pub fn k_smallest_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let (m, n) = (nums1.len(), nums2.len());
        let mut q = BinaryHeap::new();
        q.push((-(nums1[0] + nums2[0]), 0, 0));
        let mut res: Vec<Vec<i32>> = Vec::new();
        let k = k as usize;
        for _ in 0..k.min(m * n) {
            match q.pop() {
                Some(node) => {
                    let i = node.1;
                    let j = node.2;
                    res.push(vec![nums1[i], nums2[j]]);
                    if j < n - 1 {
                        q.push((-(nums1[i] + nums2[j + 1]), i, j + 1));
                    }
                    // If this was the first row element, start on the next.
                    if j == 0 && i < m - 1 {
                        q.push((-(nums1[i + 1] + nums2[j]), i + 1, j));
                    }
                }
                None => unreachable!(),
            };
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![1, 7, 11],
            vec![2, 4, 6],
            3,
            vec![vec![1, 2], vec![1, 4], vec![1, 6]],
        ),
        (
            vec![1, 1, 2],
            vec![1, 2, 3],
            2,
            vec![vec![1, 1], vec![1, 1]],
        ),
        (vec![1, 2], vec![3], 3, vec![vec![1, 3], vec![2, 3]]),
    ];
    for t in tests {
        assert_eq!(Solution::k_smallest_pairs(t.0, t.1, t.2), t.3);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
