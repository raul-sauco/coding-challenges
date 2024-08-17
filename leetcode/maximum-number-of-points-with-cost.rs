// 1937. Maximum Number of Points with Cost
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-number-of-points-with-cost/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /// Use dynamic programming, for each row and cell, store the most we can gain using a value
    /// above it from the right and from the left, we keep two maximum values, the max we can get
    /// using a cell from the right and left, each time we move one cell right/left, we subtract
    /// one to that value, and max it with the value in the dp cell we are currently processing.
    /// Once we get the max we can get from the previous rows, we add the value at the current row
    /// and store it in the dp vector to use when processing the next row.
    ///
    /// Time complexity: O(m*n) - We process each row in the matrix once, for each row, the inner
    /// for loop runs once per column and it visits two cells inside, one going right and one left.
    /// Space complexity: O(n) - The size of both dp vectors is the number of columns.
    ///
    /// Runtime 28 ms Beats 50%
    /// Memory 8.53 MB Beats 100%
    pub fn max_points(points: Vec<Vec<i32>>) -> i64 {
        let (num_rows, num_cols) = (points.len(), points[0].len());
        let (mut dp, mut next) = (vec![0; num_cols], vec![0; num_cols]);
        let (mut max_left, mut max_right);
        for row_idx in 0..num_rows {
            (max_left, max_right) = (0, 0);
            for c in 0..num_cols {
                // From the left.
                max_left = (max_left - 1).max(dp[c]);
                next[c] = next[c].max(max_left);
                // From the right.
                let r = num_cols - c - 1;
                max_right = (max_right - 1).max(dp[r]);
                next[r] = next[r].max(max_right);
            }
            dp = (0..num_cols)
                .map(|i| next[i] + (points[row_idx][i] as i64))
                .collect();
        }
        dp.into_iter().max().unwrap()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![1, 2, 3], vec![1, 5, 1], vec![3, 1, 1]], 9),
        (vec![vec![1, 5], vec![2, 3], vec![4, 2]], 11),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_points(t.0.clone());
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
