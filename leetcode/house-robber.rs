// 198. House Robber
// 🟠 Medium
//
// https://leetcode.com/problems/house-robber/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /// Check the Python solution for a gradual approach to this tabulation solution.
    /// At each house, we need to decide to rob it or skip it. If we rob it, we need to skip the
    /// next house. We can keep track of the max profit at each of the previous two houses, then
    /// visit each house, the max profit at this house is either robbing it, adding its loot to the
    /// best we had skipping the previous house, or skip it and keep what we had at the previous
    /// house.
    ///
    /// Time complexity: O(n) - We visit each element in the input and do constant time work for
    /// each.
    /// Space complexity: O(1) - We use two i32 variables of extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.14 MB Beats 53.18%
    pub fn rob(nums: Vec<i32>) -> i32 {
        if nums.len() < 3 {
            return nums.into_iter().max().unwrap_or(0);
        }
        let (mut prev, mut cur) = (nums[0], nums[0].max(nums[1]));
        for num in &nums[2..] {
            (prev, cur) = (cur, cur.max(num + prev));
        }
        prev.max(cur)
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![0], 0),
        (vec![1, 2, 3, 1], 4),
        (vec![2, 7, 9, 3, 1], 12),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::rob(t.0.clone());
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
