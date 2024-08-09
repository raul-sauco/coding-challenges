// 840. Magic Squares In Grid
// 🟠 Medium
//
// https://leetcode.com/problems/magic-squares-in-grid/
//
// Tags: Array - Hash Table - Math - Matrix

struct Solution;
impl Solution {
    /// There are only a few combinations of matrixes that are "magic" and all of them have the 5
    /// in the center square and one of two combinations of sequences along the border cells.
    /// Search for cells that contain a 5 and could be the center of a 5x5 cell and check if the
    /// border cells form one of the two valid sequences.
    ///
    /// Time complexity: O(mxn) - Where m is the number of rows and n is the number of columns.
    /// Space complexity: O(1) - We store a doubled border combination.
    ///
    /// Runtime 1 ms Beats 80%
    /// Memory 2.06 MB Beats 80%
    pub fn num_magic_squares_inside(grid: Vec<Vec<i32>>) -> i32 {
        let (num_rows, num_cols) = (grid.len(), grid[0].len());
        fn is_magic_grid(grid: &Vec<Vec<i32>>, i: usize, j: usize) -> bool {
            let mut border = [0; 8];
            (0..3).for_each(|c| {
                border[c] = grid[i - 1][c + j - 1];
                border[c + 4] = grid[i + 1][j + 1 - c];
            });
            border[3] = grid[i][j + 1];
            border[7] = grid[i][j - 1];
            let border = border
                .iter()
                .map(|&num| num.to_string())
                .collect::<String>();
            let doubled = border.clone() + &border;
            doubled.contains("29438167") || doubled.contains("76183492")
        }
        let mut res = 0;
        // Iterate over values that could be the center cell of grids
        for i in 1..num_rows - 1 {
            for j in 1..num_cols - 1 {
                if grid[i][j] == 5 && is_magic_grid(&grid, i, j) {
                    res += 1;
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![8]], 0),
        (
            vec![vec![4, 3, 8, 4], vec![9, 5, 1, 9], vec![2, 7, 6, 2]],
            1,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::num_magic_squares_inside(t.0.clone());
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
