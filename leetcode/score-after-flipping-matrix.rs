// 861. Score After Flipping Matrix
// 🟠 Medium
//
// https://leetcode.com/problems/score-after-flipping-matrix/
//
// Tags: Array - Greedy - Bit Manipulation - Matrix

struct Solution;
impl Solution {
    /// The best strategy is to set the most significant bit for all numbers to 1, then flip or
    /// preserve columns to obtain the maximum number of ones.
    ///
    /// Time complexity: O(m*n) - We visit the values in each cell and do constant time work for
    /// each.
    /// Space complexity: O(1) - We only store two usize values.
    ///
    /// Runtime 1 ms Beats 50%
    /// Memory 2.10 MB Beats 100%
    pub fn matrix_score(grid: Vec<Vec<i32>>) -> i32 {
        let (num_rows, num_cols) = (grid.len(), grid[0].len());
        // The sum of most significant bits, all 1.
        let mut res = (1 << (num_cols - 1)) * num_rows;
        for c in 1..num_cols {
            let one_count = (0..num_rows)
                .map(|r| if grid[r][0] == grid[r][c] { 1 } else { 0 })
                .sum::<usize>();
            res += (1 << ((num_cols - c) - 1)) * one_count.max(num_rows - one_count);
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![vec![0, 0, 1, 1], vec![1, 0, 1, 0], vec![1, 1, 0, 0]],
            39,
        ),
        (vec![vec![0]], 1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::matrix_score(t.0.clone());
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
