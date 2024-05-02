// 2441. Largest Positive Integer That Exists With Its Negative
// 🟢 Easy
//
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
//
// Tags: Array - Hash Table - Two Pointers - Sorting

struct Solution;
impl Solution {
    /// Sort the input, then use two pointers to compare the biggest values with the smallest.
    ///
    /// Time complexity: O(nlog(n)) - The sorting step, after that O(n)
    /// Space complexity: O(n) - The mutable input copy.
    ///
    /// Runtime 4 ms Beats 73%
    /// Memory 2.24 MB Beats 6%
    pub fn find_max_k(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        let (mut l, mut r) = (0, nums.len() - 1);
        while l < r {
            match 0.cmp(&(nums[r] + nums[l])) {
                std::cmp::Ordering::Less => r -= 1,
                std::cmp::Ordering::Equal => return nums[r],
                std::cmp::Ordering::Greater => l += 1,
            }
        }
        -1
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![-1, 2, -3, 3], 3),
        (vec![-1, 10, 6, 7, -7, 1], 7),
        (vec![-10, 8, 6, 7, -2, -3], -1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_max_k(t.0.clone());
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
