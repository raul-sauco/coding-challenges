// 2684. Maximum Number of Moves in a Grid
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/
//
// Tags: Array - Dynamic Programming - Matrix

use std::mem::swap;

struct Solution;
impl Solution {
    /// Use dynamic programming, use a dp vector to determine which cells in the previous column
    /// are reachable, initialize it at all true. The transition is marking the cell as reachable
    /// if we can reach it from any of its three neighbors in the previous rows. For that to be
    /// true, at least one of its neighbors on the top-left, left or bottom-left needs to be
    /// reachable and have a value that is strictly lower.
    ///
    /// Time complexity: O(m*n) - We may visit each cell in the grid and do three conditional
    /// checks for each using constant time.
    /// Space complexity: O(m) - We use two vectors of the length of a column to store intermediate
    /// results.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 3.84 MB Beats 100%
    pub fn max_moves(grid: Vec<Vec<i32>>) -> i32 {
        let (num_rows, num_cols) = (grid.len(), grid[0].len());
        let (mut prev, mut dp) = (vec![true; num_rows], vec![false; num_rows]);
        let mut can_move;
        for col in 1..num_cols {
            can_move = false;
            for row in 0..num_rows {
                dp[row] = (prev[row] && grid[row][col - 1] < grid[row][col])
                    || (row > 0 && prev[row - 1] && grid[row - 1][col - 1] < grid[row][col])
                    || (row < num_rows - 1
                        && prev[row + 1]
                        && grid[row + 1][col - 1] < grid[row][col]);
                if dp[row] {
                    can_move = true;
                }
            }
            if !can_move {
                return col as i32 - 1;
            }
            swap(&mut dp, &mut prev);
        }
        num_cols as i32 - 1
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![
                vec![2, 4, 3, 5],
                vec![5, 4, 9, 3],
                vec![3, 4, 2, 11],
                vec![10, 9, 13, 15],
            ],
            3,
        ),
        (vec![vec![3, 2, 4], vec![2, 1, 9], vec![1, 1, 7]], 0),
        (
            vec![
                vec![187, 167, 209, 251, 152, 236, 263, 128, 135],
                vec![267, 249, 251, 285, 73, 204, 70, 207, 74],
                vec![189, 159, 235, 66, 84, 89, 153, 111, 189],
                vec![120, 81, 210, 7, 2, 231, 92, 128, 218],
                vec![193, 131, 244, 293, 284, 175, 226, 205, 245],
            ],
            3,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_moves(t.0.clone());
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
