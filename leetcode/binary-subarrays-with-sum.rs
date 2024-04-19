// 930. Binary Subarrays With Sum
// 🟠 Medium
//
// https://leetcode.com/problems/binary-subarrays-with-sum/
//
// Tags: Array - Hash Table - Sliding Window - Prefix Sum

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Sliding window technique, two passes, we can only compute the number of subarrays with sum
    /// of at least x, we compute that for goal and goal - 1 and return the difference.
    ///
    /// Time complexity: O(n) - We visit each element in the input twice.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 2 ms Beats 87%
    /// Memory 2.16 MB Beats 100%
    pub fn num_subarrays_with_sum(nums: Vec<i32>, goal: i32) -> i32 {
        fn helper(nums: &Vec<i32>, goal: i32) -> i32 {
            let (mut start, mut sum, mut res) = (0, 0, 0);
            for end in 0..nums.len() {
                sum += nums[end];
                while start <= end && sum > goal {
                    sum -= nums[start];
                    start += 1;
                }
                res += 1 + end - start;
            }
            res as i32
        }
        helper(&nums, goal) - if goal > 0 { helper(&nums, goal - 1) } else { 0 }
    }

    /// Use a hashmap to store prefix sums seen up to that point, we will be able to get a subarray
    /// with sum equal to goal using the current index as the end and any index that had a sum of
    /// current - goal previously.
    ///
    /// Time complexity: O(n) - We visit each element in the input.
    /// Space complexity: O(n) - The hashmap of sums, if all values were 1 it would have n entries.
    ///
    /// Runtime 6 ms Beats 37%
    /// Memory 3.12 MB Beats 12%
    #[allow(dead_code)]
    pub fn num_subarrays_with_sum_hm(nums: Vec<i32>, goal: i32) -> i32 {
        let mut seen = HashMap::new();
        seen.insert(0, 1);
        let mut res = 0;
        let mut sum = 0;
        for num in nums {
            sum += num;
            if let Some(count) = seen.get(&(sum - goal)) {
                res += count;
            }
            *seen.entry(sum).or_insert(0) += 1;
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 0, 1, 0, 1], 2, 4),
        (vec![0, 0, 0, 0, 0], 0, 15),
        (vec![0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 0, 27),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::num_subarrays_with_sum(t.0.clone(), t.1);
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
