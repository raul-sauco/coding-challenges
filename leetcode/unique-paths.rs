// 62. Unique Paths
// 🟠 Medium
//
// https://leetcode.com/problems/unique-paths/
//
// Tags: Math - Dynamic Programming - Combinatorics

struct Solution;
impl Solution {
    /// Bottom-up DP, initialize a vector of n elements with 1s, the number of
    /// ways to reach positions in the first row. Then visit successive rows,
    /// the number of ways to reach each cell is the sum of ways to reach the
    /// cells above and to its left.
    ///
    /// Time complexity: O(m*n) - We visit each cell in the grid and do constant
    /// time work for each.
    /// Space complexity: O(n) - We store n values in a vector. An optimization
    /// would be to check if the number of rows or columns is greater and store
    /// the smaller one, in that case space complexity would be O(min(m,n))
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 1.96 MB Beats 92.91%
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let (m, n) = (m as usize, n as usize);
        let mut paths = vec![1; n];
        for _ in 0..m - 1 {
            for i in 1..n {
                paths[i] += paths[i - 1];
            }
        }
        paths[n - 1]
    }
}

// Tests.
fn main() {
    let tests = [(1, 1, 1), (3, 2, 3), (3, 7, 28)];
    for t in tests {
        assert_eq!(Solution::unique_paths(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
