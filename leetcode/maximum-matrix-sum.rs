// 1975. Maximum Matrix Sum
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-matrix-sum/
//
// Tags: Array - Greedy - Matrix

struct Solution;
impl Solution {
    /// Visit all values in the matrix keeping track of the number of negative values, the smallest
    /// absolute value and the total sum of absolute values. We will be able to find a combination
    /// to flip any two values, that means that, if we have an even number of negative values, we
    /// will be able to flip them all, otherwise, there will be one value that we will not be able
    /// to flip, choose the smallest absolute value.
    ///
    /// Time complexity: O(m*n) - We visit each value in the matrix and do O(1) work for each.
    /// Space complexity: O(1) - The iterator accumulator, one bool, two i64s.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 3.19 MB Beats 100%
    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {
        match matrix.into_iter().flat_map(|row| row.into_iter()).fold(
            (true, i64::MAX, 0i64),
            |acc, x| {
                let a = x.abs() as i64;
                (if x < 0 { !acc.0 } else { acc.0 }, acc.1.min(a), acc.2 + a)
            },
        ) {
            (true, _, total) => total,
            (false, smallest, total) => total - 2 * smallest,
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![1, -1], vec![-1, 1]], 4),
        (vec![vec![1, 2, 3], vec![-1, -2, -3], vec![1, 2, 3]], 16),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_matrix_sum(t.0.clone());
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
