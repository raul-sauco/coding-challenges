// 1277. Count Square Submatrices with All Ones
// 🟠 Medium
//
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/
//
// Tags: Array - Dynamic Programming - Matrix

struct Solution;
impl Solution {
    /// Use dynamic programming, visit all cells, for each cell that contains a 1, check the number
    /// of squares that finish on that cell using the number of squares that finish in its 3
    /// neighbors to the left, top and top-left, and add that to the result.
    ///
    /// Time complexity: O(m*n) - We visit each cell in the matrix and check 3 other cells for
    /// each cell that we visit.
    /// Space complexity: O(1) - Since we are taking ownership of the matrix, we can decide if we
    /// want to mutate it, the caller does not have access to matrix after calling.
    ///
    /// Runtime 3 ms Beats 100%
    /// Memory 2.80 MB Beats 66%
    pub fn count_squares(mut matrix: Vec<Vec<i32>>) -> i32 {
        let mut res = 0;
        for r in 0..matrix.len() {
            for c in 0..matrix[0].len() {
                if matrix[r][c] == 1 {
                    if r == 0 || c == 0 {
                        matrix[r][c] = 1;
                    } else {
                        matrix[r][c] = 1 + matrix[r - 1][c]
                            .min(matrix[r][c - 1])
                            .min(matrix[r - 1][c - 1]);
                    }
                    res += matrix[r][c];
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
            vec![vec![0, 1, 1, 1], vec![1, 1, 1, 1], vec![0, 1, 1, 1]],
            15,
        ),
        (vec![vec![1, 0, 1], vec![1, 1, 0], vec![1, 1, 0]], 7),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::count_squares(t.0.clone());
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
