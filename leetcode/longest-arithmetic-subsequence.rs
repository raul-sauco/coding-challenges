// 1027. Longest Arithmetic Subsequence
// 🟠 Medium
//
// https://leetcode.com/problems/longest-arithmetic-subsequence/
//
// Tags: Array - Hash Table - Binary Search - Dynamic Programming

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Iterate over the input elements left to right, use a dp hashmap where
    /// we use as the key the last element and the sequence difference with the
    /// length of that sequence as the entry value. For each element, we
    /// iterate all the elements of dp starting a new sequence or adding one to
    /// any sequences where the gap matches the gap between the current and the
    /// last element of the sequence.
    ///
    /// Time complexity: O(n^2) - We iterate over all elements in the input,
    /// for each, we visit each element to its left.
    /// Space complexity: O(n) - We can have a dictionary entry per each
    /// combination of 2 elements in the input.
    ///
    /// Runtime 979 ms Beats 9.9%
    /// Memory 53.3 MB Beats 9.9%
    pub fn longest_arith_seq_length(nums: Vec<i32>) -> i32 {
        let mut dp = HashMap::new();
        for r in 0..nums.len() {
            for l in 0..r {
                let length = *dp.entry((l, nums[r] - nums[l])).or_insert(1) + 1;
                dp.insert((r, nums[r] - nums[l]), length);
            }
        }
        *dp.values().max().unwrap()
    }

    /// An improved version I found in LeetCode, besides using a vector instead
    /// of a hashmap, I can't quite figure out why this solution is 30 times
    /// faster. Look into it, would the previous solution have a similar
    /// runtime if we use a 2D vector instead of the hashmap?
    ///
    /// Runtime 37 ms Beats 100%
    /// Memory 2.1 MB Beats 90.91%
    pub fn longest_arith_seq_length_fast(nums: Vec<i32>) -> i32 {
        let max = *nums.iter().max().unwrap();
        (-max..=max)
            .map(|step| {
                let mut dp = vec![0_i32; max as usize + 1];
                for &x in &nums {
                    dp[x as usize] =
                        dp[x as usize].max(dp.get((x - step) as usize).copied().unwrap_or(0) + 1);
                }
                *dp.iter().max().unwrap()
            })
            .max()
            .unwrap()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3, 6, 9, 12], 4),
        (vec![9, 4, 7, 2, 10], 3),
        (vec![20, 1, 15, 3, 10, 5, 8], 4),
    ];
    for t in tests {
        assert_eq!(Solution::longest_arith_seq_length(t.0.clone()), t.1);
        assert_eq!(Solution::longest_arith_seq_length_fast(t.0.clone()), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
