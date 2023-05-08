// 1572. Matrix Diagonal Sum
// 🟢 Easy
//
// https://leetcode.com/problems/matrix-diagonal-sum/
//
// Tags: Array - Matrix

struct Solution;
impl Solution {
    /// A cell belongs to a diagonal if it fulfills either of two conditions,
    /// r == c => main positive diagonal or r+c == n-1 => main negative
    /// diagonal. We iterate over all cells, if it matches, we add its value to
    /// the result.
    ///
    /// Time complexity: O(n^2) - We iterate over all cells, for each, we check
    /// if it matches the conditions and, if it does, add it to the result.
    /// Space complexity: O(1) - We only store integer values and pointers.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.2 MB Beats 85.71%
    pub fn diagonal_sum(mat: Vec<Vec<i32>>) -> i32 {
        let n = mat.len();
        let mut res = 0;
        // Iterate over all cells checking if the cell belongs to a diagonal.
        for r in 0..n {
            for c in 0..n {
                if r == c || r + c == n - 1 {
                    res += mat[r][c];
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]], 25),
        (
            vec![
                vec![1, 1, 1, 1],
                vec![1, 1, 1, 1],
                vec![1, 1, 1, 1],
                vec![1, 1, 1, 1],
            ],
            8,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::diagonal_sum(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
