// 2461. Maximum Sum of Distinct Subarrays With Length K
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
//
// Tags: Array - Hash Table - Sliding Window

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Use a sliding window of size k, keep its sum and the count of elements in the window, also
    /// the number of duplicates, add values from the right and pop them from the left updating the
    /// counts, sum and duplicates, if the current window does not have duplicates, max its value
    /// with the result.
    ///
    /// Time complexity: O(n) - We process each element in the input in O(1~)
    /// Space complexity: O(n) - The counts hashmap could have one entry per value in the input
    /// vector.
    ///
    /// Runtime 32 ms Beats 5%
    /// Memory 7.11 MB Beats 9%
    pub fn maximum_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let mut counts = HashMap::<i32, usize>::new();
        let mut duplicates = 0;
        let k = k as usize;
        let n = nums.len();
        let mut current_sum = 0i64;
        let mut res = 0i64;
        for &num in &nums[..k] {
            current_sum += num as i64;
            counts.entry(num).and_modify(|c| *c += 1).or_insert(1);
            if counts[&num] == 2 {
                duplicates += 1;
            }
        }
        if duplicates == 0 {
            res = current_sum;
        }
        let mut l = 0;
        for r in k..n {
            current_sum += nums[r] as i64;
            counts.entry(nums[r]).and_modify(|c| *c += 1).or_insert(1);
            if counts[&nums[r]] == 2 {
                duplicates += 1;
            }
            current_sum -= nums[l] as i64;
            counts.entry(nums[l]).and_modify(|c| *c -= 1);
            if counts[&nums[l]] == 1 {
                duplicates -= 1;
            }
            if duplicates == 0 {
                res = res.max(current_sum);
            }
            l += 1;
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(vec![1, 5, 4, 2, 9, 9, 9], 3, 15), (vec![4, 4, 4], 3, 0)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::maximum_subarray_sum(t.0.clone(), t.1);
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
