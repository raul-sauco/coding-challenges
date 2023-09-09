// 118. Pascal's Triangle
// 🟢 Easy
//
// https://leetcode.com/problems/pascals-triangle/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /// Generate the matrix using the problem description, each value in the
    /// matrix equals the sum of the values in the previous row in the same and
    /// the previous columns.
    ///
    /// Time complexity: O(n^2) - We iterate over each position of the matrix.
    /// There are n rows and each row can grow up to size n.
    /// Space complexity: O(n^2) - The size of the matrix we are generating.
    ///
    /// Runtime 1 ms Beats 78.79%
    /// Memory 2.14 MB Beats 32.73%
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = vec![];
        for i in 0..num_rows as usize {
            res.push(
                (0..i + 1)
                    .into_iter()
                    .map(|j| {
                        if j == 0 || j == i {
                            1
                        } else {
                            res[i - 1][j - 1] + res[i - 1][j]
                        }
                    })
                    .collect(),
            );
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        // (1, vec![vec![1]]),
        (
            5,
            vec![
                vec![1],
                vec![1, 1],
                vec![1, 2, 1],
                vec![1, 3, 3, 1],
                vec![1, 4, 6, 4, 1],
            ],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::generate(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
