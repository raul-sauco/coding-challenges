// 1800. Maximum Ascending Subarray Sum
// 🟢 Easy
//
// https://leetcode.com/problems/maximum-ascending-subarray-sum/
//
// Tags: Array

struct Solution;
impl Solution {
    /// Iterate over the input keeping track of the current sum of ascending nums, if we find a
    /// non-ascending item, reset the sum.
    ///
    /// Time complexity: O(n)
    /// Space complexity: O(1)
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.24 MB Beats 45%
    pub fn max_ascending_sum(nums: Vec<i32>) -> i32 {
        let (mut current_sum, mut res) = (nums[0], nums[0]);
        for i in 1..nums.len() {
            if nums[i] > nums[i - 1] {
                current_sum += nums[i];
            } else {
                current_sum = nums[i];
            }
            res = res.max(current_sum);
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![10, 20, 30, 5, 10, 50], 65),
        (vec![10, 20, 30, 40, 50], 150),
        (vec![12, 17, 15, 13, 10, 11, 12], 33),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_ascending_sum(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.1, res
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
