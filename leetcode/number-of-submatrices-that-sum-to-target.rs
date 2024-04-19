// 1074. Number of Submatrices That Sum to Target
// 🔴 Hard
//
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
//
// Tags: Array - Hash Table - Matrix - Prefix Sum

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Precompute a matrix of row prefix sums, then iterate over every combination of two columns.
    /// For each two columns, use the precomputed row sums to add one by one the row sums in O(1)
    /// and efficiently compute the total sum of elements in the matrixes that we can form using
    /// these columns. Store these sums in a hashmap and use it as a lookup, similar to how we do
    /// in Two Sum, to determine if we have seen previously any sum that subtracted from the
    /// current sum would give us the target. If yes, the matrix formed between these two points is
    /// one solution, and we can add 1 to the total result.
    ///
    /// Time complexity: O(m * n^2) - We iterate over every combination of 2 columns, n^2, for
    /// each, we visit each row m and do a O(1) operation using the precomputed prefix sums.
    /// Precomputing the prefix sums has a time complexity of O(m*n)
    /// Space complexity: O(m*n) - The prefix sum matrix has the highest space complexity, we also
    /// use space to store the sums in the hashmap, but that has a max size of m.
    ///
    /// Runtime 72 ms Beats 75%
    /// Memory 2.34 MB Beats 75%
    pub fn num_submatrix_sum_target(matrix: Vec<Vec<i32>>, target: i32) -> i32 {
        let (num_rows, num_cols) = (matrix.len(), matrix[0].len());
        let prefix_sums = matrix
            .iter()
            .map(|row| {
                row.iter()
                    .scan(0, |sum, num| {
                        *sum += num;
                        Some(*sum)
                    })
                    .collect::<Vec<_>>()
            })
            .collect::<Vec<_>>();
        let mut res = 0;
        for left_col_idx in 0..num_cols {
            for right_col_idx in left_col_idx..num_cols {
                let mut counts = HashMap::new();
                counts.insert(0, 1);
                // Compute the matrix sums for this combination of columns.
                let mut sum = 0;
                for row_idx in 0..num_rows {
                    sum += prefix_sums[row_idx][right_col_idx]
                        - if left_col_idx == 0 {
                            0
                        } else {
                            prefix_sums[row_idx][left_col_idx - 1]
                        };
                    let key = sum - target;
                    if let Some(count) = counts.get(&key) {
                        res += count;
                    }
                    *counts.entry(sum).or_insert(0) += 1;
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![0, 1, 0], vec![1, 1, 1], vec![0, 1, 0]], 0, 4),
        (vec![vec![1, -1], vec![-1, 1]], 0, 5),
        (vec![vec![904]], 0, 0),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::num_submatrix_sum_target(t.0.clone(), t.1);
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.2, res
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
