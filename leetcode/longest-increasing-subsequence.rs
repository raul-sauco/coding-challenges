// 300. Longest Increasing Subsequence
// 🟠 Medium
//
// https://leetcode.com/problems/longest-increasing-subsequence/
//
// Tags: Array - Binary Search - Dynamic Programming

struct Solution;
impl Solution {
    /// Iterate over the input, keep a dp array where each position is the value of the last
    /// position of a sequence of `index` length.
    ///
    /// Time complexity: O(n*log(n)) - We visit each number in the input, for each, we find its
    /// insertion position in the dp array using binary search.
    /// Space complexity: O(n) - The dp array is initialized at the same size as the input.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.19 MB Beats 51.35%
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut dp = vec![i32::MIN; nums.len() + 1];
        let mut lis = 0;
        let (mut l, mut m, mut r);
        for num in nums {
            (l, r) = (0, lis + 1);
            while l < r {
                m = (l + r) / 2;
                if dp[m] >= num {
                    r = m;
                } else {
                    l = m + 1;
                }
            }
            dp[l] = num;
            lis = lis.max(l);
        }
        lis as i32
    }
}

// Tests.
fn main() {
    let tests = [
        //         (vec![10, 9, 2, 5, 3, 7, 101, 18], 4),
        (vec![0, 1, 0, 3, 2, 3], 4),
        (vec![7, 7, 7, 7, 7, 7, 7], 1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::length_of_lis(t.0.clone());
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
