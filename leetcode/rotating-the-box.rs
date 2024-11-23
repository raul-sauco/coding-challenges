// 1861. Rotating the Box
// 🟠 Medium
//
// https://leetcode.com/problems/rotating-the-box/
//
// Tags: Array - Two Pointers - Matrix

struct Solution;
impl Solution {
    /// Create the result matrix, iterate over the input by row and reversed column using a read
    /// and write pointer, when we find a rock, write it to the current position of the write
    /// pointer and shift it one row up, when we find an obstacle, write it to its rotated position
    /// and move the write pointer to the cell above it.
    ///
    /// Time complexity: O(m*n) - We iterate over m rows and n columns.
    /// Space complexity: O(m*n) - The result matrix, if we take it into account.
    ///
    /// Runtime 138 ms Beats 83%
    /// Memory 18.87 MB Beats 50%
    pub fn rotate_the_box(matrix: Vec<Vec<char>>) -> Vec<Vec<char>> {
        // The number of rows and columns in the input matrix.
        let (num_rows, num_cols) = (matrix.len(), matrix[0].len());
        let mut res = vec![vec!['.'; num_rows]; num_cols];
        let (mut write_row, mut write_col);
        for row in 0..num_rows {
            write_col = num_rows - row - 1;
            write_row = num_cols - 1;
            for col in (0..num_cols).rev() {
                match matrix[row][col] {
                    '*' => {
                        // Obstacle, it will not move and block the current cell.
                        res[col][write_col] = '*';
                        if col > 0 {
                            write_row = col - 1;
                        }
                    }
                    '#' => {
                        // Rock, it will fall as far as it can and block that cell.
                        res[write_row][write_col] = '#';
                        if write_row > 0 {
                            write_row -= 1;
                        }
                    }
                    _ => (),
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![vec!['#', '.', '#']],
            vec![vec!['.'], vec!['#'], vec!['#']],
        ),
        (
            vec![vec!['#', '.', '*', '.'], vec!['#', '#', '*', '.']],
            vec![
                vec!['#', '.'],
                vec!['#', '#'],
                vec!['*', '*'],
                vec!['.', '.'],
            ],
        ),
        (
            vec![
                vec!['#', '#', '*', '.', '*', '.'],
                vec!['#', '#', '#', '*', '.', '.'],
                vec!['#', '#', '#', '.', '#', '.'],
            ],
            vec![
                vec!['.', '#', '#'],
                vec!['.', '#', '#'],
                vec!['#', '#', '*'],
                vec!['#', '*', '.'],
                vec!['#', '.', '*'],
                vec!['#', '.', '.'],
            ],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::rotate_the_box(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
