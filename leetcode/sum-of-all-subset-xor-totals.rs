// 1863. Sum of All Subset XOR Totals
// 🟢 Easy
//
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/
//
// Tags: Array - Math - Backtracking - Bit Manipulation - Combinatorics - Enumeration

struct Solution;
impl Solution {
    /// We can use a binary decision tree, use and skip the current element, return the sum of both
    /// decisions.
    ///
    /// Time complexity: O(2^n) - The decision tree has height n and splits in 2 at each step.
    /// Space complexity: O(n) - The height of the call stack.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.06 MB Beats 76%
    pub fn subset_xor_sum(nums: Vec<i32>) -> i32 {
        fn dfs(nums: &Vec<i32>, i: usize, cur: i32) -> i32 {
            if i == nums.len() {
                return cur;
            }
            // Use + skip.
            dfs(nums, i + 1, cur) + dfs(nums, i + 1, cur ^ nums[i])
        }
        dfs(&nums, 0, 0)
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 3], 6),
        (vec![5, 1, 6], 28),
        (vec![3, 4, 5, 6, 7, 8], 480),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::subset_xor_sum(t.0.clone());
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
