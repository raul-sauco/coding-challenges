// 63. Unique Paths II
// 🟠 Medium
//
// https://leetcode.com/problems/unique-paths-ii/
//
// Tags: Array - Dynamic Programming - Matrix

struct Solution;
impl Solution {
    // Similar to unique paths, since we can only move right or down, the
    // number of ways to reach any cell equals the sum of the number of ways
    // to reach the cell above it and the number of ways to reach the cell to
    // its left. When we find an obstacle, the number of ways to reach that
    // cell is 0 since we cannot visit it.
    //
    // Time complexity: O(m*n) - Where m is the number of rows and n is the
    // number of columns. We will visit each cell once.
    // Space complexity: O(n) - We use an array of size n to store
    // intermediate results.
    //
    // Runtime 1 ms Beats 88.57%
    // Memory 2 MB Beats 94.29%
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let n = obstacle_grid[0].len();
        // Use a one dimensional vector of length n + 1 to store
        // intermediate results.
        // Prefill a row before the initial row in the grid.
        let mut dp = vec![0; n + 1];
        dp[1] = 1;
        for row in obstacle_grid {
            for i in 1..dp.len() {
                if row[i - 1] == 1 {
                    dp[i] = 0;
                } else {
                    dp[i] += dp[i - 1];
                }
            }
        }
        *dp.last().unwrap()
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::unique_paths_with_obstacles(vec![vec![0, 1]]), 0);
    assert_eq!(
        Solution::unique_paths_with_obstacles(vec![vec![0, 1], vec![0, 0]]),
        1
    );
    assert_eq!(
        Solution::unique_paths_with_obstacles(vec![vec![0, 0, 0], vec![0, 0, 0], vec![0, 0, 0]]),
        6
    );
    assert_eq!(
        Solution::unique_paths_with_obstacles(vec![vec![0, 0, 0], vec![0, 1, 0], vec![0, 0, 0]]),
        2
    );
    println!("All tests passed!")
}
