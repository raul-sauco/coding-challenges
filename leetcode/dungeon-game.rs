// 174. Dungeon Game
// 🔴 Hard
//
// https://leetcode.com/problems/dungeon-game/
//
// Tags: Array - Dynamic Programming - Matrix

struct Solution;
impl Solution {
    /// Start at the "princess" and traverse the matrix backwards computing the
    /// minimum health we need to start with from that cell to be able to reach
    /// the princess.
    ///
    /// Time complexity: O(m*n) - We visit each element of the input 2D vector
    /// and do constant time work for each.
    /// Space complexity: O(m*n) - We use a 2D matrix of the same size as the
    /// input plus one per dimension.
    ///
    /// Runtime 1 ms Beats 75.61%
    /// Memory 2.25 MB Beats 65.85%
    pub fn calculate_minimum_hp(dungeon: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (dungeon.len(), dungeon[0].len());
        let mut dp = vec![vec![i32::MAX; n + 1]; m + 1];
        dp[m][n - 1] = 1;
        dp[m - 1][n] = 1;
        for i in (0..m).rev() {
            for j in (0..n).rev() {
                dp[i][j] = std::cmp::min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j];
                if dp[i][j] < 1 {
                    dp[i][j] = 1;
                }
            }
        }
        dp[0][0]
    }

    /// Similar solution but keep only the last row of dp values in memory.
    ///
    /// Time complexity: O(m*n) - We visit each element of the input 2D vector
    /// and do constant time work for each.
    /// Space complexity: O(n) - We use two rows of size n of extra memory.
    ///
    /// Runtime 1 ms Beats 75.61%
    /// Memory 2.22 MB Beats 65.85%
    pub fn calculate_minimum_hp_2(dungeon: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (dungeon.len(), dungeon[0].len());
        let mut dp = vec![i32::MAX; n + 1];
        let mut prev = vec![i32::MAX; n + 1];
        prev[n - 1] = 1;
        dp[n] = 1;
        for i in (0..m).rev() {
            for j in (0..n).rev() {
                dp[j] = std::cmp::min(prev[j], dp[j + 1]) - dungeon[i][j];
                if dp[j] < 1 {
                    dp[j] = 1;
                }
            }
            std::mem::swap(&mut dp, &mut prev);
            dp[n] = i32::MAX;
        }
        prev[0]
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![-2, -3, 3], vec![-5, -10, 1], vec![10, 30, -5]], 7),
        (vec![vec![0]], 1),
    ];
    for t in tests {
        assert_eq!(Solution::calculate_minimum_hp(t.0.clone()), t.1);
        assert_eq!(Solution::calculate_minimum_hp_2(t.0.clone()), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
