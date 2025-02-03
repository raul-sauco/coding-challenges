// 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
// 🟢 Easy
//
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
//
// Tags: Array

struct Solution;
impl Solution {
    /// Iterate over the numbers in the input, for each one, compare it with the previous value to
    /// determine if it is increasing, decreasing or equal, add one to the length of that sequence
    /// and restart the other at a length of 1, if that value is the new max, update it.
    ///
    /// Time complexity: O(1)
    /// Space complexity: O(1)
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.18 MB Beats 100%
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        let (mut res, mut inc, mut dec) = (1, 1, 1);
        for i in 1..nums.len() {
            match nums[i].cmp(&nums[i - 1]) {
                std::cmp::Ordering::Less => {
                    inc = 1;
                    dec += 1;
                    res = res.max(dec);
                }
                std::cmp::Ordering::Equal => {
                    inc = 1;
                    dec = 1;
                }
                std::cmp::Ordering::Greater => {
                    dec = 1;
                    inc += 1;
                    res = res.max(inc);
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 4, 3, 3, 2], 2),
        (vec![3, 3, 3, 3], 1),
        (vec![3, 2, 1], 3),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::longest_monotonic_subarray(t.0.clone());
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
