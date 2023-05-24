// 2542. Maximum Subsequence Score
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-subsequence-score/
//
// Tags: Array - Greedy - Sorting - Heap (Priority Queue)

use std::collections::BinaryHeap;

struct Solution {}
impl Solution {
    /// We start by zipping the values to keep items on the same indexes
    /// together, then we sort them. We are only allowed to use the smallest
    /// of all the values in nums2, that means we only need to keep track of one
    /// value from that input. On the other input, we also want to greedily
    /// pick the highest k-1 values, to maximize the score, we can efficiently
    /// discard the least valuable of the scores that we have seen using a heap.
    ///
    /// Time complexity: O(n*log(n)) - First we sort the n tuples formed by
    /// zipping the two input vectors, then we iterate over all the n elements
    /// pushing and popping into the heap at a O(log(k)) cost each.
    /// Space complexity: O(k) - The size of the heap and the sorted vectors.
    ///
    /// Runtime 30 ms Beats 66.67%
    /// Memory 3.9 MB Beats 66.67%
    pub fn max_score(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let k = k as usize;
        let mut sorted: Vec<(i32, i32)> = nums1.into_iter().zip(nums2.into_iter()).collect();
        sorted.sort_by(|a, b| b.1.cmp(&a.1));
        let mut pq = BinaryHeap::with_capacity(k + 1);
        let mut sum = 0;
        let mut res = 0;
        for (up, down) in sorted {
            let (up, down) = (up as i64, down as i64);
            if pq.len() == k {
                sum += pq.pop().unwrap();
            }
            sum += up;
            pq.push(-up);
            if pq.len() == k {
                res = res.max(sum * down);
            }
        }
        res
    }
}

fn main() {
    let tests = [
        (vec![1, 3, 3, 2], vec![2, 1, 3, 4], 3, 12),
        (vec![4, 2, 3, 1, 1], vec![7, 5, 10, 9, 6], 1, 30),
    ];
    for t in tests {
        assert_eq!(Solution::max_score(t.0, t.1, t.2), t.3);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
