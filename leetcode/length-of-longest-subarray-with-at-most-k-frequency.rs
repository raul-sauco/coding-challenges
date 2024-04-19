// 2958. Length of Longest Subarray With at Most K Frequency
// 🟠 Medium
//
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
//
// Tags: Array - Hash Table - Sliding Window

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Use a sliding window, count the number of times that we have seen a value, if the count
    /// goes over k, start shrinking the window from the left, removing the elements from the
    /// counter, until the count of nums[r] is back to k.
    ///
    /// Time complexity: O(n) - We visit each element in the input and do constant work for each,
    /// we could slide the left pointer more than once for a position of the right pointer, but we
    /// will move it a maximum of n times.
    /// Space complexity: O(n) - The counts hashmap will have one entry per each unique value in
    /// the input array and could be size n.
    ///
    /// Runtime 54 ms Beats 81%
    /// Memory 6.77 MB Beats 27%
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut res = 0;
        let mut l = 0;
        let mut counts = HashMap::new();
        for r in 0..nums.len() {
            counts.entry(nums[r]).and_modify(|e| *e += 1).or_insert(1);
            while *counts.get(&nums[r]).unwrap() > k {
                // Need to move the left pointer to a nums[r] instance.
                counts.entry(nums[l]).and_modify(|e| *e -= 1);
                l += 1;
            }
            res = res.max(1 + r - l);
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 2, 1, 3], 1, 3),
        (vec![5, 5, 5, 5, 5, 5, 5], 4, 4),
        (vec![1, 2, 3, 1, 2, 3, 1, 2], 2, 6),
        (vec![1, 2, 1, 2, 1, 2, 1, 2], 1, 2),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_subarray_length(t.0.clone(), t.1);
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.2, res
            );
        }
    }
    println!();
    if success == tests.len() {
        println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    } else if success == 0 {
        println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    } else {
        println!(
            "\x1b[31mx\x1b[95m {} tests failed!\x1b[0m",
            tests.len() - success
        )
    }
}
