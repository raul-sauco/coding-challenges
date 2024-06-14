// 1827. Minimum Operations to Make the Array Increasing
// 🟢 Easy
//
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
//
// Tags: Array - Greedy

struct Solution;
impl Solution {
    /// Make sure that each element is, at least, 1 unit greater than the previous one.
    ///
    /// Time complexity: O(n) - Visit each element and do constant time work for each.
    /// Space complexity: O(1) - Two i32s variables.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.18 MB Beats 64%
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut min = nums[0] + 1;
        for &num in nums[1..].into_iter() {
            if num < min {
                res += min - num;
                min += 1;
            } else {
                min = num + 1;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(vec![1, 1, 1], 3), (vec![1, 5, 2, 4, 1], 14)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_operations(t.0.clone());
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
