// 312. Burst Balloons
// 🔴 Hard
//
// https://leetcode.com/problems/burst-balloons/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /// The most efficient way to solve the problem, is to split it into sub
    /// problems, taking the last balloon bursted as the split point to divide
    /// the array into two. For each subproblem, defined by the left and right
    /// boundary of the array slice that we are processing, we will find the
    /// optimal way to solve the problem by trying to use each element as the
    /// last balloon bursted and computing the subproblems to the left and
    /// right. For each subproblem (l,r) we will store the optimal way of
    /// solving it in the dp array, to avoid doing repeated work.
    ///
    /// Time complexity: O(n^3) - We have three levels of nested loops
    /// that go over n-2 elements each at most.
    /// Space complexity: O(n^2) - The dp array has size (n+2)^2.
    ///
    /// Runtime 64 ms Beats 13.33%
    /// Memory 2.5 MB Beats 20%
    pub fn max_coins(nums: Vec<i32>) -> i32 {
        let n = nums.len() + 2;
        // We create a padded version of nums.
        let mut balloons = Vec::with_capacity(n);
        balloons.push(1);
        balloons.extend(nums.iter());
        balloons.push(1);
        let mut dp = vec![vec![0; n]; n];
        for l in (0..n - 1).rev() {
            for r in l + 2..n {
                for i in l + 1..r {
                    dp[l][r] =
                        dp[l][r].max(balloons[l] * balloons[r] * balloons[i] + dp[l][i] + dp[i][r]);
                }
            }
        }
        dp[0][n - 1]
    }
}

// Tests.
fn main() {
    let tests = [(vec![1, 5], 10), (vec![3, 1, 5, 8], 167)];
    for t in tests {
        assert_eq!(Solution::max_coins(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
