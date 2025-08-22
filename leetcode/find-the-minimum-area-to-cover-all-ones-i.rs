// 3195. Find the Minimum Area to Cover All Ones I
// 🟠 Medium
//
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/
//
// Tags: Array - Matrix

struct Solution;
impl Solution {
    /// Iterate over the cells keeping track of the first and last columns and rows where the value
    /// is a 1, then use these corners to compute the total area.
    ///
    /// Time complexity: O(m*n) - We visit each cell and do O(1) work for each.
    /// Space complexity: O(1) - We store a few i32 values.
    ///
    /// Runtime 39 ms Beats 100%
    /// Memory 8,87 MB Beats 85%
    pub fn minimum_area(grid: Vec<Vec<i32>>) -> i32 {
        let (num_rows, num_cols) = (grid.len(), grid[0].len());
        let (mut min_row, mut max_row, mut min_col, mut max_col) = (i32::MAX, -1, i32::MAX, -1);
        for row in 0..num_rows {
            for col in 0..num_cols {
                if grid[row][col] == 1 {
                    min_row = min_row.min(row as i32);
                    max_row = max_row.max(row as i32);
                    min_col = min_col.min(col as i32);
                    max_col = max_col.max(col as i32);
                }
            }
        }
        (max_row - min_row + 1) * (max_col - min_col + 1)
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![0, 1, 0], vec![1, 0, 1]], 6),
        (vec![vec![1, 0], vec![0, 0]], 1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::minimum_area(t.0.clone());
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
        println!("\x1b[60;42m✔ All tests passed!\x1b[0m")
    } else if success == 0 {
        println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    } else {
        println!(
            "\x1b[31mx\x1b[95m {} tests failed!\x1b[0m",
            tests.len() - success
        )
    }
}
