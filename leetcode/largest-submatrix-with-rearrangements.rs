// 1727. Largest Submatrix With Rearrangements
// 🟠 Medium
//
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/
//
// Tags: Array - Greedy - Sorting - Matrix

struct Solution;
impl Solution {
    /// Iterate over the columns counting the number of consecutive ones up to the current location
    /// and storing that information in an auxiliary matrix of the same size as the input. Once we
    /// have computed all the values in the auxitilary matrix, iterate over its rows sorting them
    /// in non-increasing order, then iterate over the values, each cell tells us how many
    /// consecutive ones are in its column above and including the current cell, since we have
    /// sorted the row values, we know that no cell to its left will have a lower value, that means
    /// that we can form a matrix that contains only ones with its position in the row as the
    /// number of columns and its value as the number of rows.
    ///
    /// Time complexity: O(m*n*log(n)) - Besides visiting each cell twice, we also sort the rows of
    /// the auxiliary matrix.
    /// Space complexity: O(m*n) - The auxiliary matrix has the same size as the input.
    ///
    /// Runtime 25 ms Beats 100%
    /// Memory 14.49 MB Beats 100%
    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) -> i32 {
        let (num_rows, num_cols) = (matrix.len(), matrix[0].len());
        let mut aux = vec![Vec::with_capacity(num_cols); num_rows];
        let mut consecutive_ones;
        for c in 0..num_cols {
            consecutive_ones = 0;
            for r in 0..num_rows {
                match matrix[r][c] {
                    1 => consecutive_ones += 1,
                    _ => consecutive_ones = 0,
                }
                aux[r].push(consecutive_ones);
            }
        }
        // Iterative version of the iterator below.
        // let mut res = 0;
        // Sort the rows.
        // for row in aux.iter_mut() {
        //     row.sort_unstable_by(|a, b| b.cmp(a));
        //     for j in 0..num_cols {
        //         res = res.max(row[j] * (j + 1));
        //     }
        // }
        aux.iter_mut()
            .map(|r| {
                r.sort_unstable_by(|a, b| b.cmp(a));
                r
            })
            .fold(0, |acc, x| {
                let val = x
                    .into_iter()
                    .enumerate()
                    .fold(0, |acc, (i, x)| acc.max(*x * (i + 1)));
                // println!("{:?}", x);
                acc.max(val)
            }) as i32
        // res as i32
    }
}

// Tests can run automatically on save, for example:
// $ cargo watch -c -w src -x run
// $ watchexec -e rs cargo run
fn main() -> Result<(), &'static str> {
    let tests = [
        (vec![vec![0, 0, 1], vec![1, 1, 1], vec![1, 0, 1]], 4),
        (vec![vec![1, 0, 1, 0, 1]], 3),
        (vec![vec![1, 1, 0], vec![1, 0, 1]], 2),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::largest_submatrix(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx Test {} failed expected: {} but got {}!\x1b[0m",
                i, t.1, res
            );
        }
    }
    println!("");
    if success == tests.len() {
        println!("\x1b[30;42m» All tests passed!\x1b[0m");
    } else if success == 0 {
        println!("\x1b[41m» All tests failed!\x1b[0m");
    } else {
        println!("\x1b[31;1;43m» Some tests failed!\x1b[0m");
    }
    Ok(())
}
